#!/usr/bin/env python3
"""
知识包索引增量更新 - knowledge-index-update.py
功能：读取JSONL文件增量更新SQLite索引（含FTS5）+ 触发qmd索引
使用：python knowledge-index-update.py --project-path "<项目路径>" [--full-rebuild]
设计：增量优先，只处理sync_log时间戳之后的新增行
"""

import sqlite3
import json
import argparse
import os
from pathlib import Path
from datetime import datetime, timezone

import sys
# Windows PowerShell GBK编码修复：强制stdout用UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def get_last_sync(conn):
    """获取上次同步时间戳"""
    cursor = conn.execute("SELECT timestamp FROM sync_log ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    return row[0] if row else None

def read_jsonl_incremental(jsonl_path, last_sync):
    """增量读取JSONL，只返回created > last_sync的行"""
    results = []
    if not os.path.exists(jsonl_path):
        return results
    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                created = obj.get('created', '')
                if last_sync and created <= last_sync:
                    continue
                results.append(obj)
            except json.JSONDecodeError:
                continue
    return results

def update_claims(conn, claims):
    """更新claims表+FTS5"""
    added = 0
    for claim in claims:
        cid = claim.get('claim_id')
        if not cid:
            continue

        source = claim.get('source', {})
        characteristics = json.dumps(claim.get('characteristics', []), ensure_ascii=False)
        opposing = json.dumps(claim.get('opposing', []), ensure_ascii=False)
        possible_relations = json.dumps(claim.get('possible_relations', []), ensure_ascii=False)

        # 检查是否已存在
        existing = conn.execute("SELECT id FROM claims WHERE id = ?", (cid,)).fetchone()
        if existing:
            conn.execute("""
                UPDATE claims SET statement=?, boundary=?, source_id=?, source_title=?,
                source_type=?, characteristics=?, confidence=?, school=?,
                extraction_level=?, status=?, opposing=?, possible_relations=?, updated=?
                WHERE id=?
            """, (
                claim.get('statement', ''), claim.get('boundary', ''),
                source.get('id', ''), source.get('title', ''), source.get('type', ''),
                characteristics, claim.get('confidence', 0.5),
                claim.get('school', ''), claim.get('extraction_level', 'deep'),
                claim.get('status', 'active'), opposing, possible_relations,
                datetime.now(timezone.utc).isoformat(), cid
            ))
        else:
            conn.execute("""
                INSERT INTO claims (id, statement, boundary, source_id, source_title,
                source_type, characteristics, confidence, school, extraction_level,
                status, opposing, possible_relations, created, updated)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                cid, claim.get('statement', ''), claim.get('boundary', ''),
                source.get('id', ''), source.get('title', ''), source.get('type', ''),
                characteristics, claim.get('confidence', 0.5),
                claim.get('school', ''), claim.get('extraction_level', 'deep'),
                claim.get('status', 'active'), opposing, possible_relations,
                claim.get('created', datetime.now(timezone.utc).isoformat()),
                claim.get('created', datetime.now(timezone.utc).isoformat())
            ))
            added += 1

        # 更新FTS5
        try:
            conn.execute("DELETE FROM claims_fts WHERE claim_id = ?", (cid,))
            conn.execute("""
                INSERT INTO claims_fts (claim_id, statement, boundary, characteristics, source_title)
                VALUES (?,?,?,?,?)
            """, (
                cid, claim.get('statement', ''), claim.get('boundary', ''),
                characteristics, source.get('title', '')
            ))
        except sqlite3.OperationalError as e:
            print(f"  FTS5更新失败(claim {cid}): {e}")

    return added

def update_sources(conn, sources_from_claims):
    """从claims中提取source信息更新sources表"""
    for source in sources_from_claims:
        sid = source.get('id')
        if not sid:
            continue
        existing = conn.execute("SELECT id FROM sources WHERE id = ?", (sid,)).fetchone()
        if not existing:
            conn.execute("""
                INSERT OR IGNORE INTO sources (id, title, source_type, created)
                VALUES (?,?,?,?)
            """, (
                sid, source.get('title', ''), source.get('type', ''),
                datetime.now(timezone.utc).isoformat()
            ))

def update_debates(conn, debates):
    """更新debates表"""
    added = 0
    for debate in debates:
        did = debate.get('debate_id')
        if not did:
            continue
        positions = json.dumps(debate.get('positions', []), ensure_ascii=False)
        existing = conn.execute("SELECT id FROM debates WHERE id = ?", (did,)).fetchone()
        if not existing:
            conn.execute("""
                INSERT INTO debates (id, topic, positions, status, resolution, created)
                VALUES (?,?,?,?,?,?)
            """, (
                did, debate.get('topic', ''), positions,
                debate.get('status', 'coexist'), debate.get('resolution', ''),
                debate.get('created', datetime.now(timezone.utc).isoformat())
            ))
            added += 1
    return added

def update_schools(conn, schools):
    """更新schools表"""
    added = 0
    for school in schools:
        sid = school.get('school_id')
        if not sid:
            continue
        core_claims = json.dumps(school.get('core_claims', []), ensure_ascii=False)
        representatives = json.dumps(school.get('representatives', []), ensure_ascii=False)
        characteristics = json.dumps(school.get('characteristics', []), ensure_ascii=False)
        opposing = json.dumps(school.get('opposing_schools', []), ensure_ascii=False)
        existing = conn.execute("SELECT id FROM schools WHERE id = ?", (sid,)).fetchone()
        if not existing:
            conn.execute("""
                INSERT INTO schools (id, name, core_claims, representatives, boundaries,
                characteristics, evolution_path, opposing_schools, created)
                VALUES (?,?,?,?,?,?,?,?,?)
            """, (
                sid, school.get('name', ''), core_claims, representatives,
                school.get('boundaries', ''), characteristics,
                school.get('evolution_path', ''), opposing,
                school.get('created', datetime.now(timezone.utc).isoformat())
            ))
            added += 1
    return added

def update_leads(conn, leads):
    """更新source_leads表"""
    added = 0
    for lead in leads:
        lid = lead.get('lead_id')
        if not lid:
            continue
        existing = conn.execute("SELECT id, reference_count FROM source_leads WHERE id = ?", (lid,)).fetchone()
        if existing:
            # 更新引用计数
            new_count = existing[1] + lead.get('reference_count', 1) - 1
            conn.execute("UPDATE source_leads SET reference_count = ? WHERE id = ?", (max(new_count, existing[1]), lid))
        else:
            conn.execute("""
                INSERT INTO source_leads (id, trigger_type, target_type, target, context,
                source_article, priority, reference_count, related_outline_node, status, created)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
            """, (
                lid, lead.get('trigger_type', '新采集'), lead.get('target_type', 'URL'),
                lead.get('target', ''), lead.get('context', ''),
                lead.get('source_article', ''), lead.get('priority', 'P1'),
                lead.get('reference_count', 1), lead.get('related_outline_node', ''),
                lead.get('status', 'pending'),
                lead.get('created', datetime.now(timezone.utc).isoformat())
            ))
            added += 1
    return added

def full_rebuild(conn, pack_path):
    """全量重建：清空所有表，从JSONL重新加载"""
    for table in ['claims', 'claims_fts', 'debates', 'schools', 'source_leads', 'relations', 'concepts']:
        conn.execute(f"DELETE FROM {table}" if table != 'claims_fts' else f"DELETE FROM {table}")

    return incremental_update(conn, pack_path, last_sync=None)

def incremental_update(conn, pack_path, last_sync):
    """增量更新"""
    jsonl_dir = pack_path / 'jsonl'
    if not jsonl_dir.exists():
        jsonl_dir = pack_path  # 兼容：jsonl文件直接在pack根目录

    total_claims = 0
    total_debates = 0
    total_schools = 0
    total_leads = 0

    # claims.jsonl
    claims = read_jsonl_incremental(pack_path / 'claims.jsonl', last_sync)
    if claims:
        total_claims = update_claims(conn, claims)
        # 从claims提取source信息
        sources = set()
        for c in claims:
            s = c.get('source', {})
            if s.get('id'):
                sources.add(json.dumps(s, ensure_ascii=False))
        update_sources(conn, [json.loads(s) for s in sources])
        print(f"  claims: 新增{total_claims}条")

    # debates.jsonl
    debates = read_jsonl_incremental(pack_path / 'debates.jsonl', last_sync)
    if debates:
        total_debates = update_debates(conn, debates)
        print(f"  debates: 新增{total_debates}条")

    # schools.jsonl
    schools = read_jsonl_incremental(pack_path / 'schools.jsonl', last_sync)
    if schools:
        total_schools = update_schools(conn, schools)
        print(f"  schools: 新增{total_schools}条")

    # source-leads.jsonl
    leads = read_jsonl_incremental(pack_path / 'source-leads.jsonl', last_sync)
    if leads:
        total_leads = update_leads(conn, leads)
        print(f"  source-leads: 新增{total_leads}条")

    # 写sync_log
    conn.execute("""
        INSERT INTO sync_log (action, details, claims_added, claims_updated,
        conflicts_found, status_changes, timestamp)
        VALUES (?,?,?,?,?,?,?)
    """, (
        'incremental',
        f"claims={total_claims}, debates={total_debates}, schools={total_schools}, leads={total_leads}",
        total_claims, 0, 0, 0,
        datetime.now(timezone.utc).isoformat()
    ))

    return total_claims, total_debates, total_schools, total_leads

def main():
    parser = argparse.ArgumentParser(description='知识包索引增量更新')
    parser.add_argument('--project-path', required=True, help='项目路径')
    parser.add_argument('--full-rebuild', action='store_true', help='全量重建')
    args = parser.parse_args()

    pack_path = Path(args.project_path) / 'knowledge-pack'
    db_path = pack_path / 'index' / 'knowledge.db'

    if not db_path.exists():
        print(f"数据库不存在，请先运行 knowledge-db-init.py")
        return

    conn = sqlite3.connect(str(db_path))

    if args.full_rebuild:
        print("全量重建索引...")
        result = full_rebuild(conn, pack_path)
    else:
        last_sync = get_last_sync(conn)
        print(f"增量更新 (上次同步: {last_sync})...")
        result = incremental_update(conn, pack_path, last_sync)

    conn.commit()
    conn.close()
    print(f"索引更新完成: claims={result[0]}, debates={result[1]}, schools={result[2]}, leads={result[3]}")

if __name__ == '__main__':
    main()

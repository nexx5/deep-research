#!/usr/bin/env python3
"""
索引重建脚本：从存储层文件（A*/C*/旧JSON）提取结构化数据，写入SQLite索引层。
设计原则：文件是真相源，SQLite是影子索引。本脚本只读取文件，不修改任何文件。

⚠️ 新协议项目（有 knowledge-pack/claims.jsonl）请勿使用本脚本！
   新协议项目用 merge-batch.py + knowledge-index-update.py 增量更新。
   本脚本只适用于旧协议项目（无 knowledge-pack/ 目录）。

用法：
    python .opencode/scripts/rebuild-knowledge-index.py --project-path "<项目路径>"

权限：项目内脚本，--project-path 限定范围，不弹窗。
"""

import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

# Windows PowerShell GBK编码修复：强制stdout用UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


def validate_project_path(path: str) -> str:
    """确保路径存在且包含 project.config.md"""
    abs_path = os.path.abspath(path)
    if not os.path.isdir(abs_path):
        print(f"ERROR: 路径不存在: {abs_path}", file=sys.stderr)
        sys.exit(1)
    config = os.path.join(abs_path, "project.config.md")
    if not os.path.exists(config):
        # 兼容旧项目结构（0-规划/task_queue.md）
        if not os.path.exists(os.path.join(abs_path, "0-规划")) and not os.path.exists(os.path.join(abs_path, "1-规划")):
            print(f"ERROR: 不是有效的项目目录（缺少 project.config.md）: {abs_path}", file=sys.stderr)
            sys.exit(1)
    return abs_path


def find_files(project_path: str, patterns: list) -> list:
    """在项目目录内按文件名模式查找文件"""
    results = []
    for root, dirs, files in os.walk(project_path):
        # 跳过 .opencode 和 .task 目录
        dirs[:] = [d for d in dirs if d not in ('.opencode', '.task', '__pycache__')]
        for f in files:
            for pattern in patterns:
                if Path(f).match(pattern) and '模板' not in f:
                    results.append(os.path.join(root, f))
                    break
    return results


def extract_source_id(filename: str) -> str:
    """从文件名提取 S{id}，如 分析-A062-RedFoxHub.md → 不适用；raw-S062-RedFoxHub.md → S062"""
    m = re.search(r'S(\d{3})', filename)
    return f"S{m.group(1)}" if m else None


def extract_analysis_id(filename: str) -> str:
    """从文件名提取 A{id}"""
    m = re.search(r'A(\d{3})', filename)
    return f"A{m.group(1)}" if m else None


def extract_comparison_id(filename: str) -> str:
    """从文件名提取 C{id}"""
    m = re.search(r'C(\d{3})', filename)
    return f"C{m.group(1)}" if m else None


def parse_key_claims(content: str, analysis_id: str) -> list:
    """
    从A*文件中解析 key_claims 结构化段。
    格式：
    ## key_claims（结构化断言，知识管理员提取用）
    | claim_id | subject | predicate | object | boundary | confidence | sources |
    |---|---|---|---|---|---|---|
    | 1 | RedFoxHub | 提供 | 微信公众号正文读取路径 | ... | M | S062 |
    """
    claims = []
    # 匹配 key_claims 段
    m = re.search(
        r'##\s*key_claims.*?\n((?:\|[^\n]+\n)+)',
        content, re.DOTALL
    )
    if not m:
        return claims

    table_text = m.group(1)
    lines = table_text.strip().split('\n')

    for line in lines:
        line = line.strip()
        if not line.startswith('|') or '---' in line:
            continue
        cells = [c.strip() for c in line.split('|')]
        # 去掉首尾空
        cells = [c for c in cells if c != '']
        if len(cells) < 7:
            continue
        try:
            local_id = cells[0]
            subject = cells[1]
            predicate = cells[2]
            obj = cells[3]
            boundary = cells[4] if cells[4] else "未明确"
            confidence = cells[5] if cells[5] else "M"
            sources = cells[6]
            # 解析 sources（可能是 S062 或 S062,S063）
            src_list = [s.strip() for s in re.split(r'[,，]', sources) if s.strip()]

            claim_id = f"CL_{analysis_id}_{local_id}"
            claims.append({
                'id': claim_id,
                'subject': subject,
                'predicate': predicate,
                'object': obj,
                'boundary': boundary,
                'status': 'active',
                'confidence': confidence,
                'sources': json.dumps(src_list),
                'concepts': json.dumps([]),  # 概念标签后续填充
                'created': datetime.now().isoformat(),
                'extracted_from': json.dumps([analysis_id]),
                'extraction_method': 'key_claims',
            })
        except (IndexError, ValueError):
            continue

    return claims


def extract_concepts_from_claims(claims: list) -> dict:
    """从断言列表中提取概念标签（subject 和 object 都是概念候选）"""
    concepts = {}
    for claim in claims:
        for concept_candidate in [claim['subject'], claim['object']]:
            concept = concept_candidate.strip()
            if not concept or concept == "未明确":
                continue
            if concept not in concepts:
                concepts[concept] = {'claim_ids': [], 'source_ids': []}
            concepts[concept]['claim_ids'].append(claim['id'])
            for src in json.loads(claim['sources']):
                if src not in concepts[concept]['source_ids']:
                    concepts[concept]['source_ids'].append(src)
    return concepts


def extract_findings_from_content(content: str, max_len: int = 200) -> str:
    """从A*文件内容提取一句话关键发现摘要"""
    # 找"核心价值"或"核心结论"段的第一条
    for section in ['核心结论', '核心价值', '核心发现']:
        m = re.search(rf'##\s*{section}.*?\n\s*\d+\.\s*(.+?)(?:\n|$)', content, re.DOTALL)
        if m:
            finding = m.group(1).strip()[:max_len]
            return finding
    return ""


def migrate_old_json_sources(conn: sqlite3.Connection, project_path: str) -> int:
    """从旧 knowledge-pack JSON 的 source_registry 迁移来源元数据"""
    count = 0
    kp_files = find_files(project_path, ['knowledge-pack*.json'])
    for kp_path in kp_files:
        if 'archived' in kp_path:
            continue
        try:
            with open(kp_path, 'r', encoding='utf-8') as f:
                kp = json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue

        source_registry = kp.get('source_registry', [])
        if isinstance(source_registry, dict):
            source_registry = list(source_registry.values())

        for src in source_registry:
            if not isinstance(src, dict):
                continue
            src_id = src.get('source_id', '')
            if not src_id:
                continue
            # 检查是否已存在
            existing = conn.execute("SELECT id FROM sources WHERE id = ?", (src_id,)).fetchone()
            if existing:
                # 更新 key_findings 如果为空
                if not conn.execute("SELECT key_findings FROM sources WHERE id = ?", (src_id,)).fetchone()[0]:
                    display = src.get('display_citation', '')
                    conn.execute(
                        "UPDATE sources SET key_findings = ? WHERE id = ?",
                        (display[:200], src_id)
                    )
                continue

            title = src.get('title', src.get('display_citation', src_id))
            url = src.get('url', '')
            src_type = src.get('source_type', 'unknown')
            created = src.get('created', src.get('collected_date', ''))
            raw_path = src.get('raw_path', '')
            extract_path = src.get('extract_path', '')
            analysis_ids = src.get('analysis_ids', [])
            if isinstance(analysis_ids, list):
                analysis_ids = json.dumps(analysis_ids)

            conn.execute("""
                INSERT OR IGNORE INTO sources (id, title, key_findings, url, source_type, created, raw_path, extract_path, analysis_ids)
                VALUES (?, ?, '', ?, ?, ?, ?, ?, ?)
            """, (src_id, title, url, src_type, created or '', raw_path, extract_path, analysis_ids))
            count += 1

    return count


def parse_comparison_metadata(filepath: str, comp_id: str) -> dict:
    """从C*文件提取对比文档元数据"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='gbk', errors='replace') as f:
            content = f.read()

    # 提取主题（第一个标题）
    m = re.search(r'^#\s+(.+?)$', content, re.MULTILINE)
    topic = m.group(1).strip() if m else comp_id

    # 提取日期（找文件中的日期模式 YYYY-MM-DD）
    dates = re.findall(r'20\d{2}-\d{2}-\d{2}', content)
    latest_date = max(dates) if dates else ''

    # 统计引用的来源数（S\d{3} 出现次数）
    source_refs = set(re.findall(r'S\d{3}', content))

    return {
        'id': comp_id,
        'topic': topic,
        'status': 'active',
        'version': 1,
        'last_updated': latest_date,
        'superseded_by': None,
        'file_path': filepath,
        'source_count': len(source_refs),
        'latest_source_date': latest_date,
    }


def rebuild_index(project_path: str, verbose: bool = False):
    """主函数：重建知识索引"""
    # 新协议保护：检测到 claims.jsonl 则拒绝执行
    jsonl_path = os.path.join(project_path, 'knowledge-pack', 'claims.jsonl')
    if os.path.exists(jsonl_path):
        print("ERROR: 检测到 knowledge-pack/claims.jsonl，这是新协议项目。", file=sys.stderr)
        print("       新协议项目请勿使用 rebuild-knowledge-index.py，会破坏数据。", file=sys.stderr)
        print("       请使用 merge-batch.py + knowledge-index-update.py 增量更新。", file=sys.stderr)
        sys.exit(1)

    # 确定 SQLite 路径（优先新协议 knowledge-pack/index）
    knowledge_dir = None
    db_filename = None
    for candidate in ['knowledge-pack/index', '2-执行/03-知识提炼', '03-知识提炼']:
        p = os.path.join(project_path, candidate)
        if os.path.isdir(p):
            # 检查已有的DB文件
            for db_name in ['knowledge.db', 'knowledge-index.db']:
                if os.path.exists(os.path.join(p, db_name)):
                    knowledge_dir = p
                    db_filename = db_name
                    break
            if not knowledge_dir:
                # 目录存在但无DB文件
                knowledge_dir = p
                db_filename = 'knowledge.db' if 'knowledge-pack' in candidate else 'knowledge-index.db'
            break

    if not knowledge_dir:
        # 创建新协议目录
        knowledge_dir = os.path.join(project_path, 'knowledge-pack', 'index')
        os.makedirs(knowledge_dir, exist_ok=True)
        db_filename = 'knowledge.db'

    db_path = os.path.join(knowledge_dir, db_filename)

    # 如果 DB 已存在，先备份
    if os.path.exists(db_path):
        backup_path = db_path.replace('.db', f'.backup.db')
        os.rename(db_path, backup_path)
        if verbose:
            print(f"  旧DB已备份: {backup_path}")

    # 读取 schema
    schema_path = os.path.join(os.path.dirname(__file__), 'knowledge-schema.sql')
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema_sql = f.read()

    # 创建新 DB
    conn = sqlite3.connect(db_path)
    conn.executescript(schema_sql)
    conn.commit()

    stats = {
        'sources': 0,
        'claims': 0,
        'concepts': 0,
        'comparisons': 0,
        'fts_entries': 0,
    }

    # ============================================================
    # Step 1: 从旧 JSON 迁移来源元数据
    # ============================================================
    if verbose:
        print("Step 1: 迁移旧JSON来源元数据...")
    migrated = migrate_old_json_sources(conn, project_path)
    stats['sources'] = migrated
    if verbose:
        print(f"  迁移了 {migrated} 个来源")

    # ============================================================
    # Step 2: 从 A*.md 文件提取来源元数据 + 断言
    # ============================================================
    if verbose:
        print("Step 2: 扫描单源分析文件...")
    analysis_files = find_files(project_path, ['分析-A*.md'])
    # 排除模板
    analysis_files = [f for f in analysis_files if '模板' not in os.path.basename(f)]

    all_claims = []
    for afile in analysis_files:
        analysis_id = extract_analysis_id(os.path.basename(afile))
        if not analysis_id:
            continue

        try:
            with open(afile, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(afile, 'r', encoding='gbk', errors='replace') as f:
                content = f.read()

        # 提取来源ID
        m = re.search(r'来源ID:\s*S(\d{3})', content)
        source_id = f"S{m.group(1)}" if m else None

        # 提取 key_findings
        key_finding = extract_findings_from_content(content)

        # 更新或插入 source 记录
        if source_id:
            existing = conn.execute("SELECT id FROM sources WHERE id = ?", (source_id,)).fetchone()
            if existing:
                if key_finding:
                    conn.execute("UPDATE sources SET key_findings = ?, analysis_ids = ? WHERE id = ?",
                                 (key_finding, json.dumps([analysis_id]), source_id))
            else:
                # 从文件名提取标题
                title_match = re.search(r'分析-A\d{3}-(.+?)\.md', os.path.basename(afile))
                title = title_match.group(1) if title_match else analysis_id
                conn.execute("""
                    INSERT OR IGNORE INTO sources (id, title, key_findings, url, source_type, created, raw_path, extract_path, analysis_ids)
                    VALUES (?, ?, ?, '', 'unknown', '', '', '', ?)
                """, (source_id, title, key_finding, json.dumps([analysis_id])))
                stats['sources'] += 1

        # 提取 key_claims
        claims = parse_key_claims(content, analysis_id)
        all_claims.extend(claims)

        if verbose and claims:
            print(f"  {analysis_id}: 提取了 {len(claims)} 条断言")

    # ============================================================
    # Step 3: 写入断言
    # ============================================================
    if verbose:
        print("Step 3: 写入断言...")
    for claim in all_claims:
        conn.execute("""
            INSERT OR REPLACE INTO claims
            (id, subject, predicate, object, boundary, status, confidence, sources, concepts,
             created, updated, supersedes, superseded_by, superseded_reason, extracted_from,
             extraction_method, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL, NULL, ?, ?, NULL)
        """, (
            claim['id'], claim['subject'], claim['predicate'], claim['object'],
            claim['boundary'], claim['status'], claim['confidence'],
            claim['sources'], claim['concepts'], claim['created'],
            claim['extracted_from'], claim['extraction_method']
        ))
    stats['claims'] = len(all_claims)

    # ============================================================
    # Step 4: 提取概念索引
    # ============================================================
    if verbose:
        print("Step 4: 建立概念索引...")
    concepts = extract_concepts_from_claims(all_claims)
    for concept, data in concepts.items():
        conn.execute("""
            INSERT OR REPLACE INTO concepts (concept, claim_ids, source_ids)
            VALUES (?, ?, ?)
        """, (concept, json.dumps(data['claim_ids']), json.dumps(data['source_ids'])))
    stats['concepts'] = len(concepts)

    # ============================================================
    # Step 5: 解析 C*.md 对比文档
    # ============================================================
    if verbose:
        print("Step 5: 扫描对比文档...")
    comparison_files = find_files(project_path, ['对比-C*.md', '链-C*.md'])
    comparison_files = [f for f in comparison_files if '模板' not in os.path.basename(f)]

    for cfile in comparison_files:
        comp_id = extract_comparison_id(os.path.basename(cfile))
        if not comp_id:
            continue
        meta = parse_comparison_metadata(cfile, comp_id)
        conn.execute("""
            INSERT OR REPLACE INTO comparisons
            (id, topic, status, version, last_updated, superseded_by, file_path, source_count, latest_source_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            meta['id'], meta['topic'], meta['status'], meta['version'],
            meta['last_updated'], meta['superseded_by'], meta['file_path'],
            meta['source_count'], meta['latest_source_date']
        ))
        stats['comparisons'] += 1

    # ============================================================
    # Step 6: 手动填充 FTS5 索引
    # ============================================================
    if verbose:
        print("Step 6: 填充全文索引...")
    conn.execute("DELETE FROM claims_fts;")
    all_claim_rows = conn.execute(
        "SELECT id, subject, predicate, object, boundary FROM claims"
    ).fetchall()
    for row in all_claim_rows:
        conn.execute("""
            INSERT INTO claims_fts (claim_id, subject, predicate, object, boundary)
            VALUES (?, ?, ?, ?, ?)
        """, (row[0], row[1], row[2], row[3], row[4] or ''))
    fts_count = conn.execute("SELECT COUNT(*) FROM claims_fts").fetchone()[0]
    stats['fts_entries'] = fts_count

    # ============================================================
    # Step 7: 记录同步日志
    # ============================================================
    conn.execute("""
        INSERT INTO sync_log (action, details, claims_added, claims_updated, conflicts_found, status_changes, timestamp)
        VALUES (?, ?, ?, 0, 0, 0, ?)
    """, (
        'rebuild',
        json.dumps({'stats': stats, 'project': project_path}, ensure_ascii=False),
        stats['claims'],
        datetime.now().isoformat()
    ))

    conn.commit()

    # ============================================================
    # 输出统计
    # ============================================================
    result = {
        'status': 'success',
        'project_path': project_path,
        'db_path': db_path,
        'stats': stats,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))

    conn.close()
    return result


def main():
    parser = argparse.ArgumentParser(description='知识体系索引重建')
    parser.add_argument('--project-path', required=True, type=validate_project_path,
                        help='项目根目录路径')
    parser.add_argument('--verbose', '-v', action='store_true', help='详细输出')
    args = parser.parse_args()

    if args.verbose:
        print(f"项目路径: {args.project_path}")
        print(f"开始重建索引...")

    rebuild_index(args.project_path, verbose=args.verbose)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
检查点工具 - checkpoint.py
功能：保存/恢复批次执行状态，支持中断恢复
使用：
  python checkpoint.py --project-path "<项目路径>" --save --batch-id 5 --phase merge
  python checkpoint.py --project-path "<项目路径>" --load
  python checkpoint.py --project-path "<项目路径>" --check
"""

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

def count_jsonl(path):
    """统计JSONL行数"""
    if not path.exists():
        return 0
    count = 0
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                count += 1
    return count

def count_evidence_files(evidence_path):
    """统计evidence目录文件数"""
    if not evidence_path.exists():
        return {'raw': 0, 'extract': 0, 'analysis': 0}
    return {
        'raw': len(list(evidence_path.glob('raw-S*.md'))),
        'extract': len(list(evidence_path.glob('采录-S*.md'))),
        'analysis': len(list(evidence_path.glob('分析-A*.md')))
    }

def save_checkpoint(pack_path, batch_id, phase, sources_done, sources_remaining, lead_pool_status):
    """保存检查点"""
    state = {
        'batch_id': batch_id,
        'phase': phase,  # discover/extract/merge/systematize/saturated
        'sources_done': sources_done,
        'sources_remaining': sources_remaining,
        'claims_count': count_jsonl(pack_path / 'claims.jsonl'),
        'debates_count': count_jsonl(pack_path / 'debates.jsonl'),
        'schools_count': count_jsonl(pack_path / 'schools.jsonl'),
        'leads_count': count_jsonl(pack_path / 'source-leads.jsonl'),
        'evidence_files': count_evidence_files(pack_path / 'evidence'),
        'lead_pool': lead_pool_status,
        'last_checkpoint': datetime.now(timezone.utc).isoformat()
    }

    state_path = pack_path / 'batch-state.json'
    tmp_path = pack_path / 'batch-state.json.tmp'
    with open(tmp_path, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
        f.flush()
        os.fsync(f.fileno())
    os.replace(str(tmp_path), str(state_path))  # 原子 rename
    print(f"检查点已保存: batch={batch_id}, phase={phase}")
    return state

def load_checkpoint(pack_path):
    """加载检查点"""
    state_path = pack_path / 'batch-state.json'
    if not state_path.exists():
        print("无检查点文件")
        return None

    with open(state_path, 'r', encoding='utf-8') as f:
        state = json.load(f)
    print(f"检查点: batch={state['batch_id']}, phase={state['phase']}")
    print(f"  sources_done={state['sources_done']}, remaining={state['sources_remaining']}")
    print(f"  claims={state['claims_count']}, debates={state['debates_count']}")
    print(f"  schools={state['schools_count']}, leads={state['leads_count']}")
    return state

def consistency_check(pack_path):
    """一致性检查：JSONL行数 vs evidence文件数 vs SQLite行数"""
    issues = []

    # JSONL行数
    claims_jsonl = count_jsonl(pack_path / 'claims.jsonl')
    debates_jsonl = count_jsonl(pack_path / 'debates.jsonl')

    # evidence文件数
    evidence = count_evidence_files(pack_path / 'evidence')

    # SQLite行数
    db_path = pack_path / 'index' / 'knowledge.db'
    sqlite_claims = 0
    sqlite_debates = 0
    if db_path.exists():
        import sqlite3
        conn = sqlite3.connect(str(db_path))
        sqlite_claims = conn.execute("SELECT COUNT(*) FROM claims").fetchone()[0]
        # debates 表仅旧协议存在；新协议(zhishibao claims.jsonl)无此表，缺表时视为 0
        try:
            sqlite_debates = conn.execute("SELECT COUNT(*) FROM debates").fetchone()[0]
        except sqlite3.OperationalError:
            sqlite_debates = 0
            issues.append("debates 表不存在（新协议项目正常，旧协议 debates 已并入 claims 的 opposing 字段）")
        conn.close()
    else:
        issues.append("SQLite数据库不存在")

    # 检查一致性
    if claims_jsonl != sqlite_claims:
        issues.append(f"claims不一致: JSONL={claims_jsonl}, SQLite={sqlite_claims}")
    if debates_jsonl != sqlite_debates:
        issues.append(f"debates不一致: JSONL={debates_jsonl}, SQLite={sqlite_debates}")

    # qmd索引检查
    qmd_manifest = pack_path / 'index' / 'qmd-index' / 'manifest.json'
    if qmd_manifest.exists():
        with open(qmd_manifest, 'r', encoding='utf-8') as f:
            qmd_data = json.load(f)
        qmd_files = len(qmd_data.get('indexed_files', []))
        evidence_total = evidence['raw'] + evidence['extract']
        if qmd_files != evidence_total:
            issues.append(f"qmd索引不一致: 索引={qmd_files}, evidence={evidence_total}")
    else:
        issues.append("qmd索引manifest不存在（可能未初始化）")

    if issues:
        print("一致性检查发现问题:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("一致性检查通过")

    print(f"\n统计:")
    print(f"  claims: JSONL={claims_jsonl}, SQLite={sqlite_claims}")
    print(f"  debates: JSONL={debates_jsonl}, SQLite={sqlite_debates}")
    print(f"  evidence: raw={evidence['raw']}, extract={evidence['extract']}, analysis={evidence['analysis']}")

    return issues

def main():
    parser = argparse.ArgumentParser(description='检查点工具')
    parser.add_argument('--project-path', required=True)
    parser.add_argument('--save', action='store_true')
    parser.add_argument('--load', action='store_true')
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--batch-id', default='')
    parser.add_argument('--phase', default='')
    parser.add_argument('--sources-done', type=int, default=0)
    parser.add_argument('--sources-remaining', type=int, default=0)
    parser.add_argument('--lead-pool', default='{"P0":0,"P1":0}')
    args = parser.parse_args()

    pack_path = Path(args.project_path) / 'knowledge-pack'

    if args.save:
        lead_pool = json.loads(args.lead_pool)
        save_checkpoint(pack_path, args.batch_id, args.phase,
                       args.sources_done, args.sources_remaining, lead_pool)
    elif args.load:
        load_checkpoint(pack_path)
    elif args.check:
        consistency_check(pack_path)
    else:
        print("请指定 --save / --load / --check")

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
批次合并工具 - merge-batch.py
功能：读取批次内采录+分析文件，做跨源对比+冲突检测+debate生成
使用：python merge-batch.py --project-path "<项目路径>" --batch-id <批次号>
设计：不同特点→coexist（不处理）；同特点同边界矛盾→debate(unresolved)
模型：本脚本只做数据层操作，LLM推理由合并agent(强模型)完成
"""

import sqlite3
import json
import argparse
import os
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict

import sys
# Windows PowerShell GBK编码修复：强制stdout用UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def load_batch_claims(pack_path, batch_source_ids):
    """加载批次内所有claims"""
    claims = []
    claims_path = pack_path / 'claims.jsonl'
    if not claims_path.exists():
        return claims

    with open(claims_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                claim = json.loads(line)
                if claim.get('source', {}).get('id') in batch_source_ids:
                    claims.append(claim)
            except json.JSONDecodeError:
                continue
    return claims

def group_by_characteristics(claims):
    """按characteristics分组，用于跨源关联"""
    groups = defaultdict(list)
    for claim in claims:
        chars = claim.get('characteristics', [])
        # 每个特点标签都可能关联到其他同标签的断言
        for char in chars:
            groups[char].append(claim)
    return groups

def detect_conflicts(conn, claims):
    """
    冲突检测：两阶段预筛
    1. 预筛：同subject(statement前缀)不同结论 → 候选冲突组
    2. 细筛：比boundary和characteristics
       - 不同特点 → coexist（不处理）
       - 同特点同边界矛盾 → debate(unresolved)
    """
    # 获取所有已有claims用于对比
    existing_claims = []
    cursor = conn.execute("SELECT id, statement, boundary, characteristics, source_id FROM claims")
    for row in cursor:
        existing_claims.append({
            'claim_id': row[0],
            'statement': row[1],
            'boundary': row[2],
            'characteristics': json.loads(row[3]) if row[3] else [],
            'source_id': row[4]
        })

    conflicts = []
    coexists = []

    for new_claim in claims:
        new_stmt = new_claim.get('statement', '')
        new_boundary = new_claim.get('boundary', '')
        new_chars = set(new_claim.get('characteristics', []))
        new_id = new_claim.get('claim_id', '')

        for existing in existing_claims:
            if existing['claim_id'] == new_id:
                continue

            # 预筛：statement前缀相似（同主题）
            # 简化判断：前20字符有重叠
            if not any(w in existing['statement'] for w in new_stmt.split()[:3] if len(w) > 2):
                continue

            # 细筛：比特点
            existing_chars = set(existing.get('characteristics', []))
            char_overlap = new_chars & existing_chars

            if not char_overlap:
                # 不同特点 → coexist
                coexists.append({
                    'claim_a': new_id,
                    'claim_b': existing['claim_id'],
                    'reason': '不同特点方案共存',
                    'new_chars': list(new_chars),
                    'existing_chars': list(existing_chars)
                })
                continue

            # 同特点：比boundary
            if new_boundary and existing['boundary']:
                if new_boundary == existing['boundary']:
                    # 同特点同边界 → 可能真冲突
                    conflicts.append({
                        'claim_a': new_id,
                        'claim_b': existing['claim_id'],
                        'statement_a': new_stmt,
                        'statement_b': existing['statement'],
                        'shared_characteristics': list(char_overlap),
                        'shared_boundary': new_boundary,
                        'reason': '同特点同边界矛盾'
                    })
                else:
                    # 同特点不同边界 → coexist（不同条件下成立）
                    coexists.append({
                        'claim_a': new_id,
                        'claim_b': existing['claim_id'],
                        'reason': '同特点不同边界共存',
                        'boundary_a': new_boundary,
                        'boundary_b': existing['boundary']
                    })

    return conflicts, coexists

def generate_debates(conflicts, existing_debate_count):
    """从冲突生成debate条目"""
    debates = []
    for i, conflict in enumerate(conflicts):
        debate_id = f"DB{existing_debate_count + i + 1:04d}"
        debate = {
            'debate_id': debate_id,
            'topic': f"断言冲突: {conflict['statement_a'][:50]}...",
            'positions': [
                {
                    'name': '立场A',
                    'claims': [conflict['claim_a']],
                    'characteristics': conflict['shared_characteristics'],
                    'representatives': [],
                    'pros': [],
                    'cons': [],
                    'evidence_strength': 'moderate'
                },
                {
                    'name': '立场B',
                    'claims': [conflict['claim_b']],
                    'characteristics': conflict['shared_characteristics'],
                    'representatives': [],
                    'pros': [],
                    'cons': [],
                    'evidence_strength': 'moderate'
                }
            ],
            'status': 'unresolved',
            'resolution': f"待仲裁：{conflict['reason']}",
            'created': datetime.now(timezone.utc).isoformat()
        }
        debates.append(debate)
    return debates

def append_to_jsonl(path, items):
    """追加写入JSONL"""
    with open(path, 'a', encoding='utf-8') as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

def write_merge_report(pack_path, batch_id, stats):
    """写合并报告"""
    report_path = pack_path / 'index' / f'merge-report-batch{batch_id}.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

def main():
    parser = argparse.ArgumentParser(description='批次合并工具')
    parser.add_argument('--project-path', required=True)
    parser.add_argument('--batch-id', required=True)
    parser.add_argument('--source-ids', required=True, help='逗号分隔的source_id列表')
    args = parser.parse_args()

    pack_path = Path(args.project_path) / 'knowledge-pack'
    db_path = pack_path / 'index' / 'knowledge.db'

    batch_source_ids = set(args.source_ids.split(','))
    print(f"批次 {args.batch_id}: {len(batch_source_ids)} 个来源")

    # 加载批次claims
    claims = load_batch_claims(pack_path, batch_source_ids)
    print(f"加载 {len(claims)} 条claims")

    if not claims:
        print("无claims需要合并")
        return

    # 按特点分组
    char_groups = group_by_characteristics(claims)
    print(f"特点分组: {len(char_groups)} 组")
    for char, group in list(char_groups.items())[:5]:
        print(f"  {char}: {len(group)} 条")

    # 冲突检测
    conn = sqlite3.connect(str(db_path))
    conflicts, coexists = detect_conflicts(conn, claims)
    print(f"冲突检测: {len(conflicts)} 真冲突, {len(coexists)} 共存")

    # 生成debates
    existing_debates = conn.execute("SELECT COUNT(*) FROM debates").fetchone()[0]
    new_debates = generate_debates(conflicts, existing_debates)

    # 追加debates.jsonl
    if new_debates:
        append_to_jsonl(pack_path / 'debates.jsonl', new_debates)
        print(f"追加 {len(new_debates)} 条debates")

    # 写合并报告
    stats = {
        'batch_id': args.batch_id,
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'claims_processed': len(claims),
        'characteristic_groups': len(char_groups),
        'conflicts_found': len(conflicts),
        'coexists_found': len(coexists),
        'debates_generated': len(new_debates)
    }
    write_merge_report(pack_path, args.batch_id, stats)

    conn.close()
    print(f"合并完成: {stats}")

if __name__ == '__main__':
    main()

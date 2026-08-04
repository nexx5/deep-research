#!/usr/bin/env python3
"""
线索识别工具 - lead-identifier.py
功能：扫描md文件正文，用关键词正则识别7+类线索，输出结构化线索清单
使用：python lead-identifier.py --input <md文件路径> [--output <输出jsonl路径>]
设计：触发类型×识别对象矩阵，关键词可扩展
"""

import re
import json
import argparse
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# 修复Windows控制台编码
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# ============================================================
# 关键词正则表（可扩展，非技术领域已补充）
# ============================================================

LEAD_PATTERNS = {
    "论文": [
        r'arxiv\.org/\S+',
        r'doi\.org/\S+',
        r'(?:ICML|KDD|NeurIPS|ACL|WWW|CVPR|AAAI|IJCAI)\s*\d{4}',
        r'论文',
        r'paper',
        r'et\s+al\.?',
        r'Proceedings',
        r'arXiv:\d{4}\.\d+',
    ],
    "仓库": [
        r'github\.com/[\w.-]+/[\w.-]+',
        r'gitee\.com/[\w.-]+/[\w.-]+',
        r'gitlab\.com/[\w.-]+/[\w.-]+',
        r'开源项目',
        r'仓库地址',
        r'repo(?:sitory)?',
    ],
    "概念": [
        r'参见.{0,20}',
        r'参考.{0,20}方法',
        r'(?:提出|首创|源于|借鉴).{0,30}',
        r'(?:定义|界定).{0,30}',
    ],
    "对立": [
        r'然而.{0,40}',
        r'但是.{0,40}',
        r'相反.{0,30}',
        r'不同于.{0,30}',
        r'反驳.{0,30}',
        r'质疑.{0,30}',
        r'缺陷.{0,30}',
        r'问题在于.{0,40}',
        r'局限.{0,30}',
    ],
    "数据": [
        r'\d+\.?\d*\s*%',
        r'\d+\s*倍',
        r'SOTA',
        r'benchmark',
        r'实测',
        r'提升\s*\d+',
        r'降低\s*\d+',
        r'准确率.{0,20}\d+',
    ],
    "方法": [
        r'(?:提出|设计|实现).{0,20}(?:方法|算法|框架|架构|策略|机制|范式)',
        r'(?:方法|算法|框架|架构|策略|机制|范式).{0,10}(?:称为|叫做|命名为)',
    ],
    "人物": [
        r'(?:作者|团队|实验室|大学|研究院).{0,30}',
        r'(?:教授|博士|研究员).{0,20}',
    ],
    "政策": [
        r'(?:法规|标准|规范|条例|政策|监管).{0,30}',
        r'GB/\S+',
        r'ISO\s*\d+',
    ],
    "案例": [
        r'(?:案例|实例|实践|踩坑|经验|教训).{0,30}',
        r'在实际应用中',
        r'生产环境',
    ],
    "URL": [
        r'https?://[\w.-]+/[\w/_.-]+',
    ],
}

# 触发类型推断
TRIGGER_INFERENCE = {
    "论文": "新采集",
    "仓库": "新采集",
    "概念": "缺口",
    "对立": "冲突",
    "数据": "验证",
    "方法": "新采集",
    "人物": "新采集",
    "政策": "新采集",
    "案例": "新采集",
    "URL": "新采集",
}

# STORM多视角扫描关键词（补充线索发现）
PERSPECTIVE_KEYWORDS = {
    "实践者": ["实际", "部署", "落地", "生产", "工程", "实践", "踩坑"],
    "怀疑论者": ["质疑", "问题", "局限", "缺陷", "不足", "风险", "批评"],
    "学术": ["论文", "实验", "理论", "证明", "推导", "公式", "基准"],
    "经济": ["成本", "效率", "性能", "价格", "商业化", "市场", "ROI"],
}

def identify_leads(text, source_article):
    """扫描文本，识别所有线索"""
    leads = []
    lead_counter = 0

    for target_type, patterns in LEAD_PATTERNS.items():
        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                context = text[start:end].replace('\n', ' ').strip()

                target = match.group(0).strip()

                # 去重：同target在同篇文章中只记一次
                if any(l['target'] == target and l['source_article'] == source_article for l in leads):
                    continue

                trigger_type = TRIGGER_INFERENCE.get(target_type, "新采集")

                lead_counter += 1
                leads.append({
                    "lead_id": f"LD{lead_counter:06d}",
                    "trigger_type": trigger_type,
                    "target_type": target_type,
                    "target": target,
                    "context": context,
                    "source_article": source_article,
                    "priority": "P1",  # 默认P1，强模型评估时调整
                    "reference_count": 1,
                    "related_outline_node": "",
                    "status": "pending",
                    "created": datetime.now(timezone.utc).isoformat()
                })

    # STORM多视角扫描：检查缺什么视角
    found_perspectives = set()
    for perspective, keywords in PERSPECTIVE_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                found_perspectives.add(perspective)
                break

    missing_perspectives = set(PERSPECTIVE_KEYWORDS.keys()) - found_perspectives
    for missing in missing_perspectives:
        lead_counter += 1
        leads.append({
            "lead_id": f"LD{lead_counter:06d}",
            "trigger_type": "缺口",
            "target_type": "方法",
            "target": f"缺少{missing}视角的分析",
            "context": f"本文未涉及{missing}视角（关键词：{', '.join(PERSPECTIVE_KEYWORDS[missing][:3])}）",
            "source_article": source_article,
            "priority": "P2",
            "reference_count": 1,
            "related_outline_node": "",
            "status": "pending",
            "created": datetime.now(timezone.utc).isoformat()
        })

    return leads

def merge_duplicate_leads(leads_list):
    """合并重复线索：同target被多篇文章引用→合并，reference_count+1"""
    merged = {}
    for leads in leads_list:
        for lead in leads:
            key = (lead['target'], lead['target_type'])
            if key in merged:
                merged[key]['reference_count'] += 1
                # P0条件：被≥3篇文章引用
                if merged[key]['reference_count'] >= 3:
                    merged[key]['priority'] = 'P0'
            else:
                merged[key] = lead.copy()
    return list(merged.values())

def main():
    parser = argparse.ArgumentParser(description='线索识别工具')
    parser.add_argument('--input', required=True, help='输入md文件路径（单个文件或目录）')
    parser.add_argument('--output', help='输出jsonl路径（默认追加到stdout）')
    parser.add_argument('--merge', action='store_true', help='合并重复线索')
    args = parser.parse_args()

    input_path = Path(args.input)
    all_leads = []

    if input_path.is_dir():
        md_files = list(input_path.glob('**/*.md'))
    else:
        md_files = [input_path]

    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            text = f.read()
        source_article = md_file.name
        leads = identify_leads(text, source_article)
        all_leads.extend(leads)
        print(f"[{source_article}] 识别到 {len(leads)} 条线索", flush=True)

    if args.merge:
        all_leads = merge_duplicate_leads([all_leads])
        print(f"合并去重后 {len(all_leads)} 条线索", flush=True)

    output_lines = [json.dumps(lead, ensure_ascii=False) for lead in all_leads]

    if args.output:
        with open(args.output, 'a', encoding='utf-8') as f:
            for line in output_lines:
                f.write(line + '\n')
        print(f"已写入 {args.output}", flush=True)
    else:
        for line in output_lines:
            print(line)

if __name__ == '__main__':
    main()

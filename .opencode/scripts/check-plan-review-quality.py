#!/usr/bin/env python3
"""
PLAN_REVIEW 质量检查脚本（Python 版）
检查 project.config.md 和规划文件是否满足 PLAN_REVIEW 质量要求。

用法：
    python .opencode/scripts/check-plan-review-quality.py --project-path "..."
"""

import argparse
import json
import os
import re
import sys

# Windows PowerShell GBK编码修复：强制stdout用UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


def read_text(path: str) -> str:
    if not os.path.exists(path):
        return ""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, 'r', encoding='gbk', errors='replace') as f:
            return f.read()


def read_all_markdown(root: str) -> str:
    if not os.path.isdir(root):
        return ""
    parts = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in ('.opencode', '.task', '__pycache__', 'node_modules')]
        for f in files:
            if f.endswith('.md') and '模板' not in f:
                parts.append(read_text(os.path.join(dirpath, f)))
    return '\n---FILE---\n'.join(parts)


PLACEHOLDER_VALUES = {'待补充', '待确认', '待填充', '占位', '[...]', '[项目特定]', '', 'tbd', 'todo', '略', '同上', '待前置准备填充'}


def _is_placeholder(val: str) -> bool:
    """判断单个值是否为占位（含内联数组全占位的情况）"""
    if not val:
        return True
    v = val.strip().strip('`').strip('"').strip("'")
    if not v or v.lower() in PLACEHOLDER_VALUES:
        return True
    # 内联数组 ["待补充"] / [待补充]
    if v.startswith('[') and v.endswith(']'):
        inner = v[1:-1].strip()
        if not inner:
            return True
        items = [x.strip().strip('"').strip("'") for x in inner.split(',') if x.strip()]
        if not items:
            return True
        if all(it.lower() in PLACEHOLDER_VALUES for it in items):
            return True
    return False


def has_nonempty_yaml_value(content: str, key: str) -> bool:
    """非空检查，但排除占位值（防占位欺骗）。占位如 '待补充/TBD/[]/""/["待补充"]' 均视为空。"""
    if not content:
        return False
    escaped = re.escape(key)
    # 显式空 / 空数组 / 空字符串
    if re.search(rf'(?m)^\s*{escaped}\s*:\s*\[\s*\]\s*(#.*)?$', content):
        return False
    if re.search(rf'(?m)^\s*{escaped}\s*:\s*""\s*(#.*)?$', content):
        return False
    # 单行标量/内联数组值：必须非空且非占位（含内联数组全占位）
    m = re.search(rf'(?m)^\s*{escaped}\s*:\s*(.+)$', content)
    if m:
        val = m.group(1).strip()
        if not _is_placeholder(val):
            return True
    # 块状（多行列表）
    m = re.search(rf'(?m)^\s*{escaped}\s*:\s*$', content)
    if m:
        start = m.start()
        tail = content[start:]
        lines = tail.split('\n')
        for i in range(1, min(len(lines), 8)):
            if re.match(r'^\s{2,}\S+', lines[i]):
                item = re.sub(r'^\s*-\s*', '', lines[i]).strip()
                if not _is_placeholder(item):
                    return True
            if re.match(r'^\S', lines[i]):
                return False
    return False


def has_objectives_four_queries(content: str) -> bool:
    """objectives 四问非空非占位：problem/audience/deliverables/scenarios"""
    return all(has_nonempty_yaml_value(content, k) for k in ('problem', 'audience', 'deliverables', 'scenarios'))


def has_heading_count(content: str, minimum: int) -> bool:
    if not content:
        return False
    return len(re.findall(r'(?m)^##\s+', content)) >= minimum


def find_first_file(root: str, pattern: str) -> str:
    if not os.path.isdir(root):
        return None
    for dirpath, dirs, files in os.walk(root):
        for f in files:
            if Path(f).match(pattern):
                return os.path.join(dirpath, f)
    return None


from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='PLAN_REVIEW 质量检查')
    parser.add_argument('--project-path', required=True, help='项目根目录路径')
    args = parser.parse_args()

    root = os.path.abspath(args.project_path)
    config_path = os.path.join(root, "project.config.md")
    queue_path = find_first_file(root, "task_queue.md")

    project_config = read_text(config_path)
    queue = read_text(queue_path) if queue_path else ""
    all_markdown = read_all_markdown(root)

    checks = {
        "has_project_config": os.path.exists(config_path),
        "has_run_state": os.path.exists(os.path.join(root, "run-state.md")),
        "has_markdown_assets": bool(all_markdown.strip()),
        "has_task_queue": bool(queue.strip()),
        "project_config_has_required_heading_count": has_heading_count(project_config, 8),
        "project_config_has_objectives_block": bool(re.search(r'(?m)^\s*objectives\s*:', project_config)),
        "project_config_has_process_block": bool(re.search(r'(?m)^\s*process\s*:', project_config))
                                         or bool(re.search(r'(?mi)^\s*##\s*调研工艺', project_config)),
        "project_config_objectives_problem_nonempty": has_nonempty_yaml_value(project_config, "problem"),
        "project_config_objectives_audience_nonempty": has_nonempty_yaml_value(project_config, "audience"),
        "project_config_objectives_deliverables_nonempty": has_nonempty_yaml_value(project_config, "deliverables"),
        "project_config_objectives_scenarios_nonempty": has_nonempty_yaml_value(project_config, "scenarios"),
        "project_config_has_execution": bool(re.search(r'execution\s*:', project_config))
                                        or bool(re.search(r'execution\s*:', read_text(os.path.join(root, "run-state.md")) if os.path.exists(os.path.join(root, "run-state.md")) else "")),
        "project_config_has_search_params": bool(re.search(r'breadth\s*:|depth\s*:|threshold\s*:|focus_keywords\s*:|sources\s*:', project_config))
                                             or bool(re.search(r'breadth\s*:|depth\s*:|threshold\s*:|focus_keywords\s*:|sources\s*:', read_text(os.path.join(root, "run-state.md")) if os.path.exists(os.path.join(root, "run-state.md")) else "")),
        "project_config_has_strategy_mapping_key": bool(re.search(r'(?m)^\s*strategy_mapping\s*:', project_config)),
        "project_config_has_research_axis": 'research_axis' in project_config,
        "project_config_has_type_notes": 'type_notes' in project_config,
        "project_config_has_knowledge_schema": bool(re.search(r'(?m)^\s*knowledge_schema\s*:', project_config)),
        "project_config_has_id_registry": bool(re.search(r'(?m)^\s*id_registry\s*:', project_config)),
        "knowledge_schema_has_purpose": has_nonempty_yaml_value(project_config, "purpose"),
        "knowledge_schema_has_research_type": has_nonempty_yaml_value(project_config, "research_type"),
        "knowledge_schema_has_strategy_tags": has_nonempty_yaml_value(project_config, "strategy_tags"),
        "knowledge_schema_has_node_types": has_nonempty_yaml_value(project_config, "node_types"),
        "knowledge_schema_has_edge_types": has_nonempty_yaml_value(project_config, "edge_types"),
        "knowledge_schema_has_core_questions": has_nonempty_yaml_value(project_config, "core_questions"),
        "knowledge_schema_has_conversation_goals": has_nonempty_yaml_value(project_config, "conversation_goals"),
        "knowledge_schema_has_reporting_goals": has_nonempty_yaml_value(project_config, "reporting_goals"),
        "knowledge_schema_has_comparison_anchors": has_nonempty_yaml_value(project_config, "comparison_anchors"),
        "plan_has_strategy_mapping_like_table": bool(
            'types/' in all_markdown and 'scenarios/' in all_markdown and
            'sources/' in all_markdown and '|' in all_markdown
        ),
        "queue_has_discover": bool(re.search(r'\|\s*D\d+\s*\|\s*DISCOVER\s*\|', queue)),
        "queue_discover_not_generic": bool(re.search(
            r'category|metric|parameter|review|community|official|benchmark|methodology|architecture|api|agent',
            queue, re.IGNORECASE
        )),
        "knowledge_design_has_table": '|' in all_markdown,
        "knowledge_design_has_node_like_terms": bool(re.search(
            r'node|category|metric|methodology|architecture|evidence', all_markdown, re.IGNORECASE
        )),
        "knowledge_design_has_edge_like_terms": bool(re.search(
            r'edge|has_metric|maps_to|validated_by|supports|requires|implements', all_markdown, re.IGNORECASE
        )),
        "knowledge_design_has_question_index": '?' in all_markdown,
        "knowledge_design_has_completion_markers": bool(re.search(
            r'\[ \]|completion|saturation|graph\.nodes|question_index|coverage_map', all_markdown
        )),
    }

    blocking_reasons = [k for k, v in checks.items() if not v]
    quality_valid = len(blocking_reasons) == 0

    result = {
        "project_path": root,
        "plan_review_quality_valid": quality_valid,
        "checks": checks,
        "blocking_reasons": blocking_reasons,
        "recommendation": "PLAN_REVIEW_QUALITY_OK" if quality_valid else "PLAN_REVIEW_NEEDS_REVISION",
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

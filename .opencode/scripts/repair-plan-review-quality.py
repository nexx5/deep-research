#!/usr/bin/env python3
"""
PLAN_REVIEW 质量修复脚本（Python 版）
修复 project.config.md 的缺失段和字段。通用版本，不硬编码项目特定值。

用法：
    python .opencode/scripts/repair-plan-review-quality.py --project-path "..."
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

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


def write_text(path: str, content: str):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)


def find_first_file(root: str, pattern: str) -> str:
    if not os.path.isdir(root):
        return None
    for dirpath, dirs, files in os.walk(root):
        for f in files:
            if Path(f).match(pattern):
                return os.path.join(dirpath, f)
    return None


def get_scalar(content: str, name: str, default: str = "") -> str:
    patterns = [
        rf'(?m)^\s*-\s*\*\*{re.escape(name)}[：:]\*\*\s*`?([^`\r\n]+)`?\s*$',
        rf'(?m)^\s*{re.escape(name)}\s*[:：]\s*`?([^`\r\n]+)`?\s*$',
    ]
    for pattern in patterns:
        m = re.search(pattern, content)
        if m:
            return m.group(1).strip()
    return default


def quote_list(items: list) -> str:
    if not items:
        return "[]"
    return "[" + ", ".join(f'"{item}"' for item in items if item) + "]"


def add_yaml_list(lines: list, indent: str, items: list):
    count = 0
    for item in items:
        if item and str(item).strip():
            lines.append(f'{indent}- "{str(item).replace(chr(34), chr(92)+chr(34))}"')
            count += 1
    if count == 0:
        lines.append(f"{indent}[]")


def main():
    parser = argparse.ArgumentParser(description='PLAN_REVIEW 质量修复')
    parser.add_argument('--project-path', required=True, help='项目根目录路径')
    args = parser.parse_args()

    root = os.path.abspath(args.project_path)
    config_path = os.path.join(root, "project.config.md")

    if not os.path.exists(config_path):
        print(json.dumps({"error": "project.config.md not found", "project_path": root}, ensure_ascii=False))
        sys.exit(1)

    content = read_text(config_path)

    # 读取知识包 JSON（如果存在）获取元信息
    pack_path = find_first_file(root, "knowledge-pack*.json")
    kp = None
    if pack_path:
        try:
            with open(pack_path, 'r', encoding='utf-8') as f:
                kp = json.load(f)
        except (json.JSONDecodeError, UnicodeDecodeError):
            kp = None

    # 提取标量
    research_type = get_scalar(content, "research_type", "")
    research_subtype = get_scalar(content, "research_subtype", "")
    strategy_tags_raw = get_scalar(content, "strategy_tags", "[]")

    # 从知识包补充缺失值
    if not research_type and kp:
        research_type = kp.get("metadata", {}).get("research_type", "")
    if not research_subtype and kp:
        research_subtype = kp.get("metadata", {}).get("research_subtype", "")
    if (strategy_tags_raw == "[]" or not strategy_tags_raw) and kp:
        tags = kp.get("metadata", {}).get("strategy_tags", [])
        strategy_tags_raw = quote_list(tags) if tags else "[]"

    # 修复 research_axis 和 type_notes（如果缺失）
    if 'research_axis' not in content:
        axis_line = f'- **research_axis：** {{ primary: "未分类", secondary: [] }}'
        type_notes_line = f'- **type_notes：** "待补充"'
        m = re.search(r'(?m)^\s*-\s*\*\*strategy_tags[：:]\*\.*$', content)
        if m:
            content = content[:m.end()] + '\n' + axis_line + '\n' + type_notes_line + content[m.end():]

    # 修复 strategy_mapping 段（如果缺失）—— 真实信息不可得时填明确"⚠缺失需补"，不再用"待补充"占位骗过验收
    if not re.search(r'(?m)^\s*strategy_mapping\s*:', content):
        strategy_block = f"""---
## 策略映射

```yaml
strategy_mapping:
  classification:
    research_type: "{research_type or '通用'}"
    research_subtype: "{research_subtype or '通用'}"
    strategy_tags: {strategy_tags_raw or '[]'}
    research_axis:
      primary: "⚠缺失需补"
      secondary: []
    type_notes: "⚠缺失需补"
    confidence: 0.5
  rows:
    - strategy_file: "types/{research_type or '通用'}.md"
      field_model: ["⚠缺失需补"]
      collection_direction: "⚠缺失需补"
      evidence_questions: "⚠缺失需补"
      expected_outputs: "raw-S*.md → 采集记录-S*.md → 分析-A*.md → knowledge-pack"
      strategy_gap: "⚠缺失需补"
  completeness_checks:
    has_type_row: false
    has_scenario_row: false
    source_rows_cover_all_tags: false
    no_empty_cells: false
    field_model_expanded: false
    discover_ready: false
```"""
        # 插入到"关键链接"段之前
        key_heading = "## 关键链接"
        idx = content.find(key_heading)
        if idx >= 0:
            content = content[:idx] + strategy_block + "\n\n" + content[idx:]
        else:
            content += "\n" + strategy_block

    # 修复 knowledge_schema 段（如果缺失或不完整）
    if not re.search(r'(?m)^\s*knowledge_schema\s*:', content):
        schema_lines = [
            "## 知识包 Schema",
            "",
            "```yaml",
            "knowledge_schema:",
            "  purpose:",
        ]
        add_yaml_list(schema_lines, "    ", ["reporting", "analysis", "comparison"])
        schema_lines.append(f'  research_type: "{research_type or "通用"}"')
        schema_lines.append(f'  research_subtype: "{research_subtype or "通用"}"')
        schema_lines.append(f"  strategy_tags: {strategy_tags_raw or '[]'}")
        schema_lines.append("  domain_schema:")
        schema_lines.append("    node_types:")
        add_yaml_list(schema_lines, "      ", ["⚠缺失需项目管理员补真实节点类型"])
        schema_lines.append("    edge_types:")
        add_yaml_list(schema_lines, "      ", ["⚠缺失需补真实边类型"])
        schema_lines.append("    required_chains:")
        add_yaml_list(schema_lines, "      ", ["⚠缺失需补真实链路"])
        schema_lines.append("  core_questions:")   # 验收硬门，repair 填占位会被验收拒
        add_yaml_list(schema_lines, "    ", ["⚠缺失需补真实核心问题≥3"])
        schema_lines.append("  conversation_goals:")
        add_yaml_list(schema_lines, "    ", ["⚠缺失需补真实对话能力≥2"])
        schema_lines.append("  reporting_goals:")
        add_yaml_list(schema_lines, "    ", ["⚠缺失需补真实报告类型≥1"])
        schema_lines.append("  comparison_anchors:")
        add_yaml_list(schema_lines, "    ", ["⚠缺失需补真实对比锚点≥1"])
        schema_lines.append("```")

        schema_block = "\n".join(schema_lines)
        key_heading = "## 关键链接"
        idx = content.find(key_heading)
        if idx >= 0:
            content = content[:idx] + schema_block + "\n\n---\n\n" + content[idx:]
        else:
            content += "\n---\n\n" + schema_block

    # 修复 id_registry 段（如果缺失）
    if not re.search(r'(?m)^\s*id_registry\s*:', content):
        id_block = """## ID 注册表

```yaml
id_registry:
  sources: {}
  analyses: {}
  comparisons: {}
```"""
        content += "\n---\n\n" + id_block

    write_text(config_path, content)

    result = {
        "project_path": root,
        "repaired": True,
        "project_config": config_path,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

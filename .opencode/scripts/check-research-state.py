#!/usr/bin/env python3
"""
项目状态检查脚本（Python 版）
从 .ps1 迁移，修复中文编码问题，新增 CONSISTENCY_CHECK 阶段和知识一致性检查。

用法：
    python .opencode/scripts/check-research-state.py --project-path "..."
    python .opencode/scripts/check-research-state.py --project-path "..." --strict-knowledge-pack

输出：JSON 格式的项目状态，供 orchestrator 路由决策。
"""

import argparse
import json
import os
import re
import sqlite3
import sys

# Windows PowerShell GBK编码修复：强制stdout用UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
from pathlib import Path


def find_files(project_path: str, patterns: list) -> list:
    """在项目目录内按文件名模式查找文件，排除模板和 .opencode/.task"""
    results = []
    for root, dirs, files in os.walk(project_path):
        dirs[:] = [d for d in dirs if d not in ('.opencode', '.task', '__pycache__', 'node_modules')]
        for f in files:
            if '模板' in f:
                continue
            for pattern in patterns:
                if Path(f).match(pattern):
                    results.append(os.path.join(root, f))
                    break
    return results


def test_any_path(project_path: str, relative_paths: list) -> bool:
    for rel in relative_paths:
        if os.path.exists(os.path.join(project_path, rel)):
            return True
    return False


def get_config_scalar(project_path: str, name: str, default: str) -> str:
    """从 project.config.md 提取标量字段"""
    config_path = os.path.join(project_path, "project.config.md")
    if not os.path.exists(config_path):
        return default
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(config_path, 'r', encoding='gbk', errors='replace') as f:
            content = f.read()

    patterns = [
        rf'(?m)^\s*-\s*\*\*{re.escape(name)}[：:]\*\*\s*`?([^`\r\n]+)`?\s*$',
        rf'(?m)^\s*{re.escape(name)}\s*[:：]\s*`?([^`\r\n]+)`?\s*$',
    ]
    for pattern in patterns:
        m = re.search(pattern, content)
        if m:
            return m.group(1).strip()
    return default


def get_task_queue_state(project_path: str) -> dict:
    """解析 task_queue.md 的任务状态"""
    queue_files = find_files(project_path, ["task_queue.md"])
    pending = {"DISCOVER": 0, "EXTRACT": 0, "SYNTHESIZE": 0, "KNOWLEDGE_PACK": 0}
    running = 0
    completed = 0
    total = 0

    for qfile in queue_files:
        try:
            with open(qfile, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(qfile, 'r', encoding='gbk', errors='replace') as f:
                content = f.read()

        for line in content.split('\n'):
            if not line.strip().startswith('|'):
                continue
            if re.match(r'\|\s*-+\s*\|', line):
                continue
            if re.search(r'\|\s*ID\s*\|', line, re.IGNORECASE):
                continue
            cells = [c.strip() for c in line.split('|')]
            if len(cells) < 7:
                continue
            task_id = cells[1]
            task_type = cells[2]
            status = cells[6] if len(cells) > 6 else ""
            if not task_id or not task_type:
                continue
            if not re.match(r'^[A-Z]+\d+', task_id):
                continue
            total += 1
            if 'pending' in status.lower():
                if task_type in pending:
                    pending[task_type] += 1
            elif 'in_progress' in status.lower() or 'running' in status.lower():
                running += 1
            elif 'completed' in status.lower():
                completed += 1

    next_stage = None
    for stage in ["DISCOVER", "EXTRACT", "SYNTHESIZE", "KNOWLEDGE_PACK"]:
        if pending[stage] > 0:
            next_stage = stage
            break

    return {
        "total": total,
        "pending_discover": pending["DISCOVER"],
        "pending_extract": pending["EXTRACT"],
        "pending_synthesize": pending["SYNTHESIZE"],
        "pending_knowledge_pack": pending["KNOWLEDGE_PACK"],
        "pending_total": sum(pending.values()),
        "running": running,
        "completed": completed,
        "next_pending_stage": next_stage,
    }


def get_knowledge_quality(knowledge_files: list) -> dict:
    """检查知识包 JSON 质量"""
    warnings = []
    result = {
        "schema_valid": False,
        "incremental_valid": False,
        "has_project_schema": False,
        "graph_node_count": 0,
        "graph_edge_count": 0,
        "question_count": 0,
        "deep_question_count": 0,
        "has_application_support": False,
        "inspected_file": None,
        "warnings": warnings,
    }

    # 找最大的非空 JSON
    candidates = [f for f in knowledge_files if os.path.getsize(f) > 20]
    if not candidates:
        warnings.append("knowledge pack is missing or empty")
        return result

    candidates.sort(key=lambda f: os.path.getmtime(f), reverse=True)
    kp_file = candidates[0]
    result["inspected_file"] = kp_file

    try:
        with open(kp_file, 'r', encoding='utf-8') as f:
            kp = json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        warnings.append(f"knowledge pack json parse failed: {e}")
        return result

    # project_knowledge_schema
    project_schema = kp.get("project_knowledge_schema", {})
    has_project_schema = bool(project_schema and isinstance(project_schema, dict) and len(project_schema) > 0)
    if not has_project_schema:
        warnings.append("knowledge pack missing project_knowledge_schema")

    # graph
    graph = kp.get("graph", {})
    if not graph:
        warnings.append("knowledge pack missing graph")
    else:
        nodes = graph.get("nodes", [])
        edges = graph.get("edges", [])
        result["graph_node_count"] = len(nodes) if isinstance(nodes, list) else 0
        result["graph_edge_count"] = len(edges) if isinstance(edges, list) else 0
        if result["graph_node_count"] == 0:
            warnings.append("knowledge pack graph.nodes is empty")
        if result["graph_edge_count"] == 0:
            warnings.append("knowledge pack graph.edges is empty (expected after SYNTHESIZE)")

    # questions
    q_index = kp.get("question_index", {})
    if not q_index:
        warnings.append("knowledge pack missing question_index")
    else:
        result["question_count"] = len(q_index.get("can_answer", [])) + len(q_index.get("cannot_answer_yet", []))
        result["deep_question_count"] = len(q_index.get("deep_questions", []))
        if result["question_count"] + result["deep_question_count"] == 0:
            warnings.append("knowledge pack question_index is empty")

    # application_support
    app_support = kp.get("application_support", {})
    result["has_application_support"] = bool(app_support and isinstance(app_support, dict) and len(app_support) > 0)
    if not result["has_application_support"]:
        warnings.append("knowledge pack missing application_support")

    # validation
    result["schema_valid"] = (
        has_project_schema and
        result["graph_node_count"] > 0 and
        result["graph_edge_count"] > 0 and
        result["question_count"] + result["deep_question_count"] > 0 and
        result["has_application_support"]
    )
    result["incremental_valid"] = has_project_schema and result["graph_node_count"] > 0

    return result


def get_sqlite_consistency(project_path: str) -> dict:
    """检查 SQLite 索引层一致性（新增）"""
    result = {
        "has_index": False,
        "active_claims": 0,
        "contested_claims": 0,
        "stale_comparisons": 0,
        "last_sync": None,
        "consistency_ok": False,
        "legacy_tables_missing": False,  # 新协议无 comparisons/sync_log 表，区分清楚
    }

    for candidate in ['knowledge-pack/index', '2-执行/03-知识提炼', '03-知识提炼']:
        for db_name in ['knowledge.db', 'knowledge-index.db']:
            db_path = os.path.join(project_path, candidate, db_name)
            if os.path.exists(db_path):
                result["has_index"] = True
                try:
                    conn = sqlite3.connect(db_path)
                    result["active_claims"] = conn.execute(
                        "SELECT COUNT(*) FROM claims WHERE status='active'"
                    ).fetchone()[0]
                    result["contested_claims"] = conn.execute(
                        "SELECT COUNT(*) FROM claims WHERE status='contested'"
                    ).fetchone()[0]
                    # comparisons / sync_log 表仅旧协议存在；新协议(zhishibao)无此表
                    cur = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('comparisons','sync_log')")
                    existing_tables = {row[0] for row in cur.fetchall()}
                    if 'comparisons' in existing_tables:
                        result["stale_comparisons"] = conn.execute(
                            "SELECT COUNT(*) FROM comparisons WHERE status='stale'"
                        ).fetchone()[0]
                    else:
                        result["legacy_tables_missing"] = True
                    if 'sync_log' in existing_tables:
                        sync_row = conn.execute(
                            "SELECT timestamp FROM sync_log ORDER BY id DESC LIMIT 1"
                        ).fetchone()
                        if sync_row:
                            result["last_sync"] = sync_row[0]
                    else:
                        result["legacy_tables_missing"] = True
                    conn.close()
                except sqlite3.Error:
                    pass
                break
        if result["has_index"]:
            break

    # 一致性检查：有索引 + 无 contested
    # 新协议无 comparisons 表时，stale_comparisons 维持 0（不存在即无 stale），不视为不一致
    result["consistency_ok"] = (
        result["has_index"] and
        result["contested_claims"] == 0 and
        result["stale_comparisons"] == 0
    )

    return result


def check_new_protocol(project_path):
    """检查新协议（knowledge-pack/目录）项目状态"""
    pack_path = os.path.join(project_path, "knowledge-pack")
    if not os.path.isdir(pack_path):
        return None  # 不是新协议项目

    result = {
        "protocol": "v2",
        "project_valid": True,
        "project_path": project_path,
        "has_knowledge_pack": True,
    }

    # 检查batch-state.json
    state_path = os.path.join(pack_path, "batch-state.json")
    if os.path.exists(state_path):
        with open(state_path, 'r', encoding='utf-8') as f:
            state = json.load(f)
        result["batch_state"] = state
        result["batch_id"] = state.get("batch_id", 0)
        result["phase"] = state.get("phase", "unknown")
    else:
        result["batch_state"] = None
        result["batch_id"] = 0
        result["phase"] = "init"

    # 统计JSONL
    def count_jsonl(name):
        path = os.path.join(pack_path, name)
        if not os.path.exists(path):
            return 0
        with open(path, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if line.strip())

    result["claims_count"] = count_jsonl("claims.jsonl")
    result["debates_count"] = count_jsonl("debates.jsonl")
    result["schools_count"] = count_jsonl("schools.jsonl")
    result["leads_count"] = count_jsonl("source-leads.jsonl")

    # 检查evidence文件
    evidence_path = os.path.join(pack_path, "evidence")
    if os.path.isdir(evidence_path):
        result["raw_count"] = len([f for f in os.listdir(evidence_path) if f.startswith("raw-S")])
        result["extract_count"] = len([f for f in os.listdir(evidence_path) if f.startswith("采录-S")])
        result["analysis_count"] = len([f for f in os.listdir(evidence_path) if f.startswith("分析-A")])
    else:
        result["raw_count"] = 0
        result["extract_count"] = 0
        result["analysis_count"] = 0

    # 检查索引
    db_path = os.path.join(pack_path, "index", "knowledge.db")
    result["has_sqlite_index"] = os.path.exists(db_path)

    qmd_path = os.path.join(pack_path, "index", "qmd-index")
    result["has_qmd_index"] = os.path.isdir(qmd_path)

    # 新协议一致性检查（P0-A 仲裁闭环保卫）：contested 与未仲裁 opposing
    result["contested_claims"] = 0
    result["unarbitrated_opposing_pairs"] = 0
    result["knowledge_consistency_ok"] = True
    if db_path and os.path.exists(db_path):
        import sqlite3 as _s
        try:
            _conn = _s.connect(db_path)
            _cols = {row[1] for row in _conn.execute("PRAGMA table_info(claims)").fetchall()}
            result["contested_claims"] = _conn.execute(
                "SELECT COUNT(*) FROM claims WHERE status='contested'"
            ).fetchone()[0]
            # 未仲裁 opposing 对：claims.opposing 非空但无 arbitration 记录指向该 target
            if 'opposing' in _cols:
                # 排除双重编码空数组（'\"[]\"'）：历史数据中 opposing 存的是 JSON 编码的空数组字符串，
                # SQL 层 != '[]' 无法排除，须在此一并排除；其余异常形式由 Python 层 isinstance 兜底
                _opp_rows = _conn.execute(
                    "SELECT id, opposing, arbitration FROM claims "
                    "WHERE opposing IS NOT NULL AND opposing != '' AND opposing != '[]' "
                    "AND opposing != '\"[]\"' AND opposing != '\"\"'"
                ).fetchall()
                import json as _j
                pending = set()
                for _rid, _opp, _arb in _opp_rows:
                    try:
                        _opp_list = _j.loads(_opp) if _opp else []
                    except Exception:
                        _opp_list = []
                    # 防双重编码兜底：'\"[]\"' 解析后是 str '[]' 而非 list，按空处理，避免字符级假 target
                    if not isinstance(_opp_list, list):
                        _opp_list = []
                    _decided_targets = set()
                    if _arb:
                        try:
                            for _a in (_j.loads(_arb) if isinstance(_arb, str) else _arb):
                                if isinstance(_a, dict):
                                    _decided_targets.add(_a.get("target"))
                        except Exception:
                            pass
                    for _t in _opp_list:
                        if _t not in _decided_targets:
                            pending.add(tuple(sorted([_rid, _t])))
                result["unarbitrated_opposing_pairs"] = len(pending)
            result["knowledge_consistency_ok"] = (
                result["contested_claims"] == 0 and result["unarbitrated_opposing_pairs"] == 0
            )
            _conn.close()
        except _s.Error:
            pass

    # 检查线索池
    leads_path = os.path.join(pack_path, "source-leads.jsonl")
    p0_pending = 0
    p1_pending = 0
    if os.path.exists(leads_path):
        with open(leads_path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    lead = json.loads(line)
                    if lead.get("status") == "pending":
                        if lead.get("priority") == "P0":
                            p0_pending += 1
                        elif lead.get("priority") == "P1":
                            p1_pending += 1
                except json.JSONDecodeError:
                    continue

    result["leads_p0_pending"] = p0_pending
    result["leads_p1_pending"] = p1_pending

    # 确定next_stage
    if result["raw_count"] == 0:
        result["next_stage"] = "DISCOVER"
    elif result["extract_count"] < result["raw_count"]:
        result["next_stage"] = "EXTRACT"
    elif result["claims_count"] == 0:
        result["next_stage"] = "SYNTHESIZE"
    elif not result["knowledge_consistency_ok"]:
        # 有未仲裁 opposing 或 contested → 需知识管理员处理
        result["next_stage"] = "CONSISTENCY_CHECK"
    elif p0_pending + p1_pending > 0:
        result["next_stage"] = "DISCOVER"
    elif result["debates_count"] > 0:
        # 有debate需要检查unresolved
        result["next_stage"] = "KNOWLEDGE_PACK"
    else:
        result["next_stage"] = "CLOSED_LOOP"

    result["plan_status"] = "approved"  # 新协议默认approved（由项目管理员设置）
    result["report_allowed"] = (
        result["raw_count"] >= 3 and
        result["extract_count"] >= 3 and
        result["claims_count"] >= 1 and
        p0_pending + p1_pending == 0 and
        result["knowledge_consistency_ok"]  # 含 contested=0 且 未仲裁 opposing=0
    )

    return result


def main():
    parser = argparse.ArgumentParser(description='项目状态检查')
    parser.add_argument('--project-path', required=True, help='项目根目录路径')
    parser.add_argument('--strict-knowledge-pack', action='store_true', help='严格知识包检查')
    args = parser.parse_args()

    project_path = os.path.abspath(args.project_path)

    if not os.path.exists(project_path):
        result = {
            "project_valid": False,
            "project_path": project_path,
            "plan_status": "missing",
            "next_stage": "INVALID_PROJECT",
            "report_allowed": False,
            "blocking_reasons": ["project path does not exist"],
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0)

    # 新协议检测：如果有knowledge-pack/目录，走新协议检查
    new_proto_result = check_new_protocol(project_path)
    if new_proto_result is not None:
        print(json.dumps(new_proto_result, ensure_ascii=False, indent=2))
        sys.exit(0)

    # 检查项目结构
    has_project_config = os.path.exists(os.path.join(project_path, "project.config.md"))
    has_planning = test_any_path(project_path, ["0-规划", "1-规划", "1-planning"])
    has_task_queue = test_any_path(project_path, [
        "0-规划/task_queue.md", "1-规划/task_queue.md",
        "1-planning/task_queue.md", "task_queue.md"
    ])
    has_collect_dir = test_any_path(project_path, [
        "01-采集记录", "2-执行/01-采集记录", "2-execution/01-collection"
    ])
    has_analysis_dir = test_any_path(project_path, [
        "02-分析提取", "02-合成提炼", "2-执行/02-分析提取", "2-execution/02-analysis"
    ])
    has_knowledge_dir = test_any_path(project_path, [
        "03-知识提炼", "2-执行/03-知识提炼", "2-execution/03-knowledge"
    ])
    has_check_dir = test_any_path(project_path, [
        "04-检查", "2-执行/04-检查", "2-执行/05-过程产物",
        "2-execution/04-check", "2-execution/05-process"
    ])

    # 文件计数
    raw_files = find_files(project_path, ["raw-S*.md"])
    extract_files = find_files(project_path, ["采集记录-S*.md", "采录-S*.md"])
    analysis_files = find_files(project_path, ["分析-A*.md"])
    comparison_files = find_files(project_path, ["对比-C*.md", "链-C*.md"])
    knowledge_files = find_files(project_path, ["knowledge-pack*.json"])
    non_empty_knowledge = any(os.path.getsize(f) > 20 for f in knowledge_files)

    knowledge_quality = get_knowledge_quality(knowledge_files)
    task_queue_state = get_task_queue_state(project_path)
    sqlite_consistency = get_sqlite_consistency(project_path)

    plan_status = get_config_scalar(project_path, "plan_status", "missing")
    execution_mode = get_config_scalar(project_path, "execution_mode", "continuous")
    execution_status = get_config_scalar(project_path, "execution_status", "missing")
    research_type = get_config_scalar(project_path, "research_type", "missing")

    has_research_evidence = (
        len(raw_files) + len(extract_files) + len(analysis_files) +
        len(comparison_files) + len(knowledge_files)
    ) > 0

    # 阻塞原因
    blocking = []
    if not has_project_config:
        blocking.append("missing project.config.md")
    if not has_planning:
        blocking.append("missing planning directory")
    if not has_task_queue:
        blocking.append("missing task_queue.md")
    if not has_collect_dir:
        blocking.append("missing collection directory")
    if not has_analysis_dir:
        blocking.append("missing analysis directory")
    if not has_knowledge_dir:
        blocking.append("missing knowledge directory")
    if not has_check_dir:
        blocking.append("missing check/process directory")

    project_valid = len(blocking) == 0
    raw_count = len(raw_files)
    extract_count = len(extract_files)
    analysis_count = len(analysis_files)
    comparison_count = len(comparison_files)
    knowledge_count = len(knowledge_files)

    # 报告闸门
    base_report_allowed = (
        raw_count >= 3 and
        extract_count >= 3 and
        comparison_count >= 1 and
        non_empty_knowledge and
        knowledge_quality["schema_valid"] and
        task_queue_state["pending_total"] == 0
    )

    # 新增：知识一致性检查（有 SQLite 索引时才检查）
    consistency_blocking = []
    if sqlite_consistency["has_index"]:
        if sqlite_consistency["contested_claims"] > 0:
            consistency_blocking.append(f"{sqlite_consistency['contested_claims']} contested claims need arbitration")
        if sqlite_consistency["stale_comparisons"] > 0:
            consistency_blocking.append(f"{sqlite_consistency['stale_comparisons']} stale comparisons need update")

    report_allowed = base_report_allowed and len(consistency_blocking) == 0

    # next_stage 判定
    next_stage = "INVALID_PROJECT"
    approval_required = False

    if project_valid:
        if plan_status != "approved":
            next_stage = "PLAN_REVIEW"
            approval_required = True
        elif task_queue_state["next_pending_stage"]:
            next_stage = task_queue_state["next_pending_stage"]
        elif raw_count == 0:
            next_stage = "DISCOVER"
        elif extract_count < raw_count:
            next_stage = "EXTRACT"
        elif analysis_count > 0 and comparison_count == 0:
            next_stage = "SYNTHESIZE"
        elif extract_count >= 5 and comparison_count == 0:
            next_stage = "SYNTHESIZE"
        elif not non_empty_knowledge:
            next_stage = "KNOWLEDGE_PACK"
        elif not knowledge_quality["schema_valid"] and not knowledge_quality["incremental_valid"]:
            next_stage = "KNOWLEDGE_PACK"
        elif sqlite_consistency["has_index"] and not sqlite_consistency["consistency_ok"]:
            # 新增：有索引但不一致 → CONSISTENCY_CHECK
            next_stage = "CONSISTENCY_CHECK"
        elif report_allowed:
            next_stage = "REPORT_ALLOWED"
        else:
            next_stage = "CLOSED_LOOP"

    # 报告阻塞原因
    report_blocking = []
    if raw_count < 3:
        report_blocking.append("raw count is less than 3")
    if extract_count < 3:
        report_blocking.append("extract count is less than 3")
    if analysis_count < 1:
        report_blocking.append("analysis count is less than 1")
    if comparison_count < 1:
        report_blocking.append("comparison/chain count is less than 1")
    if not non_empty_knowledge:
        report_blocking.append("knowledge pack is missing or empty")
    if not knowledge_quality["schema_valid"]:
        report_blocking.append("knowledge pack schema quality check failed")
    if task_queue_state["pending_total"] > 0:
        report_blocking.append("task_queue still has pending executable tasks")
    report_blocking.extend(consistency_blocking)

    # 输出
    result = {
        "project_valid": project_valid,
        "project_path": project_path,
        "strict_knowledge_pack": args.strict_knowledge_pack,
        "has_project_config": has_project_config,
        "has_planning": has_planning,
        "has_task_queue": has_task_queue,
        "has_collect_dir": has_collect_dir,
        "has_analysis_dir": has_analysis_dir,
        "has_knowledge_dir": has_knowledge_dir,
        "has_check_dir": has_check_dir,
        "raw_count": raw_count,
        "extract_count": extract_count,
        "analysis_count": analysis_count,
        "comparison_count": comparison_count,
        "knowledge_pack_count": knowledge_count,
        "knowledge_pack_nonempty": non_empty_knowledge,
        "knowledge_pack_schema_valid": knowledge_quality["schema_valid"],
        "knowledge_pack_incremental_valid": knowledge_quality["incremental_valid"],
        "knowledge_pack_has_project_schema": knowledge_quality["has_project_schema"],
        "knowledge_graph_node_count": knowledge_quality["graph_node_count"],
        "knowledge_graph_edge_count": knowledge_quality["graph_edge_count"],
        "knowledge_question_count": knowledge_quality["question_count"],
        "knowledge_deep_question_count": knowledge_quality["deep_question_count"],
        "knowledge_application_support": knowledge_quality["has_application_support"],
        "knowledge_pack_inspected_file": knowledge_quality["inspected_file"],
        "knowledge_quality_warnings": knowledge_quality["warnings"],
        # 新增：SQLite 索引层状态
        "has_knowledge_index": sqlite_consistency["has_index"],
        "active_claims": sqlite_consistency["active_claims"],
        "contested_claims": sqlite_consistency["contested_claims"],
        "stale_comparisons": sqlite_consistency["stale_comparisons"],
        "last_sync": sqlite_consistency["last_sync"],
        "knowledge_consistency_ok": sqlite_consistency["consistency_ok"],
        # 原有字段
        "plan_status": plan_status,
        "approval_required": approval_required,
        "execution_mode": execution_mode,
        "execution_status": execution_status,
        "research_type": research_type,
        "has_research_evidence": has_research_evidence,
        "task_queue_total": task_queue_state["total"],
        "task_queue_pending_total": task_queue_state["pending_total"],
        "task_queue_pending_discover": task_queue_state["pending_discover"],
        "task_queue_pending_extract": task_queue_state["pending_extract"],
        "task_queue_pending_synthesize": task_queue_state["pending_synthesize"],
        "task_queue_pending_knowledge_pack": task_queue_state["pending_knowledge_pack"],
        "task_queue_next_pending_stage": task_queue_state["next_pending_stage"],
        "next_stage": next_stage,
        "report_allowed": report_allowed,
        "base_report_allowed": base_report_allowed,
        "blocking_reasons": blocking,
        "report_blocking_reasons": report_blocking,
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()

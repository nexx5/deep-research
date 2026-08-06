# 更新日志

本项目版本记录遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 语义。

## [V0.2] - 2026-08-06

### ✨ 新特性

- **批量 ingest（写入层提速 8-40 倍）**：zhishibao `knowledge-ingest.py` 支持 `--claims-file` 一次批量写入，全链路（索引+嵌入+关系+视图）只跑 1 次，不再逐条触发全量索引重建；实测小库约 8.7 倍、大库 100 条预估 20-40 倍。
- **per-claim 关系**：批量模式下每条断言可带 `_relation`（extends/coexist/opposing/...）或 `_merge_into` 内部字段，pop 后不入库；优先于函数级参数（向后兼容）。

### 🔧 修复

- 修复 5 处同源"批量失败路径"：
  1. per-claim 关系写回丢失（`relations.jsonl` 不写回）→ `batch_had_relation` 标志位
  2. 单条关系校验失败导致整批中断 → `continue` 单条隔离
  3. per-claim `_relation` 格式错误导致 ValueError 崩溃 → 格式校验前置
  4. 失败条目无重提闭环 → 流程强制解析 error、修正后单独重提
  5. 整批重跑幂等 → 文档强制只重提失败条目

### 📋 流程

- 知识管理员 Step1 重写为"串行判断 + 批量写"过渡态：判断产出带 `_search_evidence`（query / candidates_returned / basis），"先查后写"从承诺变为可验证数据；无检索证据的断言拒绝入库。
- 批量 `_relation: opposing:CLxxxx` 自动标双方 contested + 互加 opposing + 写 relations.jsonl，仲裁统一到 Step2 对已建立对执行。
- `check-research-state.py` 证据扫描升级：聚合 evidence/ 顶层与 raw/{local,web,pdf}/ 子目录，按来源编号去重（兼容新布局与旧布局）。
- 调研员 key_claims 规范：2-8 条是典型参考区间非上限，写入门槛是质量（独立可迁移模式 + boundary）；预估超 12-15 条按模式/边界分簇。
- 快速调研师：默认仅在对话中输出报告，用户明确指令落盘时才写文件。

### 兼容性

- 数据格式不变：claims.jsonl / relations.jsonl / SQLite schema 均未动。
- 旧用法全部保留：单条 `--claim`、函数级 `--relation`、函数级 `--merge-into`（回归验证通过）。
- 语义判断零改动：duplicate/merge/extend/conflict 判定仍由 AI 完成，脚本只执行。

---

## [V0.1] - 2026-07

- 初始发布：调研管理平台（Apache-2.0）。
- 三大工作流：调研采集（状态机驱动）、知识管理（知识包资产）、知识输出（报告/问答/设计/快速调研）。
- 完整 Sample 示例项目（深度调研agent与skill调研，含 HTML 报告与知识包）。

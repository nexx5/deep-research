# 更新日志

本项目版本记录遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/) 语义。

## [V0.2.2] - 2026-08-07

### ⚠️ 破坏性变更

- **取消原批次模式（旧协议项目）**：平台只支持知识包模式（新协议项目，必须有 `knowledge-pack/` 目录）。项目目录无 `knowledge-pack/` → 调研员返回 INVALID_PROJECT，由项目管理员按新协议重建骨架，不再按原批次模式直采执行。`02-采集.md` / `03-分析提取.md` / `04-质量闸门.md` 已加废弃声明，不再作为调研员子阶段文件被调度。

### ✨ 新特性

- **强制 MapReduce 派发采录员（禁止调研员直采）**：调研员自己是调度器，本批所有采集+采录任务（搜索→抓取→raw→采录→分析）必须交给采录员 subagent 执行，禁止在自己会话内直采替代采录员。修复根因：调研员直采会丢失"raw 原文完整性"与"D1 引用追溯"两类关键能力（只存在于采录员层指令），导致产出能力分叉。
- **并发派发 4~12，默认 6**：一个批次内并行派发 M 个采录员 task（默认 6，受 API 限流时降到 3，任务数 <4 按实际数）。
- **自动降并发机制（强制）**：连续 3 个 task 失败/超时 → 并发降到 3；连续 2 轮再失败 → 串行并标记质量告警。
- **批次启动自检日志点**：每次批次开始必须在 `run-state.md` 或 `.task/批次记录.md` 写一行"MapReduce 模式确认：knowledge-pack/ 存在 → 强制派发采录员，禁止直采 P0 已读"，作为可审计证据。
- **采录员 task prompt 必备要素九项（P0）**：调研员派发采录员时 task prompt 必须携带（目标锚点 / 为什么做 / 搜索硬约束 / raw 完整性 / D1 引用追溯 / 6 类线索 / 文件产出路径 / 硬约束 / 输出 JSON）。

### 🔧 强化（采录员层防御）

- **raw 原文完整性（强制）**：raw 必须是原文存档不是摘要，禁止"提炼要点""关键章节摘录"；长度接近原文（通常 5-50KB 而非 0.3-2.5KB）；PDF 用 PyMuPDF/pdfplumber 逐页保存；技术类按 6 维度自检（CLI/配置/API/架构/性能/实现，合格≥4）。
- **D1 引用追溯（强制）**：采录员扫描 raw 中外部引用，被引用但未采录的 → 生成 discovered_lead（trigger_type=引用追溯，priority≥P2）；规范族互相引用必须追溯；二手官方链接追溯为独立来源；不可访问标记"引用不可及"。

### 📋 流程

- orchestrator 批次调度逻辑改任务导向（"必须 MapReduce 派发采录员、禁止直采"），新增「派发调研员时的强制要求（P0）」段：模式强制声明 + 禁止"流程导向"表述（不写"执行流程 DISCOVER→EXTRACT→SYNTHESIZE 由你执行"）。
- 根 AGENTS.md 同步：调研员职责改为"调度器（MapReduce 强制派发）"，调研员子阶段节标注 02-04 已废弃。

### 兼容性

- **不兼容旧协议项目**：无 `knowledge-pack/` 目录的项目必须由项目管理员按新协议重建骨架后才能继续。
- 知识包数据格式不变：claims.jsonl / relations.jsonl / SQLite schema 均未动。
- EXTRACTOR_MODEL 轮换机制保留（采录员模型由环境变量指定，与并发机制不冲突）。

---

## [V0.2.1] - 2026-08-06

### 🔧 优化

- 优化脚本调用。

---

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

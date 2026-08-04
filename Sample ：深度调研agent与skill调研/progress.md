# 进度日志：深度调研agent与skill调研

> 项目配置见 `project.config.md`

## 2026-08-04 初始化

- 项目初始化，创建目录结构（复制自模板库）
- 填充 project.config.md（静态定义+策略映射+知识包Schema）、run-state.md（运行态）、1-规划/1-任务规划.md、task_queue.md、1-规划/4-知识包设计.md
- 知识包初始化：zhishibao knowledge-db-init.py（knowledge.db + 空 claims.jsonl + 空 relations.jsonl + config.json）；source-leads.jsonl 写入 12 条初始线索
- 初始化 knowledge-pack-深度调研agent与skill调研.json（元信息 + project_knowledge_schema）
- 建立 qmd 集合索引（BM25 已建；向量嵌入因全局缓存维度不匹配未做，需 `qmd embed -f` 全库重嵌）
- 质量校验：check-research-state project_valid=true；check-plan-review-quality PLAN_REVIEW_QUALITY_OK
- 当前状态：等待 PLAN_REVIEW 用户确认

---

## 2026-08-04 Batch 1（调研员首轮 DISCOVER+EXTRACT+SYNTHESIZE）

### 批次产出
- **raw×8**：raw-S001（GPT Researcher README）、raw-S002（Open Deep Research README+架构博客）、raw-S003（STORM README+论文摘要）、raw-S004（hyperresearch 公开资料）、raw-S005（ChatGPT DR 官方）、raw-S006（Perplexity DR 官方）、raw-S007（Gemini DR 官方合集）、raw-S008（Genspark 官网）
- **采录×8**：采录-S001~S008（全部 deep 档，SPO 表格 + evidence 引文 + characteristics）
- **分析×8**：分析-A001~A008（summary + key_claims + opposing_to）
- **跨源对比×1**：对比-C001（六维客观对照：能力/架构/工作流/成本开放度/证据知识管理/方法流派）

### 关键发现与处理
- **死链修正**：SLD001（assafelovic/deep-research）与 SLD002（OpenDeepResearch/OpenDeepResearch）均 404，分别修正为 gpt-researcher（assafelovic）与 langchain-ai/open_deep_research（经 GitHub API/搜索验证），已更新 source-leads.jsonl 并如实记录
- **冲突标记**：A002 写入 conflict_flags（OpenDeepResearch 多 agent vs Cognition 反多 agent）；A007 写入 conflict_flags（Gemini 官方文档结构化输出矛盾）
- **线索池**：12→25 条（8 done + 13 新增）；P0 待采 dzhng/deep-research（单 agent 流派）与 Deep Research Bench（评测基准）为下批重点
- **任务队列**：D001 completed；新增 D002-D007（开源补采/评测验证/流派对立/付费补采/剩余初始/社区口碑）
- **检查点**：checkpoint.py batch=1, phase=discover, sources_done=8, remaining=17

### 全局进度
- 当前 Phase：Phase 2（开源）+ Phase 3（付费）+ 缺口补采完成，D001-D014 全部 completed
- 已完成 Task：14/14
- 被阻塞 Task：0

---

## 2026-08-04 Batch 5（重计=1，consolidation 后缺口任务补采，D010-D014 完成）

### 批次产出
- **raw×6 新增**（累计 38）：raw-S033（DRACO 基准）、S034（Operator System Card）、S035（浏览器代理基准+竞品）、S036（STORM 论文）、S037（OpenManus）、S038（DeepResearchEval+继任者+DeerFlow/WebThinker）
- **采录×6 + 分析×6**：S033-S038 对应
- **跨源对比×1**：对比-C005（缺口补采汇总：浏览器代理流派版图/评测基准家族扩充/开源对照）

### 关键发现与处理
- **浏览器代理流派版图**：OSWorld/WebArena/WebVoyager 共同标尺（人类基线 72.36%/78.24%），三厂商自报成绩对照（CUA/Anthropic/Mariner）；Operator System Card 安全细节（prompt injection monitor 79%→99% recall）
- **DRACO 官方基准**：arXiv:2602.11685（Perplexity 自评利益相关），官方 70.5% vs 第三方 34% 须分别引用；原 PDF URL 下载失败已用 arXiv 同版替代
- **STORM 主论文**：pre-writing 三阶段学术证据 + 8+ 篇学术后继线索（趋势观察）
- **OpenManus**：任务给定 ShilongLee 不存在，采录 FoundationAgents/OpenManus（57.9k stars）——社区复刻 vs 闭源 Manus 开放度对照
- **DeepResearchEval**：量纲独立于 DRB 家族（三处标注）；MAF AutoGen 迁移指南继任实证
- **线索池**：48→53 条（48 done + 5 pending：P1×5 方向类）；D001-D014 全部 completed
- **检查点**：checkpoint.py batch=5, phase=discover, sources_done=38, remaining=5

### 全局进度
- **建议：交知识管理员二次 consolidation 判饱和**（38 源 + 5 份跨源对比；剩余 5 条 P1 方向线索由知识管理员评估）

---

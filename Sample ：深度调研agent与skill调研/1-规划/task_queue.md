# Task Queue

> 调研员的核心驱动。主 agent 循环：读队列 → 派发 sub-agent → 收摘要 → 更新队列。
> 任务类型：PLAN_REVIEW（方案确认）、DISCOVER（搜索抓取）、EXTRACT（提取标注）、SYNTHESIZE（聚类对撞合成）。

---

## 状态摘要

| 指标 | 值 |
|------|-----|
| 运行模式 | approved_execution |
| 总任务数 | 14 |
| pending | 0 |
| pending_approval | 0 |
| in_progress | 0 |
| completed | 14 |
| failed | 0 |
| blocked | 0 |
| 未分析采录数 | 0 |

> Batch 5（重计=1）完成（2026-08-04）：6 采录员产出 S033-S038（DRACO 基准、Operator System Card、浏览器代理基准+竞品、STORM 论文、OpenManus、评测家族+继任者+可靠性）+ 对比-C005（缺口补采汇总）。D010-D014 缺口任务全部完成，D001-D014 共 14 个任务全部 completed。

---

## 任务队列

| ID | 类型 | Source | 描述 | 优先级 | 状态 | 依赖 |
|----|------|--------|------|--------|------|------|
| D001 | DISCOVER | project | 初始采集（Batch1 已完成）：开源侧 4 篇（gpt-researcher/OpenDeepResearch/STORM/hyperresearch 公开资料）+ 付费侧 4 篇（ChatGPT/Perplexity/Gemini DR、Genspark），产出 raw-S001~S008 + 采录-S001~S008 + 分析-A001~A008；S001/S002 原 URL 404 已修正为真实生态实体 | H | completed | P001 |
| D002 | DISCOVER | leads | 开源组补采（Batch3 完成）：dzhng/deep-research(S009)、nickscamara(S011)、docs.gptr.dev+gptr-mcp(S012)、gemini-fullstack(S017)、dspy+STORM preview(S018) | H | completed | D001 |
| D003 | DISCOVER | leads | 评测基准与交叉验证（Batch3 完成）：DRB 基准(S010)、付费第三方评测(S013)、hyperresearchbench(S019)、DRB 双源对比(S020) | H | completed | D001 |
| D004 | DISCOVER | leads | 方法流派对立证据（Batch3 完成）：Cognition(S021)、Co-STORM(S021) | M | completed | D001 |
| D005 | DISCOVER | leads | 付费服务补采（Batch3-4 完成）：定价 S022、Perplexity 产品演进 S025 | M | completed | D001 |
| D006 | DISCOVER | leads | agent 框架内置能力（Batch4 完成）：LangChain/LlamaIndex 深度研究能力 S026 | M | completed | D001 |
| D007 | DISCOVER | leads | 付费服务社区口碑验证（Batch2 完成）：S014 | M | completed | D001 |
| D008 | DISCOVER | leads | 付费服务新条目 + 引用可靠性证据（Batch3 完成）：Kimi/Parallel/Azure/Claude/Grok 概览(S023)、引用幻觉审计(Cornell+arXiv 2604.03173)(S024) | M | completed | D007 |
| D009 | DISCOVER | leads | 学术/安全线索补采（Batch4 完成）：DRB II(S027)、LiveResearchBench+GAIA(S028)、FORGE+MisKnow-Agent+STC(S029) | M | completed | D008 |
| D010 | DISCOVER | leads | 付费服务基准补采（Batch5 完成）：Perplexity DRACO 官方基准 S033 | H | completed | D005 |
| D011 | DISCOVER | leads | 浏览器代理流派补采（Batch5 完成）：Operator System Card S034 + OSWorld/WebArena/WebVoyager+竞品 S035 | H | completed | D009 |
| D012 | DISCOVER | leads | 论文驱动流派学术一手证据（Batch5 完成）：STORM 主论文 S036 | M | completed | D009 |
| D013 | DISCOVER | leads | 开源对照样本补采（Batch5 完成）：OpenManus S037（任务给定 ShilongLee 不存在，采录 FoundationAgents/OpenManus） | M | completed | D005 |
| D014 | DISCOVER | leads | 评测基准家族与可靠性补充（Batch5 完成）：DeepResearchEval+继任者+DeerFlow/WebThinker S038 | M | completed | D009 |

---

## 线索生成任务

| ID | 类型 | 描述 | 来源 | 优先级 | 状态 |
|----|------|------|------|--------|------|
| | | | | | |

---

## 已完成任务

| ID | 类型 | Source | 描述 | 完成时间 | 产出 |
|----|------|--------|------|----------|------|
| D001 | DISCOVER | project | 初始采集 Batch1：开源 4 + 付费 4 | 2026-08-04 | raw-S001~S008、采录-S001~S008、分析-A001~A008、对比-C001 |
| D002 | DISCOVER | leads | 开源组补采（Batch3） | 2026-08-04 | S009/S011/S012/S017/S018 |
| D007 | DISCOVER | leads | 付费服务社区口碑验证（Batch2） | 2026-08-04 | raw-S014、采录-S014、分析-A014 |
| D005 | DISCOVER | leads | 付费服务补采（Batch3-4） | 2026-08-04 | S022/S025 |
| D006 | DISCOVER | leads | agent 框架内置能力（Batch4） | 2026-08-04 | S026 |
| D009 | DISCOVER | leads | 学术/安全线索补采（Batch4） | 2026-08-04 | S027/S028/S029 |
| D010 | DISCOVER | leads | 付费服务基准补采（Batch5） | 2026-08-04 | S033 |
| D011 | DISCOVER | leads | 浏览器代理流派补采（Batch5） | 2026-08-04 | S034/S035 |
| D012 | DISCOVER | leads | 论文驱动流派学术一手证据（Batch5） | 2026-08-04 | S036 |
| D013 | DISCOVER | leads | 开源对照样本补采（Batch5） | 2026-08-04 | S037 |
| D014 | DISCOVER | leads | 评测基准家族与可靠性补充（Batch5） | 2026-08-04 | S038 |
| D003 | DISCOVER | leads | 评测基准与交叉验证（Batch2-3） | 2026-08-04 | S010/S013/S019/S020 |
| D004 | DISCOVER | leads | 方法流派对立证据（Batch3） | 2026-08-04 | S021 |
| D008 | DISCOVER | leads | 付费新条目+引用可靠性（Batch3） | 2026-08-04 | S023/S024 |

---

## 队列运行规则

1. `plan_status != approved` 时，只允许执行 PLAN_REVIEW，不得执行 DISCOVER/EXTRACT/SYNTHESIZE。
2. 用户确认方案后，将 `plan_status` 改为 `approved`，并将 D001 从 `pending_approval` 改为 `pending`。
3. 选任务：H > M > L。同优先级内按 ID 顺序。
4. DISCOVER 完成后自动生成对应 EXTRACT 任务。
5. EXTRACT 完成条件：采录检查点通过。
6. SYNTHESIZE 触发：未分析采录 >= 5 或采集暂歇。
7. 线索处理：sub-agent 返回线索 → 主 agent 去重 → 生成 DISCOVER 任务入队。
8. 去重：同名/同址/同关键词的线索不重复添加。
9. 饱和判定：队列空 + 无缺口 + 无新线索 + 子问题全覆盖。
10. 每次队列变更后更新本文件。

---
source_id: S020
source_url: "https://arxiv.org/abs/2506.11763 ; https://arxiv.org/abs/2506.06287"
title: "双源对比：USTC DeepResearch Bench（arXiv:2506.11763）与 FutureSearch Deep Research Bench（arXiv:2506.06287）"
author: "Mingxuan Du 等（USTC 团队）; FutureSearch 团队"
date: "2025-06-13 ; 2025-05-06"
fetched_at: 2026-08-04T09:10:00
content_type: paper
access_note: "访问日期 2026-08-04；元数据与摘要经「多源搜索」skill 学术引擎（arXiv API / OpenAlex / Semantic Scholar）获取；评估器细节补充自两基准官方渠道（USTC GitHub README / drb.futuresearch.ai evals 页）"
---

# raw 存档说明

本 raw 文件为**双源合并存档**：两篇同名但不同源的 "Deep Research Bench" 论文。引用其中任一基准的分数时必须区分量纲（见断言 source 标注）。

---

# 论文一：USTC DeepResearch Bench

- **arXiv ID**：2506.11763
- **URL**：https://arxiv.org/abs/2506.11763
- **标题**：DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents
- **DOI**：10.48550/arXiv.2506.11763
- **OpenAlex Work ID**：W4415069437
- **发布**：2025-06-13（v1）
- **分类**：cs.CL / cs.IR（arxiv:comment: 31 pages, 5 figures）
- **作者**：Mingxuan Du, Benfeng Xu, Chiwei Zhu, Xiaorui Wang, Zhendong Mao
- **团队归属**：中国科学技术大学（USTC）——GitHub README 官方联系邮箱为 dumingxuan@mail.ustc.edu.cn / imlrz@mail.ustc.edu.cn（mail.ustc.edu.cn 域名）
- **OpenAlex 引用数**：2（更新日期 2026-07-28，全部来自 2026 年）
- **官方仓库**：https://github.com/Ayanami0730/deep_research_bench（Code License: MIT）
- **官方主页**：https://deepresearch-bench.github.io/
- **数据集**：https://huggingface.co/datasets/muset-ai/DeepResearch-Bench-Dataset
- **Leaderboard**：https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard ；https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard ；第三方平台 AGI-Eval：https://agi-eval.cn/evaluation/detail?id=67

## arXiv 摘要（原文）

> Deep Research Agents are a prominent category of LLM-based agents. By autonomously orchestrating multistep web exploration, targeted retrieval, and higher-order synthesis, they transform vast amounts of online information into analyst-grade, citation-rich reports--compressing hours of manual desk research into minutes. However, a comprehensive benchmark for systematically evaluating the capabilities of these agents remains absent. To bridge this gap, we present DeepResearch Bench, a benchmark consisting of 100 PhD-level research tasks, each meticulously crafted by domain experts across 22 distinct fields. Evaluating DRAs is inherently complex and labor-intensive. We therefore propose two novel methodologies that achieve strong alignment with human judgment. The first is a reference-based method with adaptive criteria to assess the quality of generated research reports. The other framework is introduced to evaluate DRA's information retrieval and collection capabilities by assessing its effective citation count and overall citation accuracy. We have open-sourced DeepResearch Bench and key components of these frameworks at https://github.com/Ayanami0730/deep_research_bench to accelerate the development of practical LLM-based agents.

## 官方 README 关键陈述（GitHub: Ayanami0730/deep_research_bench，访问 2026-08-04）

### 任务集构成
- 100 个 PhD-level 研究任务，由领域专家在 **22 个不同领域**精心制作。
- 任务语言构成：**50 中文 + 50 英文**。
- 主题分布依据 **96,147 条匿名化用户查询**（来自 web search-enabled LLM 交互）分析，按 WebOrganizer taxonomy 分为 22 个主题域，以保持与真实世界使用一致的主题平衡。
- 领域举例：Science & Technology（物理、化学、生物学、环境科学、工程）；Finance & Business（投资、个人财务、营销、人力资源）；Software（软件与互联网使用相关主题）；Others（艺术与设计、娱乐、历史、工业、交通、旅行等）。
- 专家任务收集流程：邀请 PhD 级专家与资深从业者（5+ 年经验）设计挑战性研究任务，经人工筛选（质量、清晰度、真实性、挑战水平）产出 100 个任务。

### 评估框架
- **RACE（Reference-based Adaptive Criteria-driven Evaluation）**：评估**报告生成质量**，多步流程：
  - 动态标准生成：自动生成任务特定评估标准，覆盖四个关键维度——Comprehensiveness（覆盖广度与深度）、Insight/Depth（分析与洞察质量）、Instruction-Following（遵循任务要求）、Readability（清晰度、组织、呈现质量）
  - 参考基准评分：将目标报告与高质量参考报告对比，确保判别性评估
  - 加权评估：使用适配各任务具体要求的动态权重
- **FACT（Framework for Factual Abundance and Citation Trustworthiness）**：评估**信息检索与 grounding 能力**：
  - 声明-URL 提取：自动从生成报告中提取事实声明及其引用来源
  - 去重：移除冗余声明-URL 对，聚焦唯一事实声明
  - 支持验证：使用网页抓取与 LLM 判断被引来源是否实际支持声明
  - 引用指标：**Citation Accuracy**（正确支持引用的百分比）、**Effective Citations**（每任务可验证支持引用的平均数量）

### 评估器版本演进（LLM-as-judge）
- 2025-07-15 更新：RACE 评估使用 Gemini-2.5-Pro，FACT 评估使用 Gemini-2.5-Flash（此前更早版本被"superseded"）。
- 2026-05-11 更新：官方评估器切换为 **GPT-5.5**（RACE 评估器）与 **GPT-5.4-mini**（FACT pipeline）；同日新增对 Kimi-Researcher、Doubao-DeepResearch、Claude-Researcher 的完整评估。
- Leaderboard 迁移计划：2026-05-31 前为双接受窗口（legacy Gemini-2.5-Pro 与新 GPT-5.5 双榜并行）；2026-06-01 起仅维护 GPT-5.5 榜，原论文结果将用 GPT-5.5 重评并自动迁移。

### 提交要求（截至 2026-05-11 更新）
- 需提供 OpenAI/OpenRouter/OpenAI API key（GPT-5.5，用于验证/评估）；OpenRouter 为默认后端；Jina API key 用于 FACT 网页抓取。
- 开放/闭源模型均可提交；闭源需提供产品页与/或 API 链接用于复现验证。

---

# 论文二：FutureSearch Deep Research Bench

- **arXiv ID**：2506.06287
- **URL**：https://arxiv.org/abs/2506.06287
- **标题**：Deep Research Bench: Evaluating AI Web Research Agents
- **DOI**：10.48550/arXiv.2506.06287
- **OpenAlex Work ID**：W4417114727
- **发布**：2025-05-06（v1）
- **分类**：cs.AI
- **作者**：Nikos I. Bosse, Jon Evans, Robert G. Gambee, Daniel Hnyk, Peter Mühlbacher, Lawrence Phillips, Dan Schwarz, Jack Wildman
- **团队归属**：FutureSearch（公司/研究团队，官方 evals 页域名 futuresearch.ai）
- **公开 Leaderboard**：https://drb.futuresearch.ai/

## arXiv 摘要（原文）

> Amongst the most common use cases of modern AI is LLM chat with web search enabled. However, no direct evaluations of the quality of web research agents exist that control for the continually-changing web. We introduce Deep Research Bench, consisting of 89 multi-step web research task instances of varying difficulty across 8 diverse task categories, with the answers carefully worked out by skilled humans. We provide a "RetroSearch" environment with a large frozen set of scraped web pages, and demonstrate that offline "RetroSearch" agents perform comparably to "live web" agents, enabling reliable evaluations of models over time. We provide robust agent tooling and scaffolding to benchmark major LLMs as they are released, including "thinking" models like o3 and Gemini 2.5 Pro. We include automated evaluations of the lengthy agent traces to report progress over time in hallucinations, tool use, and forgetting. Finally, we evaluate the major web research products branded as "Deep Research", "Deep Search", "Search", or "Research." Results are available on a public leaderboard at https://drb.futuresearch.ai/.

## 官方 evals 页关键陈述（drb.futuresearch.ai，访问 2026-08-04）

### 任务集构成
- DRB 基准评测 LLM agent 在网页上的研究能力；每个真实世界任务提供 **10k-100k 离线存储网页**用于搜索与推理，并附精心整理的答案。
- 评分方式：先按任务类别求平均（radar chart），再跨全部任务求平均；Runtime 由 ReAct 步数估计（非墙钟时间）。

### RetroSearch 环境
- DRB（与 BTF-2）使用 RetroSearch：向 agent 提供**冻结的、先前抓取的网页版本**而非实时页面，使评测在网页变化时可复现，并使预测任务可"past-casting"。
- RetroSearch 目标：尽可能模拟 Google 搜索（具体为 Serper search API），最小化 live 与 retro agent 运行的差异。单次 RetroSearch 查询流程：
  1. 对查询执行 live Serper 搜索
  2. 从 RetroSearch 数据库与其他归档源查找搜索结果中获得的页面
  3. 若页面不在 RetroSearch 数据库中则从结果中移除
  4. 使用简单 LLM 从页面内容样本重写 snippet
  5. 以 Google 结果原始格式返回

### 论文中评测覆盖对象（摘要明确陈述）
- 主要 LLM（含 o3、Gemini 2.5 Pro 等 "thinking" 模型）
- 品牌为 "Deep Research"、"Deep Search"、"Search"、"Research" 的主要网页研究产品

### FutureSearch 相关评测体系（页面信息，用于语境）
- BTF-2（Bench to the Future 2，arXiv:2506.21558）：1,417 个预测问题，冻结 15M 文档语料，Brier score。
- BTF-3：1,907 个已解决预测问题（1,515 binary + 392 numeric），Brier/RPS。
- 两个基准均使用 RetroSearch；评测由 FutureSearch evals 团队维护。

---

# 采集过程记录

| 渠道 | 用途 | 结果 |
|---|---|---|
| arXiv API（export.arxiv.org/api/query?id_list=2506.11763,2506.06287） | 元数据+摘要 | 成功，两篇均返回完整 entry |
| OpenAlex API（title.search:DeepResearch Bench / Deep Research Bench） | 引用数/DOI/机构 | 成功；USTC cited_by_count=2；另发现同团队 DeepResearch Bench II（arXiv:2601.08536） |
| Semantic Scholar API（references 接口） | 两论文参考文献 | 成功；各返回 25 条引用（含 GAIA、BrowseComp、WebArena、WebShop 等） |
| GitHub API（repos/Ayanami0730/deep_research_bench/readme） | USTC 官方 README（RACE/FACT 命名） | 成功（GitHub 网页直连 transport error，API 可达） |
| drb.futuresearch.ai（webfetch） | FutureSearch 官方 evals 页（RetroSearch 架构/任务说明） | 成功 |

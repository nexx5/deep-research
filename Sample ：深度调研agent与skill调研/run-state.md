# 运行状态：深度调研agent与skill调研

> 运行时累积状态。随批次更新，与 `project.config.md`（静态定义，PLAN_REVIEW 后冻结）分离。
> 机器读 `knowledge-pack/batch-state.json`，本文件供 agent/人类读 + 采录员做去重 + 调研员关键词追加。
> **本文件不替代 batch-state.json**——还原点以 batch-state.json 为准，本文件是人类/agent 可读镜像。

---

## 执行参数

```yaml
execution:
  parallel_discover_limit: 8
  failure_fallback_limit: 3
  mode: continuous
```

---

## 搜索参数（每轮可变）

```
当前轮参数 = {
  round: 4              本轮轮次（agent 每轮自动 +1）
  breadth: 5            本轮搜索宽度（生态调研中等宽度）
  depth: 2              递归深度（浅层，覆盖官网/README/评测即可）
  threshold: 0.7        当前轮采集阈值（Batch4 完成后收窄，进入深挖/收尾）
  sources: [arxiv, openalex, bing, searxng]   本轮启用搜索源（含论文tag故含学术引擎）
  exclude: []           排除关键词
  user_notes: ""        用户补充说明
}
```

---

## 批次进度

- **当前批次：** batch 5（重计=1，已完成，6 条缺口任务采录完成，18 新文件 + 对比-C005）
- **已有采录：** 38 篇（raw-S001~S038）
- **模型配比：** deepseek-v4-flash 并发采集 6 个采录员（Batch5）
- **上批次结论摘要：** DRACO 官方基准（arXiv:2602.11685，10 领域生产数据驱动、加权 rubric 四轴、Perplexity 自评利益相关、官方 70.5% vs 第三方 34% 须分别引用）；Operator System Card（分层安全、prompt injection monitor 79%→99% recall、100 提示 13 错误）；浏览器代理评测标尺（OSWorld 72.36%/WebArena 78.24% 人类基线，三厂商自报对照）；STORM 主论文（pre-writing 三阶段、FreshWiki 评估、8+ 学术后继线索）；OpenManus（FoundationAgents 57.9k stars，社区复刻 vs 闭源 Manus 开放度对照）；DeepResearchEval（量纲独立于 DRB 家族）+ MAF/Agents SDK 继任实证 + DeerFlow/WebThinker 对照

---

## focus_keywords / explore_keywords（按批次累加，调研员追加，不写回 project.config）

> 调研员每批次从分析线索中追加关键词到本段（累加不覆盖）。去重时与已采列表+id_registry 比对。

### batch 0 初始种子（前置准备注入，供 D001 首轮使用）
- 开源框架：deep-research 开源复刻（assafelovic/deep-research）、OpenDeepResearch、STORM（stanford-oval/storm）、hyperresearch
- 开源 skill：深度调研类 research skill、Skill-hub 深度调研类、claude code research skill、awesome agent skills 中的 research 类
- agent 框架内置：LangChain Deep Research、LlamaIndex Deep Research、OpenClaw 深度研究能力
- 付费服务：ChatGPT Deep Research、Perplexity Deep Research、Gemini Deep Research、Genspark、Manus、OpenAI Operator
- 对比维度词：deep research architecture / agent loop / planner / retriever / evidence chain / knowledge base / pricing

### batch 1 追加（来自 A001-A008 线索发掘，累加）
- 开源补充实体：dzhng/deep-research（单 agent 连续深化流派）、nickscamara/open-deep-research（Firecrawl 路线）、langchain-ai/deep_research_from_scratch、gemini-fullstack-langgraph-quickstart、gptr-mcp、AG2（ag2ai/ag2）
- 评测基准：Deep Research Bench（DRB，RACE/FACT 评估器）、hyperresearchbench、DeepSearchQA、GAIA、Humanity's Last Exam（HLE）、SimpleQA
- 方法流派：Plan-and-Solve（arXiv:2305.04091）、STORM/Co-STORM（论文驱动）、Cognition dont-build-multi-agents（反多agent）、单agent vs 多agent 流派对比、人机协作深度调研（Co-STORM）、MCP 工具接口标准
- 付费服务补充：Perplexity Advanced DR（Opus 4.6 Thinking/代码沙箱）、Perplexity Labs（Research 更名/10+分钟扩展）、OpenAI Operator（调研+执行组合）、Google AI Ultra、Genspark Claw/Speakly/GenClipboard 独立产品线
- 依赖生态：Tavily（检索 API）、crawl4ai（爬虫）、Unpaywall/Europe PMC（OA 学术）、dspy、LangSmith（可观测性）
- 对比维度补充：官方声称 vs 独立验证差距、成本结构（订阅/API用量/自托管资源）、证据引用机制（编号引用/Sources 段/引用-句子绑定）、知识复用（长期记忆/vault）

### batch 2 追加（来自 A009-A016 线索发掘，累加）
- 评测基准家族：DRB 论文（arXiv:2506.11763，USTC+Metastone）、FutureSearch DRB（arXiv:2506.06287，同名不同源）、DeepResearch Bench II（arXiv:2601.08536）、DeepResearchEval（arXiv:2601.09688）、GAIA 排行榜、WebArena/WebVoyager（浏览器代理基准）
- 第三方评测指标：RACE（报告质量四维+Overall）、FACT（引用准确率+有效引用数）、检查点准确率（AIMultiple 33 检查点）、引用幻觉审计（arXiv:2604.03173）、Cornell 污染漏洞
- 生态新条目：Kimi K2.5 Deep Research、Parallel（parallel.ai）、Azure AI Foundry DR、Claude Deep Search、Grok Deep Search、Claude Deep Search、agent CLI 类（Claude Code/Codex 深度调研）
- 依赖生态补充：Firecrawl（商业抓取 API）、Vercel ai-chatbot 模板、AI SDK、OpenRouter、TogetherAI、DeepSeek-R1、Fireworks
- 通用 agent 对照：Manus（Meta 收购撤销事件、积分计费、Browser Operator）、OpenManus 开源复刻、OpenAI Operator（CUA/agent mode）
- 社区口碑主题：Perplexity"快而浅"、ChatGPT 配额成本、Gemini 指令遵循/幻觉、Genspark 运营问题、引用质量跨服务共现痛点

### batch 3 追加（来自 A017-A024 线索发掘，累加）
- 方法流派三角：单 agent（dzhng/deep-research）vs 多 agent（OpenDeepResearch/LangGraph）vs 反多 agent（Cognition 上下文工程+单线程）vs 人机协作（Co-STORM 三方话语协议+mind map）
- 技术底座：dspy（编程式 prompt 优化，STORM/Co-STORM 官方实现框架，arXiv:2310.03714）、litellm、langgraph、Google Search grounding
- 评测基准体系：USTC DRB（RACE/FACT，量纲须标注）vs FutureSearch DRB（RetroSearch+trace）同名不同源；DRB II（132 任务/9430 rubric）；LiveResearchBench；GAIA；BrowseComp；WebArena
- 攻击/可靠性研究：FORGE（轨迹劫持）、MisKnow-Agent（误导知识）、Search-Time Contamination、DRBench（53,090 URLs）、ExpertQA、urlhealth 工具
- 官方附属基准利益相关：hyperresearchbench（benchmarked internally、n=9 pilot、third party pending）
- 定价公开度：OpenAI 定性配额（Free/Plus/Pro）、Perplexity /pricing 404→拆分 Pro/Max/Enterprise、Genspark 积分结构（Plus 10,000/Pro 125,000 credits）+ 登录墙
- 新条目形态：Kimi Deep Research、Parallel（自建索引 vs 第三方搜索 API 流派）、Azure AI Foundry agent、Claude Research/Deep Search、Grok DeepSearch
- 多 agent 库生态：CAMEL、MetaGPT、OpenAI Swarm、Microsoft AutoGen（Cognition 点名批评对象）

### batch 4 追加（来自 A025-A032 线索发掘，累加）
- 框架内置能力：LangChain deepagents harness（MIT、27.3k stars、官方 deep research 教程）vs LlamaIndex 无专用页（BM25 全站验证）
- 浏览器代理流派：CUA（Perception-Reasoning-Action 循环、OSWorld 38.1%/WebArena 58.1%/WebVoyager 87% 官方声称）、Operator System Card、Anthropic computer use、Google Project Mariner、Perplexity Computer（Search as Code、20+ 模型路由）
- 调研-执行一体趋势：Perplexity DR 并入 Computer 宿主、OpenAI DR+Operator 组合愿景
- 评测基准补全：DRB II（9430 rubric 独立量纲）、LiveResearchBench（动态抗污染）、GAIA（gating 防泄露）、DRACO（Perplexity 官方）
- 攻击/可靠性：FORGE 轨迹劫持、MisKnow-Agent FCAR、Search-Time Contamination 虚增 4%、DeerFlow/WebThinker 受影响系统
- 框架继任者：OpenAI Agents SDK（Swarm）、Microsoft Agent Framework（AutoGen MAF 1.0）
- 方法流派补充：DSPy 论文（自改进管线）、Anthropic workflows vs agents 分类（orchestrator-workers 合法）、抽象层态度张力（Anthropic 反框架 vs DSPy 编译器）

### batch 5（重计=1）追加（来自 A033-A038 线索发掘，累加）
- 浏览器代理评测标尺：OSWorld（369 任务/人类 72.36%）、WebArena（四域/人类 78.24%）、WebVoyager（15 网站/GPT-4V 评估）；三厂商自报成绩对照（CUA/Anthropic/Mariner）
- 官方基准利益相关：DRACO（Perplexity+Harvard 自评，judge 第三方 Gemini-3-Pro，官方 70.5% vs 第三方 34% 须分别引用）、DeepSearchQA（Google，官方声称 SOTA）、ResearchRubrics（Scale AI）
- STORM 学术后继簇：HiEviDR-Bench/GEIS/Dossier/ViDR/CogGen/Self-Evolving DR 等 8+ 篇（趋势观察证据）
- 框架继任实证：MAF 官方 AutoGen 迁移指南；Agents SDK 未提 Swarm
- 深度调研系统对照：DeerFlow 2.0 harness 转型、WebThinker LRM agent、OpenManus（57.9k stars 社区复刻）
- 安全维度：Operator System Card（分层安全/prompt injection monitor/Preparedness Framework）、GPT-4o System Card 继承

---

## dead_ends（已穷尽路径，留作饱和判定参考）

| 代号 | 线索/方向 | 处理 |
|---|---|---|
| | | |

---

## 用户阶段性意见（运行期注入的临时定义/售前定义/阶段性成果，不写 project.config）

- 2026-08-04 用户确认新定位：**客观生态观察**——以"看"为主、客观收集证据为主，不做改进方向建议；与自有平台的对比不写入调研任务，由最终知识分析自然得出。PLAN_REVIEW 方案已按此修订（project.config.md / 1-任务规划.md / 4-知识包设计.md / task_queue.md 同步）。

---

## 备注

- 初始种子关键词仅供 D001 首轮使用，调研员须在后续批次按线索追加（累加不覆盖）。
- 付费服务定价/能力变化快，采录时须记录访问日期与版本。

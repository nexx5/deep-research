---
source_id: S023
source_url: https://www.kimi.com/features/deep-research + https://parallel.ai + https://azure.microsoft.com/en-us/blog/introducing-deep-research-in-azure-ai-foundry-agent-service + https://support.claude.com/en/articles/11088861-use-research-on-claude + https://x.ai/news/grok-3 + https://docs.x.ai/developers/tools/web-search
title: 新形态付费 Deep Research 服务概览（Kimi Deep Research / Parallel / Azure AI Foundry Deep Research / Claude Research(Deep Search) / Grok DeepSearch）
author: 多源（见各节）
date: 2025-02 ~ 2026-06（各节标注）
fetched_at: 2026-08-04
content_type: official_product_overview_collection
---

> 本 raw 为五条目官方页/公告/文档合并存档，全部为**厂商官方来源**（官方声称，非独立验证）：
> - **源A = Kimi Deep Research**（https://www.kimi.com/features/deep-research，Moonshot AI 官方功能页，英文版，页面素材日期 2026-06）
> - **源B = Parallel**（https://parallel.ai，官方首页+FAQ）
> - **源C = Azure AI Foundry Deep Research**（https://azure.microsoft.com/en-us/blog/introducing-deep-research-in-azure-ai-foundry-agent-service，官方博客，作者 Yina Arenas，2025-07-07）
> - **源D = Claude Research（第三方称 Claude Deep Search）**（https://support.claude.com/en/articles/11088861-use-research-on-claude，Claude 官方支持页）
> - **源E = Grok DeepSearch**（https://x.ai/news/grok-3，xAI 官方公告 2025-02-19；https://docs.x.ai/developers/tools/web-search，xAI 官方文档）
> 各节标注对应 URL 与访问日期 2026-08-04。仅存档原文表述，不评判。官方声称全部单独标注。

---

# 源A：Kimi Deep Research（Moonshot AI）

## A0. 元信息
- URL: https://www.kimi.com/features/deep-research
- 运营方: Moonshot AI（月之暗面）
- 页面标题: "Kimi Deep Research: From Concept to Report"
- 功能入口: https://www.kimi.com/deep-research

## A1. 核心定位
- 官方首页语: "The depth of a research team, the speed of AI. Describe your topic, upload your files, and let Kimi Deep Research take it from there. Searching across the open web and professional databases to produce thorough, cited reports with multi-format outputs tailored to how you work."（描述主题、上传文件，Kimi Deep Research 自主搜索开放网络与专业数据库，产出详尽、带引用的多格式报告）
- "Start with your intent, then build a structured research plan": 输入研究主题并可上传文件，Kimi 分析输入、提出澄清问题确认范围、在任何搜索开始前规划研究计划。
- "Search at scale with high-quality, database-supported results": 每个研究任务执行数十次定向搜索，覆盖开放网络与专业数据库；综合新闻媒体、政府来源、学术出版物、企业数据库、实时金融与经济数据。
- "Research that gets sharper with every follow-up": 支持同一会话多轮对话；追问、要求深挖或改变研究角度时，Kimi 每轮检索额外来源并细化分析，基于已有信息延续而非从头开始。
- 后台运行: FAQ 明示 "Kimi Deep Research can run in the background, so you can continue using other Kimi features"。
- 三阶段工作流（FAQ）: "Clarification, autonomous execution, and generating rich, deep, and multi-format research deliverables."

## A2. 输出格式
- 官方明示支持: Markdown 报告、PDF、PowerPoint 演示、Word 文档、Excel 表格、交互式 HTML 报告（"interactive HTML reports, Word documents, PowerPoint decks, Excel spreadsheets, and PDFs"）。
- 报告内嵌图表与数十个可追溯引用来源（来自上传材料与网络研究）。

## A3. 定价与额度
- FAQ: "Kimi Deep Research is available on the free plan with a limited monthly allowance. For more complex or multi-turn research tasks, additional credits can be unlocked by upgrading your plan."
- FAQ: "Kimi doesn't cap Deep Research by query count; the usage is measured by token consumption."（按 token 消耗计量，不按查询次数）

## A4. 适用场景（官方列举）
- Finance & Investment（投资/公司分析，每项声明可引用可追溯）
- Academic research（文献检索与结构化综述）
- Market research（市场数据综合、竞争格局与行业趋势）
- Consulting & Business analysis（面向董事会与客户演示的结构化引用报告）

---

# 源B：Parallel（Parallel Web Systems）

## B0. 元信息
- URL: https://parallel.ai（官方首页）
- 定位语: "Web infrastructure for AI to search, extract, monitor, and reason over the world's information"
- 关联文档: https://docs.parallel.ai

## B1. 产品定位
- FAQ: "Parallel builds web search and research APIs purpose-built for AI agents and agentic workflows. We run our own web-scale index with billions of pages and millions more added and updated daily."
- 差异定位（FAQ，官方自述）: "Most search APIs retro-fit traditional search engines for AI, but Parallel's Index was designed for LLMs and programmatic use from the start."
- 客户（官方列举）: Harvey、Formation Bio、Attio、Starbridge、Granola、Monaco、Manus、Hex、Modal、Dropbox、Greptile、Rogo、Profound、Opendoor。

## B2. 产品套件
- **Task API**: "Deep research and analysis at enterprise scale. Give it an objective, get back structured, cited answers"
- **Monitor API**: "Track changes and act on what matters, with structured alerts via webhook"
- **FindAll API**: "Build structured datasets with real-time enrichment. Describe what you want, get a live list"
- **Search API**: "The highest-accuracy web search for your AI. Fresh, fast, and affordable grounding in one call"
- **Extract API**: "Get full or excerpted contents from the public web, including PDFs, JS-heavy pages, and government sites"
- **Responses API**: "returns synthesized, cited answers from the live web in seconds... same quality as Task, purpose-built for conversational speed"
- **Parallel Web Index**: "Real-time access to the web's most valuable sources, built from the ground up for AIs"

## B3. 深度研究能力（Task API / Web Agents）
- "Hand over an objective and get back hundreds of finished, cited reports in minutes: an account brief before the call, an investment memo, a competitive landscape. Analyst-grade work, embedded in your workflow."
- 可验证性: "Parallel's Web Agents use Basis to attach provenance and calibrated confidence scoring to every output, for trusted use and auditability in production."（Basis 框架：引用、结果背后的推理、每项事实的校准置信度评分；置信度可反馈回检索）
- 成本结构: "Per-request pricing means you pay for answers, not tokens."

## B4. 定价与开放度
- FAQ: "Web search starts as low as $1 per 1,000 requests."
- FAQ: "New accounts get a signup credit, and every account gets a recurring free monthly allowance of $5." 免费 hosted MCP server（个人/爱好者适用）。
- 官方评测数据（官网自报，2026-04-19~21 测试）: 六项开放基准（BrowseComp/FRAMES/FreshQA/HLE/SealQA/WebWalker）上 Parallel Turbo 对比 Exa/Tavily/Brave/SerpAPI/OpenAI Web Search 的准确率-成本表（如 BrowseComp 51%/$216 CPM vs Exa 33.7%/$361、Tavily 19.3%/$357；SimpleQA 91%/$8 vs Exa 89.3%/$20、Tavily 72%/$23）。方法：GPT-5.4 agent 共享 harness，≤25 次工具调用/问题，GPT-5.4 LLM 判分。
- 合规: SOC 2 Type II、HIPAA-ready、GDPR、零数据留存选项、SSO/SAML。
- 集成: Google Cloud、OpenRouter、Vercel、LangChain、Supabase、Google Sheets、Snowflake、Gemini、Hermes Agent、OpenClaw、n8n；OpenAI SDK 兼容（base URL 指向 Chat API）；MCP server 适配 Cursor/Claude Code。

---

# 源C：Azure AI Foundry Deep Research（Microsoft）

## C0. 元信息
- URL: https://azure.microsoft.com/en-us/blog/introducing-deep-research-in-azure-ai-foundry-agent-service
- 作者: Yina Arenas（Corporate Vice President, Microsoft Foundry）
- 日期: 2025-07-07，4 min read
- 状态: "public preview"（有限公开预览）

## C1. 核心定位
- 官方原文: "Deep Research in Azure AI Foundry—an API and software development kit (SDK)-based offering of OpenAI's advanced agentic research capability, fully integrated with Azure's enterprise-grade agentic platform."（OpenAI 高级 agentic 研究能力的 API/SDK 形态企业化封装）
- "developers can build agents that deeply plan, analyze, and synthesize information from across the web—automate complex research tasks, generate transparent, auditable outputs, and seamlessly compose multi-step workflows with other tools and agents"
- 对比定位（官方自述）: "Unlike packaged chat assistants, Deep Research in Foundry Agent Service can evolve with your needs—ready for automation, extensibility, and integration with future internal data sources."

## C2. 架构与 agent 流程（官方五步）
1. **Clarifying intent and scoping the task**: 用户/下游应用提交查询，agent 使用 GPT 系列模型（含 GPT-4o、GPT-4.1）澄清问题、收集上下文、精确界定研究任务。
2. **Web grounding with Bing Search**: 安全调用 Grounding with Bing Search 工具，获取高质量近期网络数据——"no hallucinations from stale or irrelevant content"（官方表述）。
3. **Deep Research task execution**: o3-deep-research 模型执行研究任务，逐步推理、随新洞察转向、综合全面答案。
4. **Transparency, safety, and compliance**: 最终输出为结构化报告，记录答案、模型推理路径、来源引用与澄清请求——"fully auditable"。
5. **Programmatic integration and composition**: Deep Research 以 API 暴露，可从自定义业务应用/内部门户/工作流自动化工具调用，或作为多 agent 链的一部分（例：一个 agent 做深度网络分析、一个用 Azure Functions 生成幻灯片、一个用 Azure Logic Apps 发邮件）。

## C3. 定价（官方博客公布，o3-deep-research）
- Input: $10.00 per 1M tokens
- Cached Input: $2.50 per 1M tokens
- Output: $40.00 per 1M tokens
- 另计: Grounding with Bing Search 费用 + 澄清问题所用的基础 GPT 模型费用（Search context tokens 按所用模型的输入 token 价计费）。

## C4. 开放度
- 有限公开预览（limited public preview），需注册 https://aka.ms/oai/deepresearchaccess
- 形态为 API/SDK agent tool，非消费者聊天功能
- 组合生态: Logic Apps、Azure Functions、Foundry Agent Service connectors

---

# 源D：Claude Research（Anthropic；第三方评测称 "Claude Deep Search"）

## D0. 元信息
- URL: https://support.claude.com/en/articles/11088861-use-research-on-claude
- 官方功能名: "Research"（支持页标题 "Use research on Claude"；AIMultiple 等第三方评测称 "Claude Deep Search"——命名差异如实记录）
- 访问渠道: Claude 网页版、Claude Desktop、Claude Mobile

## D1. 核心定位与能力
- 官方原文: "Research transforms how Claude finds and analyzes information. Claude operates agentically, conducting multiple searches that build on each other while determining exactly what to investigate next. It explores different angles of your question automatically and works through open questions systematically."
- 输出: "delivers thorough answers in minutes, complete with easy-to-check citations"
- 前提: "You must have web search turned on for research to function."
- 内部上下文: 开启后可跨内部上下文（连接 Gmail、Google Calendar、Google Docs 时）与网络进行 research。

## D2. 开放度与定价
- 仅付费计划用户可用: "Research is available for users with paid Claude plans (Pro, Max, Team, or Enterprise) using Claude on the web, Claude Desktop, or Claude Mobile."
- 用量: "Research is subject to the same limits as standard Claude conversations. However, research sessions can use up your limits faster due to Claude retrieving multiple sources and providing comprehensive responses."
- 无单独 API/自托管形态描述（支持页未提及 API 版 Deep Research）。

---

# 源E：Grok DeepSearch（xAI）

## E0. 元信息
- 公告 URL: https://x.ai/news/grok-3（"Grok 3 Beta — The Age of Reasoning Agents"，2025-02-19）
- 文档 URL: https://docs.x.ai/developers/tools/web-search
- 功能名: DeepSearch（官方公告拼写 "DeepSearch"）

## E1. 首次发布与定位（Grok 3 公告）
- 官方原文: "As a first step towards this vision, we are rolling out DeepSearch—our first agent. It's a lightning-fast AI agent built to relentlessly seek the truth across the entire corpus of human knowledge. DeepSearch is designed to synthesize key information, reason about conflicting facts and opinions, and distill clarity from complexity."
- 用途（官方列举）: "Whether you need to access the latest real-time news, seek advice about your social woes, or conduct in-depth scientific research, DeepSearch will take you far beyond a browser search."
- 输出: "Its final summary trace results in a concise and comprehensive report"（最终总结轨迹产出简洁而全面的报告）
- 上下文: Grok 3 公告同时发布 Grok 3 (Think) 与 Grok 3 mini (Think) 推理模型；DeepSearch 定位为"结合推理与工具使用的 agent"第一步。

## E2. 开放度（公告口径）
- "Grok 3 is now available to 𝕏 Premium and Premium+ users on 𝕏 and Grok.com. 𝕏 Premium+ users will also immediately gain access to Think and DeepSearch."
- "DeepSearch will also be released to Enterprise partners via our API."（公告称将通过 API 向企业伙伴提供）
- 发布时间背景: 公告日期 2025-02-19，两款模型"仍在训练中"。

## E3. Web Search 工具 API（docs.x.ai，独立层面）
- 官方文档: "The Web Search tool enables Grok to search the web in real-time and browse web pages to find information."
- SDK 支持: xAI SDK（`web_search`）、OpenAI Responses API（`web_search`）、Vercel AI SDK（`xai.tools.webSearch()`），及所有 Responses API 兼容 SDK。
- 示例模型: grok-4.5（文档示例使用该模型）。
- 参数: `allowed_domains`（仅搜指定域，最多 5）、`excluded_domains`（排除域，最多 5，不能与 allowed 同用）、`enable_image_understanding`（浏览时分析图片）、`enable_image_search`（搜索图片并以内嵌返回）。
- 注: 该文档描述的是模型可调用的 web search 工具（API 层），与 E1 的应用内 DeepSearch agent 是两个层面；文档未使用 "DeepSearch" 一词描述该工具。

---

## 跨条目观察（客观记录，不评判）

1. **命名差异**: 官方功能名并不统一——Kimi 用 "Deep Research"、Azure 用 "Deep Research"、Claude 支持页用 "Research"（第三方 AIMultiple 称 "Claude Deep Search"）、Grok 用 "DeepSearch"、Parallel 用 "Task API / deep research"。
2. **形态差异**: 五条目分属两类形态——(a) 消费者应用内功能（Kimi Deep Research、Claude Research、Grok DeepSearch，面向订阅用户）；(b) 面向 agent/开发者的 API 基础设施（Parallel Task API、Azure Foundry Deep Research agent tool）。
3. **定价模式差异**: token 计费（Kimi、Azure o3-deep-research）、请求计费（Parallel）、订阅内额度（Claude、Grok 随 X Premium）。
4. **免费层存在**: Kimi（免费计划有限额度）、Parallel（$5/月免费额度 + 免费 MCP server）；Claude/Grok 无免费（Grok 公告称向全部 Grok 用户以用量限制滚动开放基础能力，Premium+ 优先高级功能）。
5. **官方声称性质**: 全部为厂商自报（含 Parallel 自建基准、Azure 架构描述、Kimi 能力描述），未经本批次独立验证；S013 第三方评测对其中 Grok/Claude/Parallel 有独立实测数据，可作对照（客观标注）。


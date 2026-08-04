---
source_id: S012
source_url: https://docs.gptr.dev
title: GPT Researcher 官方文档（docs.gptr.dev）+ gptr-mcp MCP Server 仓库（github.com/assafelovic/gptr-mcp）
author: assafelovic（GPT Researcher 团队）
date: 2026（文档站点版权年 2026；仓库创建 2025-03-30，最后推送 2025-11-07）
fetched_at: 2026-08-04
content_type: official_doc
---

> 本 raw 为两源合并存档：**源A = docs.gptr.dev 官方文档（Docusaurus 站）**，**源B = github.com/assafelovic/gptr-mcp 仓库（README + GitHub API 元数据）**。各节标注对应 URL。全部内容为官方公开资料，访问日期 2026-08-04。

---

# 源A：docs.gptr.dev 官方文档

## A0. 文档站主页（https://docs.gptr.dev）

- 定位标语："The leading autonomous AI research agent"
- 导航分区：Welcome / Getting Started / GPT Researcher / Frontend / Custom Context / Handling Logs / LLM Providers / Retrievers / Multi-Agent Frameworks / MCP Server / Examples / Contribute / Roadmap / FAQ
- "GPT Researcher is an open source autonomous agent designed for comprehensive online research on a variety of tasks."
- 社区链接：Discord、Twitter、LinkedIn；版权 "Copyright © 2026 GPT Researcher"

## A1. Introduction（https://docs.gptr.dev/docs/gpt-researcher/getting-started/introduction）

- 定位："GPT Researcher is an autonomous agent designed for comprehensive online research on a variety of tasks."
- "The agent can produce detailed, factual and unbiased research reports, with customization options for focusing on relevant resources, outlines, and lessons."
- 方法学来源："Inspired by the recent Plan-and-Solve and RAG papers, GPT Researcher addresses issues of speed, determinism and reliability, offering a more stable performance and increased speed through parallelized agent work, as opposed to synchronous operations."（对应 arXiv:2305.04091 与 arXiv:2005.11401）
- 动机（Why GPT Researcher?）：
  - 人工研究需数周；
  - 现有 LLM 训练数据过时、幻觉风险高；
  - LLM token 输出有限，不足以支撑 2k+ 词长报告；
  - 启用联网的方案（如 ChatGPT + Web Plugin）只考虑有限资源，可能得出肤浅/有偏结论；
  - 只用部分资源会造成结论偏差。
- 架构："The main idea is to run 'planner' and 'execution' agents, whereas the planner generates questions to research, and the execution agents seek the most related information based on each generated research question. Finally, the planner filters and aggregates all related information and creates a research report."
- 模型与成本："The agents leverage both gpt-4o-mini and gpt-4o (128K context) to complete a research task. We optimize for costs using each only when necessary. **The average research task takes around 3 minutes to complete, and costs ~$0.1.**"
- 流程细化：创建领域 agent → 生成一组研究问题 → 对每个问题触发 crawler agent 抓取在线资源 → 对每个抓取资源按相关性摘要并记录来源 → 过滤聚合全部摘要生成最终报告。
- 特性清单：生成 research/outlines/resources/lessons 报告；长报告（over 2K words）；单次聚合 over 20 web sources；内置 web 界面（HTML/CSS/JS）；带 javascript support 的网页抓取；跟踪已访问/已用来源；导出 PDF、Word 等。

## A2. Getting Started（https://docs.gptr.dev/docs/gpt-researcher/getting-started）

- 前置：Python 3.11+。
- 安装：`git clone https://github.com/assafelovic/gpt-researcher.git`；`pip install -r requirements.txt`。
- API Keys：导出或 .env 两种方式；`export OPENAI_API_KEY={...}`、`export TAVILY_API_KEY={...}`；可设 `export OPENAI_BASE_URL={custom}` 使用 OpenAI 兼容 API。
- LLM 推荐："For LLM provider, we recommend OpenAI GPT, but you can use any other LLM model (including open sources)."
- 搜索 API 推荐："For web search API, we recommend Tavily Search API, but you can also refer to other search APIs of your choice by changing the search provider in config/config.py to duckduckgo, google, bing, searchapi, serper, searx and more."
- 运行：`uvicorn main:app --reload`，浏览器访问 http://localhost:8000；支持 venv / Poetry 方式。

## A3. FAQ（https://docs.gptr.dev/docs/faq）

- 定义："GPT Researcher is a popular open source autonomous research agent that takes care of the tedious task of research for you, by scraping, filtering and aggregating over 20+ web sources per a single research task."
- 构建技术："built with best practices for leveraging LLMs (prompt engineering, RAG, chains, embeddings, etc), and is optimized for quick and efficient research. It is also fully customizable."
- **成本（关键数据）**："A research task using GPT Researcher costs around **$0.01 per a single run (for GPT-4 usage)**. We're constantly optimizing LLM calls to reduce costs and improve performance."
- 事实准确性机制："using multiple sources, and by using proprietary AI to score and rank the most relevant and accurate information... use proprietary AI to filter out irrelevant information and sources... by using RAG and other techniques... leading to more accurate generative AI content and reduced hallucinations."
- 未来计划：改进搜索 API（与 design partners 合作）、增加数据源、改进 research agent；Roadmap 在 trello.com/b/3O7KBePw/gpt-researcher-roadmap。

## A4. Configure LLM（https://docs.gptr.dev/docs/gpt-researcher/llms）

- 默认："the default LLM and embedding is OpenAI due to its superior performance and speed."
- 切换方式："you can easily switch between them by updating the SMART_LLM, FAST_LLM and EMBEDDING env variables. You might also need to include the provider API key and corresponding configuration params."（另有 STRATEGIC_LLM 出现在各示例中）
- 支持的 LLMs：openai, anthropic, azure_openai, cohere, google_vertexai, google_genai, fireworks, ollama, together, mistralai, huggingface, groq, bedrock, litellm, minimax。
- 支持的 embeddings：openai, azure_openai, cohere, google_vertexai, google_genai, fireworks, ollama, together, mistralai, huggingface, nomic, voyageai, bedrock。
- **已知限制（官方警告）**："GPT Researcher is optimized and heavily tested on GPT models. Some other models might run into context limit errors, and unexpected responses."
- 示例配置（节选）：
  - OpenAI：`FAST_LLM=openai:gpt-5-mini`、`SMART_LLM=openai:gpt-5`、`STRATEGIC_LLM=openai:o4-mini`、`EMBEDDING=openai:text-embedding-3-small`
  - Custom LLM：`OPENAI_BASE_URL=http://localhost:1234/v1` + `FAST_LLM=openai:{your-llm}`（如 llama.cpp Server）；自定义 embedding 用 `EMBEDDING=custom:{your-embedding}`
  - Azure：`FAST_LLM=azure_openai:gpt-4o-mini`、`SMART_LLM=azure_openai:gpt-4o`、`EMBEDDING=azure_openai:text-embedding-3-large`（要求部署名与模型名一致）
  - Ollama：`OLLAMA_BASE_URL=http://localhost:11434`、`FAST_LLM=ollama:llama3`、`EMBEDDING=ollama:nomic-embed-text`；Granite 家族有定制 prompt：`PROMPT_FAMILY=granite`
  - Groq / Anthropic / Mistral / Together / NetMind / HuggingFace / Gemini / VertexAI / Cohere / Fireworks / Bedrock / LiteLLM / xAI / DeepSeek / Dashscope / Openrouter / Forge / AI/ML API / MiniMax / Avian / vLLM（均有配置示例）
- Avian 示例给出部分模型价格（如 deepseek/deepseek-v3.2 0.26/1M tokens 等）。

## A5. Search Engines / Retrievers（https://docs.gptr.dev/docs/gpt-researcher/search-engines）

- 默认检索器："GPT Researcher defaults to using the Tavily search engine for retrieving search results."
- 切换："specifying the RETRIEVER env var. Please note that each search engine has its own API Key requirements and usage limits."
- 多检索器串联："You can also specify multiple retrievers by separating them with commas. The system will use each specified retriever in sequence. For example: RETRIEVER=tavily, arxiv"
- 已集成检索器清单：Tavily（默认）、Bing、Google、SearchApi、Serp API、Serper、Searx、Duckduckgo、Arxiv、Exa、PubMedCentral。
- 自定义检索器：`RETRIEVER=custom` + `RETRIEVER_ENDPOINT`（端点 URL）+ `RETRIEVER_ARG_*` 前缀参数；响应格式要求为 JSON 数组 `[{"url": "...", "raw_content": "..."}]`。
- Serper 可选配置：SERPER_REGION / SERPER_LANGUAGE / SERPER_TIME_RANGE / SERPER_EXCLUDE_SITES。

## A6. MCP Server Getting Started（https://docs.gptr.dev/docs/gpt-researcher/mcp-server/getting-started）

- 定位："The GPT Researcher MCP Server provides Model Context Protocol (MCP) integration for GPT Researcher, allowing AI assistants to perform autonomous, comprehensive web research and generate reports via the MCP protocol."
- 对比："Standard search tools return raw results requiring manual filtering, often containing irrelevant sources and wasting context window space. GPT Researcher performs autonomous, deep research - not just search... Though slightly slower (30-40 seconds) than standard search, it delivers higher quality information, optimized context, comprehensive results, and better reasoning for LLMs."
- 暴露能力：
  - Resources：`research_resource`（Get web resources related to a given task via research）
  - Primary Tools：`deep_research`（autonomous web research）、`quick_search`（fast web search, speed over quality）、`write_report`（generate report based on research results）、`get_research_sources`、`get_research_context`
  - Prompts：`research_query`
- 前置：Python 3.10+（本页）；OpenAI API key；Tavily API key（或其它搜索 API）。
- 安装：`git clone https://github.com/assafelovic/gptr-mcp.git` → `pip install -r requirements.txt` → `.env`（OPENAI_API_KEY、TAVILY_API_KEY）。
- 运行：`python server.py` 或 `mcp run server.py`。
- 集成 Claude：API Integration（/docs/gpt-researcher/mcp-server/claude-integration）与 Desktop Integration 两种方式。
- 示例（NVIDIA 投资研究）：文档示例中工具名为 `conduct_research`，"this takes 30-40 seconds"。
- Troubleshooting：检查 .env API keys；Python 3.10+；依赖；服务器日志。
- Next Steps：MCP 协议文档（docs.anthropic.com/claude/docs/model-context-protocol）；Advanced Usage 页面。

## A7. MCP Server Advanced Usage（https://docs.gptr.dev/docs/gpt-researcher/mcp-server/advanced-usage）

- 自定义配置（.env）：`STRATEGIC_LLM=openai:gpt-4o-mini`（改默认推理模型）、`MAX_ITERATIONS=2`（减少迭代加速研究）、`SCRAPER=tavily_extract`（生产环境托管抓取）。
- Server 配置文件 `config.json`：host / port / debug / timeout / max_concurrent_requests。
- Claude 集成示例：`{"tools": [{"name": "gptr-researcher", "endpoint": "http://localhost:8000/mcp"}]}`
- 高级工具用法：conduct_research 参数 query/depth/focus_areas/timeline；write_report 参数 style/format/include_images/citation_style/executive_summary。
- 安全：X-API-Key 认证中间件（MCP_API_KEY env）、HTTPS（ssl-keyfile/certfile）、速率限制（slowapi，示例 `@limiter.limit("10/minute")`）。
- Docker 部署：Dockerfile 示例基于 python:3.10-slim，`docker run -p 8000:8000 -e OPENAI_API_KEY=... -e TAVILY_API_KEY=...`
- 扩展：添加新工具（`@app.tool("analyze_sentiment")` 示例）、自定义报告格式、更多数据源、专用研究 agent。
- 故障处理：外部 API 限流重试（tenacity 示例）、大任务内存管理（gc.collect 示例）。

## A8. Retrievers MCP Integration（https://docs.gptr.dev/docs/gpt-researcher/retrievers/mcp-configs）

- 定位："The Model Context Protocol (MCP) enables GPT Researcher to connect with diverse data sources and tools through a standardized interface."
- 集成方式："GPT Researcher features an intelligent two-stage MCP approach that automatically selects the best tools and generates contextual research, powered by LangChain's MCP adapters for seamless integration."
  - Stage 1 Smart Tool Selection：LLM 分析查询与可用 MCP servers，选择最相关工具；
  - Stage 2 Contextual Research：LLM 使用所选工具 + 动态生成的查询特定参数执行研究。
- 启用：`export RETRIEVER=mcp`（纯 MCP）；混合推荐 `export RETRIEVER=tavily,mcp`（也可 google,mcp,arxiv 等组合）。
- 前置：`pip install gpt-researcher`（MCP 依赖自动包含）。
- Quick Start：`GPTResearcher(query=..., mcp_configs=[{name, command, args, env}])` → `await researcher.conduct_research()` → `await researcher.write_report()`。
- mcp_configs 键：name（必填）、command（本地必填*）、args（本地必填*）、env（可选）、connection_url（远程必填**）、connection_type（可选，自动检测 websocket）、connection_token（可选）。"Local servers: Require name, command, and args / Remote servers: Require name and connection_url"。
- 连接类型自动检测：wss:// 前缀→WebSocket；https:// 前缀→HTTP；无 URL→stdio（默认）。
- MCP_STRATEGY：fast（默认，主查询跑一次 MCP）/ deep（所有子查询跑 MCP）/ disabled（跳过 MCP）。
- MCP_AUTO_TOOL_SELECTION=true：多工具服务器自动选择。
- 成本查询 API：`researcher.get_costs()`（示例 "Research cost: ${researcher.get_costs():.4f}"）。
- 故障排查：No retriever specified / Invalid retriever(s) / No MCP server configurations found / MCP server connection failed / No tools available / Tool execution failed。
- 最佳实践：总是设置 RETRIEVER；用混合策略；敏感数据存环境变量；先独立测试 MCP server；debug 模式。

---

# 源B：github.com/assafelovic/gptr-mcp 仓库

## B0. GitHub API 元数据（https://api.github.com/repos/assafelovic/gptr-mcp，2026-08-04 抓取）

- full_name: assafelovic/gptr-mcp；private: false；fork: false
- description: "MCP server for enabling LLM applications to perform deep research via the MCP protocol"
- created_at: 2025-03-30T16:47:15Z；pushed_at: 2025-11-07T07:46:52Z；updated_at: 2026-08-03T13:19:52Z
- stargazers_count: 361；forks_count: 64；watchers_count: 361；open_issues_count: 17；subscribers_count: 3
- language: Python；license: MIT License；homepage: https://gptr.dev；default_branch: master
- topics: deep-research, deepresearch, gpt-researcher, mcp, mcp-server, websearch

## B1. README 定位与对比（https://raw.githubusercontent.com/assafelovic/gptr-mcp/master/README.md）

- 定位："GPT Researcher MCP Server"。
- Why GPT Researcher MCP："While LLM apps can access web search tools with MCP, GPT Researcher MCP delivers deep research results. Standard search tools return raw results requiring manual filtering, often containing irrelevant sources and wasting context window space."
- "GPT Researcher autonomously explores and validates numerous sources, focusing only on relevant, trusted and up-to-date information. Though slightly slower than standard search (~30 seconds wait), it delivers: Higher quality information / Optimized context usage / Comprehensive results / Better reasoning for LLMs"

## B2. README 接口清单

- Resources：`research_resource`（Get web resources related to a given task via research）
- Primary Tools：
  - `deep_research`：Performs deep web research on a topic, finding the most reliable and relevant information
  - `quick_search`：Performs a fast web search optimized for speed over quality, returning search results with snippets. Supports any GPTR supported web retriever such as Tavily, Bing, Google, etc.
  - `write_report`：Generate a report based on research results
  - `get_research_sources`：Get the sources used in the research
  - `get_research_context`：Get the full context of the research
- Prompts：`research_query`（Create a research query prompt）

## B3. README 前置与安装

- "GPT Researcher >=0.12.16 requires Python 3.11+"；Python 3.11 or higher installed。
- API keys：OpenAI API key；Tavily API key；"You can also connect any other web search engines or MCP using GPTR supported retrievers."
- 安装：clone GPT Researcher 仓库 → `cd gptr-mcp` → `pip install -r requirements.txt` → `cp .env.example .env`（OPENAI_API_KEY、TAVILY_API_KEY，"You can also add any other env variable for your GPT Researcher configuration"）。

## B4. README 运行方式与传输模式

- 运行三方式：`python server.py`；`mcp run server.py`；Docker（docker-compose up -d 或 `docker run -d --name gptr-mcp -p 8000:8000 --env-file .env gptr-mcp`）。
- n8n 集成：`docker network connect n8n-mcp-net gptr-mcp`（连接现有 n8n 网络）。
- 传输模式表：
  | Transport | Use Case |
  |---|---|
  | STDIO | Claude Desktop、本地 MCP 客户端，本地开发默认 |
  | SSE | Docker、Web clients、n8n 集成，Docker 中自动启用 |
  | Streamable HTTP | 现代 Web 部署 |
- 自动检测：本地默认 STDIO；Docker 环境自动 SSE；`export MCP_TRANSPORT=sse` 手动覆盖；`DOCKER_CONTAINER=true` 强制 Docker 模式。
- 端点：Health Check `GET /health`；SSE Endpoint `GET /sse`（获取 session ID）；MCP Messages `POST /messages/?session_id=YOUR_SESSION_ID`。
- "The server binds to 0.0.0.0:8000 to work with Docker containers"。
- Best Practices：本地开发用 STDIO；生产用 Docker 自动 SSE；测试用 health 端点；n8n 用容器网络；Web 部署考虑 Streamable HTTP。

## B5. README Claude Desktop 集成

- 配置文件：Mac `~/Library/Application Support/Claude/claude_desktop_config.json`；Windows `%APPDATA%\Claude\claude_desktop_config.json`。
- 关键提示："Claude Desktop launches your MCP server as a separate subprocess, so you must explicitly pass your API keys in the configuration. The server cannot access your shell's environment variables or .env file automatically."
- 安全："Your Claude Desktop config contains sensitive API keys. Protect it: chmod 600 ... Never commit this file to version control." 备选方案：wrapper 脚本 run_gptr_mcp.sh（source .env 后启动 server.py）。

## B6. README 示例（Claude 使用 deep_research 工具）

- NVIDIA 投资研究示例：`[Claude uses deep_research tool - this takes 30-40 seconds]`；返回包含股票表现、产品发布、分析师共识、行业地位等结构化研究结果。
- 注意：README 的示例工具名是 `deep_research`；docs（A6）示例写的是 `conduct_research`。

## B7. README 故障排查与已知问题

- General：API keys 正确性；"Python 3.11 or higher (required by gpt-researcher >=0.14.0)"（此处版本号与前置段 >=0.12.16 不一致）；依赖；日志。
- Docker：容器可访问性（docker ps/logs）、绑定 0.0.0.0:8000。
- n8n：同一 Docker 网络、容器名作 hostname、URL http://gptr-mcp:8000/sse。
- Session ID：先连 /sse 获取 session ID，再用 /messages/?session_id=；每客户端独立 session ID。
- Claude Desktop：绝对路径、env 段必须含 OPENAI_API_KEY 与 TAVILY_API_KEY、重启 Claude。
- License：MIT License；联系：assaf.elovic@gmail.com / Discord。

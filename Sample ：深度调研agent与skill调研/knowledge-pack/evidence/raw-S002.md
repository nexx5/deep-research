---
source_id: S002
source_url: https://github.com/langchain-ai/open_deep_research
title: Open Deep Research (langchain-ai/open_deep_research) — README/官方博客/源码原文存档
author: Lance Martin (LangChain)
date: 2026-08-04
fetched_at: 2026-08-04T09:00:00
content_type: github_repo
---

# 抓取记录

- 任务指定原 URL：https://github.com/OpenDeepResearch/OpenDeepResearch → **404 死链**（GitHub API 确认 org `OpenDeepResearch` 存在但 0 个公开仓库，orgs/repos API 均 404）
- 实际采录替代源：https://github.com/langchain-ai/open_deep_research（生态中承载 "Open Deep Research" 名称的最权威开源实现，Tavily 搜索确认）
- 仓库元数据（GitHub API，2026-08-04）：stars 12,503；forks 1,767；watchers 75；license MIT；created 2024-11-20；updated 2026-08-04；default_branch main；221 commits；39 issues；64 PRs；version 0.0.16（pyproject.toml）
- 抓取页面：
  1. GitHub 仓库主页（README 渲染页）— https://github.com/langchain-ai/open_deep_research
  2. raw README — https://raw.githubusercontent.com/langchain-ai/open_deep_research/main/README.md
  3. 官方架构博客 — https://blog.langchain.com/open-deep-research/（2025-07-16，LangChain Team）
  4. 源码 src/open_deep_research/deep_researcher.py
  5. 源码 src/open_deep_research/configuration.py
  6. 源码 src/open_deep_research/state.py
  7. 源码 src/open_deep_research/prompts.py
  8. 源码 src/open_deep_research/utils.py
  9. pyproject.toml
  10. .env.example

---

# 1. README 全文（raw.githubusercontent.com 抓取）

# 🔬 Open Deep Research

Deep research has broken out as one of the most popular agent applications. This is a simple, configurable, fully open source deep research agent that works across many model providers, search tools, and MCP servers. It's performance is on par with many popular deep research agents ([see Deep Research Bench leaderboard](https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard)).

### 🔥 Recent Updates

**August 14, 2025**: See our free course [here](https://academy.langchain.com/courses/deep-research-with-langgraph) (and course repo [here](https://github.com/langchain-ai/deep_research_from_scratch)) on building open deep research.

**August 7, 2025**: Added GPT-5 and updated the Deep Research Bench evaluation w/ GPT-5 results.

**August 2, 2025**: Achieved #6 ranking on the [Deep Research Bench Leaderboard](https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard) with an overall score of 0.4344.

**July 30, 2025**: Read about the evolution from our original implementations to the current version in our [blog post](https://rlancemartin.github.io/2025/07/30/bitter_lesson/).

**July 16, 2025**: Read more in our [blog](https://blog.langchain.com/open-deep-research/) and watch our [video](https://www.youtube.com/watch?v=agGiWUpxkhg) for a quick overview.

### 🚀 Quickstart

1. Clone the repository and activate a virtual environment:
```bash
git clone https://github.com/langchain-ai/open_deep_research.git
cd open_deep_research
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
2. Install dependencies:
```bash
uv sync
# or
uv pip install -r pyproject.toml
```
3. Set up your `.env` file (model selection, search tools, other config):
```bash
cp .env.example .env
```
4. Launch agent with the LangGraph server locally:
```bash
uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.11 langgraph dev --allow-blocking
```
- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs

### ⚙️ Configurations

#### LLM 🧠

Open Deep Research supports a wide range of LLM providers via the [init_chat_model() API](https://python.langchain.com/docs/how_to/chat_models_universal_init/). It uses LLMs for a few different tasks (fields in configuration.py):

- **Summarization** (default: `openai:gpt-4.1-mini`): Summarizes search API results
- **Research** (default: `openai:gpt-4.1`): Power the search agent
- **Compression** (default: `openai:gpt-4.1`): Compresses research findings
- **Final Report Model** (default: `openai:gpt-4.1`): Write the final report

> Note: the selected model will need to support structured outputs and tool calling.
> Note: For OpenRouter: Follow guide (issue #75) and for local models via Ollama (issue #65).

#### Search API 🔍

Open Deep Research supports a wide range of search tools. By default it uses the [Tavily](https://www.tavily.com/) search API. Has full MCP compatibility and work native web search for Anthropic and OpenAI. See the `search_api` and `mcp_config` fields in configuration.py.

#### Other

See the fields in configuration.py for various other settings to customize the behavior.

### 📊 Evaluation

Open Deep Research is configured for evaluation with [Deep Research Bench](https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard). This benchmark has 100 PhD-level research tasks (50 English, 50 Chinese), crafted by domain experts across 22 fields (e.g., Science & Tech, Business & Finance) to mirror real-world deep-research needs. It has 2 evaluation metrics, but the leaderboard is based on the RACE score. This uses LLM-as-a-judge (Gemini) to evaluate research reports against a golden set of reports compiled by experts across a set of metrics.

#### Usage

> Warning: Running across the 100 examples can cost ~$20-$100 depending on the model selection.

```bash
python tests/run_evaluate.py
python tests/extract_langsmith_data.py --project-name "YOUR_EXPERIMENT_NAME" --model-name "you-model-name" --dataset-name "deep_research_bench"
```
Move the generated JSONL file to a local clone of the Deep Research Bench repository and follow their Quick Start guide for evaluation submission.

#### Results

| Name | Summarization | Research | Compression | Total Cost | Total Tokens | RACE Score |
|------|---------------|----------|-------------|------------|--------------|------------|
| GPT-5 | openai:gpt-4.1-mini | openai:gpt-5 | openai:gpt-4.1 | (未标注) | 204,640,896 | 0.4943 |
| Defaults | openai:gpt-4.1-mini | openai:gpt-4.1 | openai:gpt-4.1 | $45.98 | 58,015,332 | 0.4309 |
| Claude Sonnet 4 | openai:gpt-4.1-mini | anthropic:claude-sonnet-4-20250514 | openai:gpt-4.1 | $187.09 | 138,917,050 | 0.4401 |
| Deep Research Bench Submission | openai:gpt-4.1-nano | openai:gpt-4.1 | openai:gpt-4.1 | $87.83 | 207,005,549 | 0.4344 |

### 🚀 Deployments and Usage

- **LangGraph Studio**: run locally via quickstart.
- **Hosted deployment**: deploy to [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/#deployment-options).
- **Open Agent Platform**: OAP is a UI from which non-technical users can build and configure their own agents. We've deployed Open Deep Research to our public demo instance of OAP (https://oap.langchain.com). You can also deploy your own instance of OAP.

### Legacy Implementations 🏛️

The `src/legacy/` folder contains two earlier implementations. They are less performant than the current implementation, but provide alternative ideas understanding the different approaches to deep research.

#### 1. Workflow Implementation (`legacy/graph.py`)
- **Plan-and-Execute**: Structured workflow with human-in-the-loop planning
- **Sequential Processing**: Creates sections one by one with reflection
- **Interactive Control**: Allows feedback and approval of report plans
- **Quality Focused**: Emphasizes accuracy through iterative refinement

#### 2. Multi-Agent Implementation (`legacy/multi_agent.py`)
- **Supervisor-Researcher Architecture**: Coordinated multi-agent system
- **Parallel Processing**: Multiple researchers work simultaneously
- **Speed Optimized**: Faster report generation through concurrency
- **MCP Support**: Extensive Model Context Protocol integration

---

# 2. 官方架构博客（blog.langchain.com/open-deep-research/，2025-07-16，核心正文）

## TL;DR

Deep research has broken out as one of the most popular agent applications. OpenAI, Anthropic, Perplexity, and Google all have deep research products that produce comprehensive reports. There are also many open source implementations. We've built an open deep researcher that is simple and configurable, allowing users to bring their own models, search tools, and MCP servers. Open deep research is built on LangGraph.

## Challenge

Research is an open‑ended task; the best strategy to answer a user request can't be easily known in advance. Requests can require different research strategies and varying levels of search depth. A key design principle for open deep research is **flexibility** to explore different research strategies depending on the request.

## Architectural Overview

Agents are well suited to research because they can flexibly apply different strategies, using intermediate results to guide their exploration. Open deep research uses an agent to conduct research as part of a three step process:

- **Scope** – clarify research scope
- **Research** – perform research
- **Write** – produce the final report

### Phase 1: Scope

The purpose of scoping is to gather all user-context needed for research. Two-step pipeline: **User Clarification** and **Brief Generation**.

**User Clarification**: OpenAI has made the point that users rarely provide sufficient context in a research request. We use a chat model to ask for additional context if necessary.

**Brief Generation**: The chat interaction can include clarification questions, follow-ups, or user-provided examples. Because the interaction can be quite verbose and token-heavy, we translate it into a comprehensive, yet focused research brief. The research brief serves as our north star for success, and we refer back to it throughout the research and writing phases.

### Phase 2: Research

The goal of research is to gather the context requested by the research brief. We conduct research using a supervisor agent.

**Research Supervisor**: The supervisor has a simple job: delegate research tasks to an appropriate number of sub-agents. The supervisor determines if the research brief can be broken-down into independent sub-topics and delegates to sub-agents with isolated context windows. This allows the system to parallelize research work, finding more information faster.

**Research Sub-Agents**: Each research sub-agent is presented with a sub-topic from the supervisor. The sub-agent is prompted to focus only on a specific topic and doesn't worry about the full scope of research brief. Each sub-agent conducts research as a tool-calling loop, making use of search tools and / or MCP tools configured by the user. When each sub-agent finishes, it makes a final LLM call to write a detailed answer to the subquestion posed, taking into account all of its research and citing helpful sources. If we return raw information to the supervisor, the token usage can bloat significantly; our sub-agent cleans up its findings and returns them to the supervisor.

**Research Supervisor Iteration**: The supervisor reasons about whether the findings from the sub-agents sufficiently address the scope of work in the brief. If the supervisor wants more depth, it can spawn further sub-agents to conduct more research.

### Phase 3: Report Writing

The goal of report writing is to fulfill the request in the research brief using the gathered context from sub-agents. To write the report, we provide an LLM with the research brief and all of the research findings returned by sub-agents. This final LLM call produces an output in one-shot, steered by the brief and answered with the research findings.

## Lessons

### Only use multi-agent for easily parallelized tasks
Cognition has argued against multi-agent because sub-agents working in parallel can be difficult to coordinate. We also learned this lesson. Earlier versions of our research agent wrote sections of the final report in parallel with sub-agents. It was fast, but we faced a problem: the reports were disjoint because the section-writing agents were not well coordinated. We resolved this by using multi-agent for only the research task itself, performing writing after all research was done.

### Multi-agent is useful for isolating context across sub-research topics
Our experiments showed that single agent response quality suffers if the request has multiple sub-topics. The intuition: a single context window needs to store and reason about tool feedback across all of the sub-topics. This tool feedback is often token heavy. Numerous failure modes, such as context clash, become prevalent as the context window accumulates tool calls across many different sub-topics. A multi-agent approach allows multiple sub-agents to run in parallel, each dedicated to an independent, focused task; sub-topic context can be isolated in each sub-agent.

### Multi-agent supervisor enables the system to tune to required research depth
Users do not want simple requests to take 10+ minutes. But some requests require research with higher token utilization and latency. The supervisor can handle both cases by selectively spawning sub-agents to tune the level of research depth needed for a request.

### Context Engineering is important to mitigate token bloat and steer behavior
Research is a token-heavy task. Anthropic reported that their multi-agent system used 15x more tokens than a typical chat application! We used context engineering to mitigate this. We compress the chat history into a research brief, which prevents token-bloat from prior messages. Sub-agents prune their research findings to remove irrelevant tokens and information before returning to the supervisor. Without sufficient context engineering, our agent was prone to running into context window limits from long, raw tool-call results. Practically, it also helps save $ on token spend and helps avoid TPM model rate limits.

## Next Steps (open questions)

- What is the best way to handle token-heavy tool responses, and filter out irrelevant context?
- Are there any evaluations worth running in the hot path of the agent to ensure high quality responses?
- Deep research reports are valuable and relatively expensive to create, can we store this work and leverage these in the future with long-term memory?

---

# 3. 源码摘录：deep_researcher.py（主图结构）

主图（AgentState, input=AgentInputState, config_schema=Configuration）：
- 节点：clarify_with_user → write_research_brief → research_supervisor（supervisor 子图）→ final_report_generation → END
- 边：START→clarify_with_user；research_supervisor→final_report_generation；final_report_generation→END

clarify_with_user：若 configuration.allow_clarification=False 则跳过；用 research_model 结构化输出 ClarifyWithUser（need_clarification/question/verification）；需要澄清则 goto END 返回问题，否则 goto write_research_brief。

write_research_brief：用 research_model 结构化输出 ResearchQuestion（research_brief），初始化 supervisor_messages（lead_researcher_prompt + research_brief），goto research_supervisor。

supervisor（SupervisorState）：绑定工具 [ConductResearch, ResearchComplete, think_tool]；research_iterations+1；goto supervisor_tools。

supervisor_tools：
- 退出条件：research_iterations > max_researcher_iterations，或无 tool_calls，或含 ResearchComplete → goto END（提取 notes）
- think_tool 调用：记录 reflection
- ConductResearch 调用：只取前 max_concurrent_research_units 个并发执行（asyncio.gather 并行 researcher_subgraph），overflow 调用返回错误 ToolMessage
- 聚合 raw_notes；异常时（token 超限或其它）直接结束研究阶段

researcher（ResearcherState）：get_all_tools 获取工具（搜索/MCP/think_tool），无工具则 ValueError；绑定工具循环；tool_call_iterations+1；goto researcher_tools。

researcher_tools：
- 无 tool_calls 且无 native web search（openai/anthropic 检测）→ goto compress_research
- 并行执行所有工具调用（execute_tool_safely 包裹错误）
- 退出条件：tool_call_iterations >= max_react_tool_calls 或含 ResearchComplete → goto compress_research
- 否则继续 researcher 循环

compress_research：compression_model 压缩 findings（最多 3 次尝试；token 超限则 remove_up_to_last_ai_message 截断重试）；输出 compressed_research + raw_notes；goto END。

researcher_subgraph：researcher → researcher_tools → compress_research → END（可被 supervisor 并行 ainvoke）。

final_report_generation：final_report_model 一次生成；用 research_brief + messages + findings（notes join）；token 超限时按 model_token_limit*4 截断 findings，最多 4 次尝试（每次 -10%）；成功返回 final_report + messages。

# 4. 源码摘录：configuration.py（配置项）

- SearchAPI 枚举：ANTHROPIC / OPENAI / TAVILY / NONE
- MCPConfig：url / tools / auth_required
- max_structured_output_retries: 3（1-10）
- allow_clarification: True（默认允许向用户追问）
- max_concurrent_research_units: 5（1-20）— 并发子 agent 上限
- search_api: SearchAPI.TAVILY（默认 Tavily）
- max_researcher_iterations: 6（1-10）— supervisor 反思/追问轮数上限
- max_react_tool_calls: 10（1-30）— 单个 researcher 工具调用迭代上限
- summarization_model: openai:gpt-4.1-mini / max_tokens 8192
- max_content_length: 50000（网页内容摘要前字符上限，1000-200000）
- research_model: openai:gpt-4.1 / max_tokens 10000
- compression_model: openai:gpt-4.1 / max_tokens 8192
- final_report_model: openai:gpt-4.1 / max_tokens 10000
- mcp_config / mcp_prompt
- from_runnable_config 支持从环境变量或 configurable 读取

# 5. 源码摘录：state.py

- ConductResearch（结构化输出）：research_topic（单一主题，至少一段高细节描述）
- ResearchComplete（结构化输出）：研究完成标记
- ClarifyWithUser：need_clarification / question / verification
- ResearchQuestion：research_brief
- AgentState：messages + supervisor_messages + research_brief + raw_notes + notes + final_report（override_reducer）
- SupervisorState：supervisor_messages + research_brief + notes + research_iterations + raw_notes
- ResearcherState：researcher_messages + tool_call_iterations + research_topic + compressed_research + raw_notes

# 6. 源码摘录：prompts.py（提示词要点）

- clarify_with_user_instructions：判断是否需要追问；已有澄清问题则几乎不再问；要求 JSON 输出
- transform_messages_into_research_topic_prompt：对话→research brief；最大化具体性；不臆造假设；优先官方/一手来源（产品/旅行→官网，学术→原论文，人物→LinkedIn/个人网站）；查询语言匹配来源语言
- lead_researcher_prompt（supervisor）：think_tool 先规划后反思；偏向单 agent（除非明显可并行）；比较型问题每个比较对象一个 sub-agent；最多 max_researcher_iterations 次 ConductResearch；每次最多 max_concurrent_research_units 个并行
- research_system_prompt（researcher）：工具循环；简单查询 2-3 次搜索、复杂查询最多 5 次；3+ 相关来源即停；think_tool 每次搜索后反思
- compress_research_system_prompt：清理 findings 但逐字保留所有相关信息；内联引用编号；Sources 段列出全部来源；"A later LLM will be used to merge this report with others, so having all of the sources is critical."
- final_report_generation_prompt：one-shot 生成；必须与用户消息同语言；[Title](URL) 引用格式；Sources 段；禁止自称作者；段落形式为主
- summarize_webpage_prompt：网页内容摘要（约原长 25-30%），保留关键事实/统计/引用；JSON 输出 summary + key_excerpts（最多 5 条）

# 7. 源码摘录：utils.py（工具与机制）

- tavily_search：多查询并行（asyncio.gather）；max_results=5；topic general/news/finance；include_raw_content=True；URL 去重；每个结果用 summarization_model 摘要（60s 超时，失败回退原文）；输出格式 "--- SOURCE {i}: {title} --- URL ... SUMMARY ..."
- think_tool：反思工具（记录反思文本）
- get_search_tool：ANTHROPIC → {"type":"web_search_20250305","max_uses":5}；OPENAI → {"type":"web_search_preview"}；TAVILY → tavily_search
- load_mcp_tools：MultiServerMCPClient（streamable_http transport）；OAuth token exchange（Supabase token → MCP token）；工具名冲突跳过；只加载 mcp_config.tools 指定工具；wrap_mcp_authenticate_tool 处理 MCP 认证错误（-32003 需交互）
- get_all_tools：ResearchComplete + think_tool + 搜索工具 + MCP 工具
- is_token_limit_exceeded：OpenAI/Anthropic/Gemini 提供商标识；MODEL_TOKEN_LIMITS 表（gpt-4.1 系列 1047576、gemini-1.5-pro 2097152、claude 200000 等）
- remove_up_to_last_ai_message：token 超限时截断
- get_api_key_for_model：GET_API_KEYS_FROM_CONFIG=false 时从环境变量读（OPENAI_API_KEY/ANTHROPIC_API_KEY/GOOGLE_API_KEY）；true 时从 config apiKeys 读
- anthropic_websearch_called / openai_websearch_called：检测 native web search 使用

# 8. pyproject.toml

- name: open_deep_research; version 0.0.16; description "Planning, research, and report generation."
- authors: Lance Martin; license MIT; requires-python >=3.10
- 依赖：langgraph>=0.5.4, langchain-community, langchain-openai, langchain-anthropic, langchain-mcp-adapters>=0.1.6, langchain-deepseek, langchain-tavily, langchain-groq, openai, tavily-python, arxiv, pymupdf, xmltodict, linkup-sdk, duckduckgo-search, exa-py, requests, beautifulsoup4, python-dotenv, pytest, httpx, markdownify, azure-identity, azure-search, azure-search-documents, rich, langgraph-cli[inmem], langsmith, langchain-google-vertexai, langchain-google-genai, ipykernel, supabase, mcp>=1.9.4, langchain-aws, pandas

# 9. .env.example

OPENAI_API_KEY=
ANTHROPIC_API_KEY=
GOOGLE_API_KEY=
TAVILY_API_KEY=
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=
LANGSMITH_TRACING=
# Only necessary for Open Agent Platform
SUPABASE_KEY=
SUPABASE_URL=
# Should be set to true for a production deployment on Open Agent Platform. Should be set to false otherwise, such as for local development.
GET_API_KEYS_FROM_CONFIG=false

# 10. 搜索补充确认（Tavily 搜索结果，2026-08-04）

- github.com/nickscamara/open-deep-research：OpenAI Deep Research 的开源克隆，使用 Firecrawl extract+search 配合推理模型（"An Open-Source clone of Open AI's Deep Research experiment"）
- github.com/dzhng/deep-research：最简实现 deep research agent（"the simplest implementation of a deep research agent"）
- pypi.org/project/open-deep-research：PyPI 包（0.0.15/0.0.16 等版本，"Planning, research, and report generation."）
- www.opendeepresearch.dev：Open Deep Research 官网（"Powered by Together AI"）
- www.together.ai/blog/open-deep-research：Together AI 博客（"LLM agent workflow that can answer complex multi-hop questions and simultaneously write long-form research reports"）
- huggingface.co/blog/open-deep-research：HuggingFace 博客 "Open-source DeepResearch – Freeing our search agents"（评论区有用户报告本地运行 run.py 报错、缺 README 安装说明）
- langchain.com/blog/open-deep-research：LangChain 博客（与 #2 同源）

---

# 独立验证说明

- 官方声称 vs 独立验证分开记录：RACE 分数、成本数据来自官方 README 自提交评测实验（官方声明）；性能"on par with many popular deep research agents"为官方声称，未经本项目独立复测
- 仓库活跃度（12.5k stars / 221 commits / 39 open issues）为 GitHub API 独立可验证数据
- 许可证 MIT、版本 0.0.16 为 pyproject.toml 与 GitHub API 交叉验证

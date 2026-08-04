---
source_id: S026
source_url: https://docs.langchain.com/oss/python/deepagents/deep-research + https://developers.llamaindex.ai/python/framework/use_cases/agents
title: Agent框架内置Deep Research能力：LangChain Deep Agents文档 + LlamaIndex agents文档（官方文档合并采录）
fetched_at: 2026-08-04T12:00:00
content_type: official_doc
search_channel: Tavily API (socks5://127.0.0.1:4040) + webfetch 直抓
---

# S026 原始存档：LangChain / LlamaIndex 官方文档 Deep Research 能力

> 两框架官方文档合并为一份 raw，分节标注各 URL。访问日期：2026-08-04。
> 获取方式：Tavily 搜索定位 → webfetch 直抓官方文档页（docs.langchain.com / developers.llamaindex.ai 均可直连）。
> 以下为抓取到的关键原文段落（markdown 化后存档）。

---

## 节A：LangChain Deep Agents - Build a deep research agent

URL: https://docs.langchain.com/oss/python/deepagents/deep-research

### 原文摘录（标题/概述）

> # Build a deep research agent
> Build a multi-step web research agent with subagent delegation
>
> ## Overview
> This guide demonstrates how to build a multi-step web research agent from scratch using [Deep Agents](/oss/python/deepagents). The agent decomposes research questions into focused tasks, delegates them to specialized sub-agents, and synthesizes findings into a comprehensive report.
>
> The agent you build will:
> 1. Plan research using the opt-in todo list middleware
> 2. Delegate focused research tasks to sub-agents with isolated context
> 3. Assess search results and plan next steps as you gather information
> 4. Synthesize findings with proper citations into a final report
>
> The spawned sub-agents will conduct web searches with Tavily, fetching full webpage content for analysis.

### 原文摘录（Key concepts / Prerequisites）

> ### Key concepts
> This tutorial covers:
> * Subagents for parallel, context-isolated research
> * Custom tools for web search
> * Multi-step planning with the opt-in planning tool
>
> ### Prerequisites
> API keys for:
> * Anthropic (Claude) or Google (Gemini)
> * Tavily for web search (optional - free tier sufficient)
> * LangSmith for tracing (optional)

### 原文摘录（依赖安装）

> ```bash
> pip install deepagents tavily-python httpx markdownify langchain-anthropic langchain-core
> ```
> (或 langchain-google-genai 变体)

### 原文摘录（tavily_search 工具定义）

> The `tavily_search` tool uses Tavily for URL discovery, then fetches full webpage content so the agent can analyze complete sources instead of summaries.
> ```python
> tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
> def fetch_webpage_content(url: str, timeout: float = 10.0) -> str:
>     """Fetch webpage and convert HTML to markdown."""
>     # httpx.get + markdownify
> @tool(parse_docstring=True)
> def tavily_search(query: str, ...) -> str:
>     """Search the web for information on a given query. Uses Tavily to discover relevant URLs, then fetches and returns full webpage content as markdown."""
> ```

### 原文摘录（workflow 指令：委派策略与限制）

> ## Research Workflow
> 1. Plan: Create a todo list with write_todos ...
> 3. Research: Delegate research tasks to sub-agents using the task() tool - ALWAYS use sub-agents for research, never conduct research yourself
> 4. Synthesize: Review all sub-agent findings and consolidate citations (each unique URL gets one number across all findings)
> 5. Write Report: Write a comprehensive final report to `/final_report.md`
> 6. Verify: Read `/research_request.md` and confirm you've addressed all aspects ...
>
> ## Sub-Agent Research Coordination
> - DEFAULT: Start with 1 sub-agent for most queries
> - ONLY parallelize when the query EXPLICITLY requires comparison or has clearly independent aspects
> - Parallel Execution Limits: Use at most {max_concurrent_research_units} parallel sub-agents per iteration
> - Research Limits: Stop after {max_researcher_iterations} delegation rounds if you haven't found adequate sources

### 原文摘录（agent 创建代码）

> ```python
> from deepagents import create_deep_agent
> from langchain.agents.middleware import TodoListMiddleware
> research_sub_agent = {
>     "name": "research-agent",
>     "description": "Delegate research to the sub-agent. Give one topic at a time.",
>     "system_prompt": RESEARCHER_INSTRUCTIONS.format(date=current_date),
>     "tools": [tavily_search],
> }
> model = init_chat_model(model="anthropic:claude-sonnet-4-5-20250929", temperature=0.0)
> agent = create_deep_agent(
>     model=model,
>     tools=[tavily_search],
>     system_prompt=INSTRUCTIONS,
>     subagents=[research_sub_agent],
>     middleware=[TodoListMiddleware()],
> )
> ```
> (Gemini 变体：model="gemini-3-pro-preview" / ChatGoogleGenerativeAI)

### 原文摘录（运行方式）

> You can run the agent synchronously ... or you can stream updates as they come in.
> If you set the LANGSMITH_API_KEY environment variable before running, you can view the agent's traces in LangSmith ...
> Full code: https://github.com/langchain-ai/deepagents/tree/main/examples/deep_research

### 官方文档声称（营销性）

> 无重大未验证性能声称；本页为教程页，主要为能力介绍。

---

## 节B：LangChain Deep Agents overview（框架定位）

URL: https://docs.langchain.com/oss/python/deepagents/overview

### 原文摘录

> # Deep Agents overview
> Build agents that can plan, use subagents, and leverage file systems for complex tasks
>
> Deep Agents is the easiest way to start building agents and applications that are powered by LLMs—with built-in capabilities for file systems for context management, subagent-spawning, and long-term memory.
> Optional capabilities such as task planning and skills extend the harness when your use case needs them.

### 原文摘录（deepagents 与 LangChain/LangGraph 的关系）

> `deepagents` is a standalone library built on top of LangChain's core building blocks for agents. It uses the LangGraph runtime for durable execution, streaming, human-in-the-loop, and other features.
> LangChain is the framework that provides the core building blocks for your agents.
> For building custom agents without these built-in capabilities, consider using LangChain's `create_agent` or building a custom LangGraph workflow.

### 原文摘录（核心能力分类）

> ## Execution environment: Tools, virtual filesystem, optional sandbox, and REPL (interpreter)
> ## Context management: Skills, memory, summarization, context offloading, and prompt caching
> ## Delegation: Subagent spawning and optional task planning
> ## Steering: Human-in-the-loop approval and interrupts
>
> ### Task planning
> Task planning is an opt-in harness capability that lets agents maintain a structured task list during execution.
> Starting in v0.7 task planning is opt-in only. In earlier versions, task planning middleware was included by default.
> Pass TodoListMiddleware to the middleware parameter to give the agent a write_todos tool ...

### 原文摘录（工具与 MCP）

> Pass custom functions, LangChain tools, or tools from any MCP server with the `tools=` parameter. Deep Agents fully support the Model Context Protocol (MCP) ...

### 原文摘录（虚拟文件系统）

> The harness provides a configurable virtual filesystem which can be backed by different pluggable backends: in-memory state, local disk, LangGraph store, composite routing, or a custom backend with permission rules ...
> | Tool: ls | read_file | write_file | edit_file | delete | glob | grep | execute |
> (execute 仅在 sandbox backends 可用)

### 原文摘录（subagents）

> The harness includes a built-in `task` tool that lets the main agent create ephemeral subagents for isolated, long-running, multi-step, or parallel tasks.
> Subagent execution provides: Fresh context, Autonomous execution, Single handoff, Configurable strategy, Stateless messaging, Context and token efficiency.

### 官方文档声称（营销性）

> "Deep Agents is the easiest way to start building agents..."——定位陈述，非性能验证。

---

## 节C：LangChain Deep Agents 产品页 + GitHub（开放度）

URL: https://www.langchain.com/deep-agents / https://github.com/langchain-ai/deepagents

### 产品页原文摘录

> # Build agents for complex, multi-step tasks
> Deep Agents is an open source agent harness built for long-running tasks. It handles planning, context management, and multi-agent orchestration for complex work like research and coding.
> - Break down complex objectives: Planning tools let agents decompose tasks ...
> - Delegate work in parallel: Spawn subagents for independent subtasks, each with isolated context
> - Persist knowledge across sessions: Virtual filesystem stores system prompts, skills, and long-term memory
> Deep Agents is available as an SDK and CLI ...

### GitHub 原文摘录（许可证/star/定位）

> langchain-ai/deepagents — "The batteries-included agent harness."
> - MIT license（仓库 LICENSE 标识 + PyPI License badge 指向 opensource.org/licenses/MIT）
> - Stars: 27.3k / Forks: 3.8k
> - Features: Sub-agents, Filesystem, Context management, Shell access, Persistent memory, Human-in-the-loop, Skills, Tools (own functions or any MCP server)
> - Deep Agents available as JavaScript/TypeScript library — deepagents.js
> - Inspired by Claude Code: an attempt to identify what makes it general-purpose, and push that further.
> - Security: Deep Agents follows a "trust the LLM" model. Enforce boundaries at the tool/sandbox level.

### 官方声称

> "Production-ready — built on LangGraph (streaming, persistence, checkpointing) with first-class tracing, evaluation, and deployment via LangSmith"——官方定位声称。

---

## 节D：LlamaIndex agents 官方文档（Use Cases）

URL: https://developers.llamaindex.ai/python/framework/use_cases/agents

### 原文摘录

> # Agents
> An "agent" is an automated reasoning and decision engine. It takes in a user input/query and can make internal decisions for executing that query in order to return the correct result. The key agent components can include, but are not limited to:
> - Breaking down a complex question into smaller ones
> - Choosing an external Tool to use + coming up with parameters for calling the Tool
> - Planning out a set of tasks
> - Storing previously completed tasks in a memory module
>
> LlamaIndex provides a comprehensive framework for building agentic systems with varying degrees of complexity:
> - If you want to build agents quickly: Use our prebuilt agent and tool architectures ...
> - If you want full control over your agentic system: Build and deploy custom agentic workflows from scratch using our Workflows ...

### 原文摘录（Use Cases 中的研究相关）

> ## Use Cases
> - Agentic RAG: Build a context-augmented research assistant over your data that not only answers simple questions, but complex research tasks.
> - Report Generation: Generate a multimodal report using a multi-agent researcher + writer workflow + LlamaParse.
> - Customer Support: starter template for building a multi-agent concierge with workflows.
>
> ## Ecosystem
> - Community-Built Agents: We offer a collection of 40+ agent tools for use with your agent in LlamaHub.

### 官方声称

> 未发现"内置 deep research 专用产品"的陈述；本页将 deep research 描述为 agentic RAG / report generation 用例，通过 Workflows 自建。

---

## 节E：LlamaIndex Multi-agent patterns（research→write→review 模式）

URL: https://developers.llamaindex.ai/python/framework/understanding/agent/multi_agent

### 原文摘录

> When more than one specialist is required to solve a task you have several options in LlamaIndex, each trading off convenience for flexibility. This page walks through the three most common patterns:
>
> Pattern 1 – AgentWorkflow (i.e. linear "swarm" pattern) — built-in; declare a set of agents and let AgentWorkflow manage the hand-offs.
> Pattern 2 – Orchestrator agent (sub-agents as tools) — built-in; an "orchestrator" agent chooses which sub-agent to call next; those sub-agents are exposed to it as tools.
> Pattern 3 – Custom planner (DIY) — you write the LLM prompt (often XML / JSON) that plans the sequence yourself and imperatively invoke the agents in code.
>
> 示例：Three agents collaborate to research, write and review a report.
> research_agent = FunctionAgent(name="ResearchAgent", description="Search the web and record notes.", tools=[search_web, record_notes], can_handoff_to=["WriteAgent"])
> write_agent = FunctionAgent(name="WriteAgent", ...)
> review_agent = FunctionAgent(name="ReviewAgent", ...)
> agent_workflow = AgentWorkflow(agents=[research_agent, write_agent, review_agent], root_agent=research_agent.name, ...)
> resp = await agent_workflow.run(user_msg="Write me a report on the history of the web …")

### 官方声称

> 该页明确以 research→write→review 报告生成为示例展示 LlamaIndex 多 agent 能力，但定位为"模式/模式代码"而非"内置 deep research 产品"。

---

## 节F：LlamaIndex 文档全站搜索 "deep research"（未命中验证）

URL: https://developers.llamaindex.ai/api/search?q=deep%20research （文档自带 BM25 搜索 API）

### 返回结果（top 10 标题）

1. CometAPI（第三方 LLM 集成页，excerpt 提及 GPT/Claude/Gemini）
2. Perplexity（LLM 集成页，excerpt："Perplexity's Sonar API offers a solution that combines real-time, grounded web search with advanced reasoning and deep research capabilities"）
3. Activeloop Deep Memory（retriever 集成）
4. Deep Lake Vector Store（vector store 集成）
5. You.com Retriever（retriever 集成）
6. MistralAI（LLM 集成）
7. Lindorm（vector store）
8. Chroma + Fireworks + Nomic（示例）
9. ChangeLog（2026-03-16 条目）
10. Multi-agent patterns in LlamaIndex（详见节E）

### 结论（如实记录）

- LlamaIndex 官方文档全站 BM25 搜索 "deep research" **未命中任何名为 "deep research" 的专用功能文档页**。
- 命中的 deep research 相关内容均为：①第三方 LLM/检索服务集成页的附带描述（Perplexity Sonar、You.com 等）；②multi-agent patterns 页（作为构建 deep research 系统的模式指南）。
- 因此："LlamaIndex 内置 deep research 专用能力"在本次搜索范围内**未发现**（搜索范围：developers.llamaindex.ai BM25 全站搜索 + agents use cases + multi-agent patterns 深读；未覆盖全部教程/notebook 页面）。

---

## 节G：Tavily 搜索结果辅助（定位来源，非正文）

- 搜索词 "LangChain deep research agent official documentation" 首位官方结果即 docs.langchain.com/oss/python/deepagents/deep-research。
- 搜索词 "LlamaIndex deep research agent" 未返回任何 developers.llamaindex.ai 官方 deep research 页，官方相关仅 developers.llamaindex.ai/.../use_cases/agents（agents 总览）。返回的多为第三方教程（YouTube Laurie Voss、DataCamp webinar、Dev.to、Medium、Maven 课程、Colab notebook）与第三方复刻仓库（github.com/Davy-hou/open_deep_research_llamaIndex）。
- 说明：第三方 deep research 教程存在（如 LlamaIndex 官方人员 Laurie Voss 的 "Building a Deep Research AI Multi-Agent with LlamaIndex" webinar），但那是教学视频，不属于官方文档内置能力页。

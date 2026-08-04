---
source_id: S038
source_url: "https://arxiv.org/abs/2601.09688 ; https://github.com/openai/openai-agents-python ; https://github.com/microsoft/agent-framework ; https://github.com/bytedance/deer-flow ; https://arxiv.org/abs/2504.21776"
title: "多源合并：DeepResearchEval 评测框架（arXiv:2601.09688）+ OpenAI Agents SDK / Microsoft Agent Framework（框架继任者）+ DeerFlow / WebThinker（深度调研系统对照）"
fetched_at: 2026-08-04T10:00:00
content_type: mixed (paper + github README)
access_date: 2026-08-04
---

# raw 原文存档：S038（五源分节）

> 获取渠道：多源搜索 skill——arXiv API（export.arxiv.org）学术引擎取摘要；GitHub API（api.github.com）取仓库 README 与元数据。各源 URL 均由任务指令明确给定，非猜测。
> 摘要为 arXiv Atom XML 原文；README 为 GitHub 官方仓库一手内容（deer-flow README 全长 97KB，raw 仅保留概览级关键段落，其余引用官方 URL）。

---

## 源A：DeepResearchEval（arXiv:2601.09688）——论文摘要级

### 元数据
- 标题（原文）：DeepResearchEval: An Automated Framework for Deep Research Task Construction and Agentic Evaluation
- 作者（原文）：Yibo Wang, Lei Wang, Yue Deng, Keming Wu, Yao Xiao, Huanjin Yao, Liwei Kang, Hai Ye, Yongcheng Jing, Lidong Bing
- arXiv ID：2601.09688，版本 v1（published 2026-01-14T18:38:31Z）
- 主分类：cs.CL
- 代码（论文 arxiv:comment 声明）：https://github.com/Infinity-AILab/DeepResearchEval
- 摘要页：https://arxiv.org/abs/2601.09688v1

### 摘要（英文原文，一字未改）
Deep research systems are widely used for multi-step web research, analysis, and cross-source synthesis, yet their evaluation remains challenging. Existing benchmarks often require annotation-intensive task construction, rely on static evaluation dimensions, or fail to reliably verify facts when citations are missing. To bridge these gaps, we introduce DeepResearchEval, an automated framework for deep research task construction and agentic evaluation. For task construction, we propose a persona-driven pipeline generating realistic, complex research tasks anchored in diverse user profiles, applying a two-stage filter Task Qualification and Search Necessity to retain only tasks requiring multi-source evidence integration and external retrieval. For evaluation, we propose an agentic pipeline with two components: an Adaptive Point-wise Quality Evaluation that dynamically derives task-specific evaluation dimensions, criteria, and weights conditioned on each generated task, and an Active Fact-Checking that autonomously extracts and verifies report statements via web search, even when citations are missing.

---

## 源B1：OpenAI Agents SDK（github.com/openai/openai-agents-python）——README 概览级

### 元数据（GitHub API）
- 描述：A lightweight, powerful framework for multi-agent workflows
- 创建：2025-03-11；语言：Python；许可证：MIT
- stars 28,376 / forks 4,440（2026-08-04 快照）
- 文档：https://openai.github.io/openai-agents-python/ ；JS/TS 版：github.com/openai/openai-agents-js（README 提及）

### README 关键原文（英文）
- 定位："The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent workflows. It is provider-agnostic, supporting the OpenAI Responses and Chat Completions APIs, as well as 100+ other LLMs."
- 核心概念清单（README 原列）：Agents（LLMs configured with instructions, tools, guardrails, and handoffs）；Sandbox agents（Agents preconfigured to work with a container to perform work over long time horizons）；Realtime agents；Voice agents；Agents as tools / Handoffs（Delegating to other agents for specific tasks）；Tools（functions, MCP, hosted tools）；Guardrails；Human in the loop；Sessions（Automatic conversation history management across agent runs）；Tracing（Built-in tracking of agent runs）
- 运行方式：text agent / sandbox agent / realtime agent / voice agent 四种；需要 Python 3.10+
- 依赖生态：Pydantic、Requests、MCP Python SDK、Griffe；可选 any-llm / LiteLLM
- 注：README 未提及 Swarm；README 未提及内置 deep research 工作流

---

## 源B2：Microsoft Agent Framework（github.com/microsoft/agent-framework）——README 概览级

### 元数据（GitHub API）
- 描述：A framework for building, orchestrating and deploying AI agents and multi-agent workflows with support for Python and .NET.
- 创建：2025-04-28；语言：Python；许可证：MIT
- stars 12,588 / forks 2,107（2026-08-04 快照）
- 文档：https://learn.microsoft.com/agent-framework/ ；https://aka.ms/agent-framework

### README 关键原文（英文）
- 定位："Microsoft Agent Framework (MAF) is an open, multi-language framework for building production-grade AI agents and multi-agent workflows in .NET and Python."；"built for teams taking agents from prototype to production... supports a broad ecosystem including Microsoft Foundry, Azure OpenAI, OpenAI, and the GitHub Copilot SDK"
- Key Features（README 原列）：Python and C#/.NET Support；Multiple Agent Provider Support；Middleware；Orchestration Patterns & Workflows（"graph-based workflows supporting sequential, concurrent, handoff, and group collaboration patterns; includes checkpointing, streaming, human-in-the-loop, and time-travel"）；Foundry Hosted Agents (new)；Observability（OpenTelemetry）；Declarative Agents（YAML）；Agent Skills（"Build domain-specific knowledge bases from multiple sources—files, inline code, class libraries—for agents to discover and use"）；AF Labs（"Experimental packages for cutting-edge features including benchmarking, reinforcement learning"）；DevUI
- 迁移指南（README 明确列出）："Migration from Semantic Kernel"；"Migration from AutoGen"（learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen）
- Important Notes（README 原文）："If you use Microsoft Agent Framework to build applications that operate with any third-party servers, agents, code, or non-Azure Direct models ('Third-Party Systems'), you do so at your own risk."

---

## 源C1：DeerFlow（github.com/bytedance/deer-flow）——README 概览级

> 官方仓库名称为小写连字符 deer-flow（非 DeerFlow）；任务给定 URL bytedance/DeerFlow 404，经 GitHub 搜索定位为 bytedance/deer-flow。

### 元数据（GitHub API）
- 描述：An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.
- 创建：2025-05-07；语言：Python；许可证：MIT；官网 https://deerflow.tech
- stars 79,245 / forks 10,821（2026-08-04 快照）
- topics（官方标注）：agent, deep-research, harness, langchain, langgraph, superagent, multi-agent 等

### README 关键原文（英文，概览级）
- 定义："DeerFlow (Deep Exploration and Efficient Research Flow) is an open-source super agent harness that orchestrates sub-agents, memory, and sandboxes to do almost anything — powered by extensible skills."
- 2.0 重写："DeerFlow 2.0 is a ground-up rewrite. It shares no code with v1. If you're looking for the original Deep Research framework, it's maintained on the 1.x branch... Active development has moved to 2.0."
- Trending："On February 28th, 2026, DeerFlow claimed the #1 spot on GitHub Trending following the launch of version 2."
- 转型陈述（From Deep Research to Super Agent Harness）："DeerFlow started as a Deep Research framework — and the community ran with it... developers have pushed it far beyond research: building data pipelines, generating slide decks, spinning up dashboards, automating content workflows."；"DeerFlow wasn't just a research tool. It was a harness — a runtime that gives agents the infrastructure to actually get work done."；"DeerFlow 2.0 is no longer a framework you wire together. It's a super agent harness — batteries included, fully extensible. Built on LangGraph and LangChain, it ships with everything an agent needs out of the box: a filesystem, memory, skills, sandbox-aware execution, and the ability to plan and spawn sub-agents for complex, multi-step tasks."
- Skills："A standard Agent Skill is a structured capability module — a Markdown file that defines a workflow, best practices, and references to supporting resources. DeerFlow ships with built-in skills for research, report generation, slide creation, web pages, image and video generation, and more."；"Skills are loaded progressively — only when the task needs them, not all at once."
- Sandbox："Each task gets its own execution environment with a full filesystem view — skills, workspace, uploads, outputs."；支持 Local Execution / Docker Execution / Docker with Kubernetes 三种模式
- Context Engineering："Each sub-agent runs in its own isolated context... will not be able to see the context of the main agent or other sub-agents."；"DeerFlow manages context aggressively — summarizing completed sub-tasks, offloading intermediate results to the filesystem, compressing what's no longer immediately relevant."
- Long-Term Memory："DeerMem remains the default local backend. An opt-in mem0 backend is also available."；"Across sessions, DeerFlow builds a persistent memory of your profile, preferences, and accumulated knowledge."；另有可选 OpenViking 后端（README 提及）
- Sub-Agents："Sub-agents are an optimization, not the default response to a complex request."；"The lead agent can spawn sub-agents on the fly — each with its own scoped context, tools, and termination conditions... Sub-agents report back structured results, and the lead agent verifies and synthesizes them into a coherent output."
- InfoQuest：README 称 DeerFlow 集成 BytePlus 自研智能搜索与抓取工具集 InfoQuest
- 推荐模型（README 原文）：Doubao-Seed-2.0-Code, DeepSeek v3.2, Kimi 2.5（Volcengine Coding Plan 推荐）；"DeerFlow is model-agnostic — it works with any LLM that implements the OpenAI-compatible API."
- 注：README 未提及 MisKnow-Agent

---

## 源C2：WebThinker（arXiv:2504.21776）——论文摘要级

### 元数据
- 标题（原文）：WebThinker: Empowering Large Reasoning Models with Deep Research Capability
- 作者（原文）：Xiaoxi Li, Jiajie Jin, Guanting Dong, Hongjin Qian, Yongkang Wu, Ji-Rong Wen, Yutao Zhu, Zhicheng Dou
- arXiv ID：2504.21776，版本 v2（published 2025-04-30T16:25:25Z，updated 2025-10-13T12:40:15Z）
- 分类：cs.CL, cs.AI, cs.IR；接收：NeurIPS 2025（arxiv:comment 声明）
- 代码（摘要声明）：https://github.com/RUC-NLPIR/WebThinker（RUC-NLPIR 团队，非 bytedance）

### 摘要（英文原文，一字未改）
Large reasoning models (LRMs), such as OpenAI-o1 and DeepSeek-R1, demonstrate impressive long-horizon reasoning capabilities. However, their reliance on static internal knowledge limits their performance on complex, knowledge-intensive tasks and hinders their ability to produce comprehensive research reports requiring synthesis of diverse web information. To address this, we propose WebThinker, a deep research agent that empowers LRMs to autonomously search the web, navigate among web pages, and draft reports during the reasoning process. WebThinker integrates a Deep Web Explorer module, enabling LRMs to dynamically search, navigate, and extract information from the web when encountering knowledge gaps. It also employs an Autonomous Think-Search-and-Draft strategy, allowing the model to seamlessly interleave reasoning, information gathering, and report writing in real time. To further enhance research tool utilization, we introduce an RL-based training strategy via iterative online Direct Preference Optimization (DPO). Extensive experiments on complex reasoning benchmarks (GPQA, GAIA, WebWalkerQA, HLE) and scientific report generation tasks (Glaive) demonstrate that WebThinker significantly outperforms existing methods and strong proprietary systems. Our approach enhances LRM reliability and applicability in complex scenarios, paving the way for more capable and versatile deep research systems. The code is available at https://github.com/RUC-NLPIR/WebThinker.

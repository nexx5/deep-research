---
source_id: S030
source_url: https://github.com/camel-ai/camel + https://github.com/FoundationAgents/MetaGPT + https://github.com/openai/swarm + https://github.com/microsoft/autogen
title: 多 Agent 框架概览合并存档（CAMEL / MetaGPT / OpenAI Swarm / Microsoft AutoGen）
author: 各仓库维护组织（camel-ai / FoundationAgents / openai / microsoft）
date: 各仓库页面（访问时状态）
fetched_at: 2026-08-04
content_type: github_repo_overview_collection
---

> 本 raw 为四个多 agent 框架 GitHub 仓库主页的合并存档，全部为**仓库官方 README 自述**（组织/团队官方声明，非独立验证）：
> - **源A = CAMEL**（https://github.com/camel-ai/camel，camel-ai 组织）
> - **源B = MetaGPT**（https://github.com/FoundationAgents/MetaGPT，FoundationAgents 组织）
> - **源C = OpenAI Swarm**（https://github.com/openai/swarm，OpenAI 组织）
> - **源D = Microsoft AutoGen**（https://github.com/microsoft/autogen，Microsoft 组织）
> 抓取渠道：多源搜索 skill 渠道1 webfetch（GitHub 页面，markdown），访问日期 2026-08-04。
> 存档已剔除 GitHub 导航噪音，保留 README 原文与仓库元数据；各节标注 URL。仅存档原文表述，不评判。
> 背景：本批为 Cognition《Don't Build Multi-Agents》（S021）点名批评对象（CAMEL/MetaGPT/OpenAI Swarm/Microsoft AutoGen）的概览采录；Cognition 批评与本批各框架官方主张客观并列，本 raw 不判对错。

---

# 源A：CAMEL（camel-ai/camel）

## A0. 元信息
- URL: https://github.com/camel-ai/camel
- 页面标题: "🐫 CAMEL: The first and the best multi-agent framework. Finding the Scaling Law of Agents."
- Stars 17.5k / Forks 2.0k / Watchers 121 / Commits 2,282（master）
- 许可证: Apache-2.0
- 官网: https://www.camel-ai.org；文档: https://docs.camel-ai.org
- PyPI: `pip install camel-ai`（README 明示）

## A1. 定位
- README: "CAMEL is an open-source community dedicated to finding the scaling laws of agents. We believe that studying these agents on a large scale offers valuable insights into their behaviors, capabilities, and potential risks. To facilitate research in this field, we implement and support various types of agents, tasks, prompts, models, and simulated environments."
- 研究论文锚点: CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society（arXiv:2303.17760，NeurIPS 2023）
- 设计原则（README 明示四项）: Evolvability（数据/环境交互驱动系统持续进化）、Scalability（支持百万级 agents 系统）、Statefulness（agent 有状态记忆，多步交互）、Code-as-Prompt（每行代码与注释都作为 agent 的提示）

## A2. 能力
- "Simulate up to 1M agents to study emergent behaviors and scaling laws in complex, multi-agent environments."
- 三大构建方向: Data Generation（CoT/Self-Instruct/Source2Synth 等数据生成）、Task Automation（Role Playing / Workforce / RAG Pipeline）、World Simulation（Oasis 案例）
- 关键模块（README 列表）: Agents、Agent Societies、Data Generation、Models、Tools、Memory、Storage、Benchmarks、Interpreters、Data Loaders、Retrievers、Runtime、Human-in-the-Loop

## A3. 与深度调研的关联（README 明示的用例/文档）
- Usecase: "Multi-Agent Research Assistant"——"Simulates a team of research agents collaborating on literature review, improving efficiency in exploratory analysis and reporting."
- Cookbook: "Role-Playing Scraper for Report & Knowledge Graph Generation"——role-playing agents for data scraping and reporting
- Cookbook: Dynamic Knowledge Graph Role-Playing——"processes financial reports, news articles, and research papers to help traders analyze data, identify relationships, and uncover market insights"
- Research 项目列表: OWL（https://github.com/camel-ai/owl）、OASIS、CRAB、Loong、Agent Trust、Emos

## A4. 与 Cognition 批评相关（客观记录）
- 本仓库主页 README 未见对 Cognition《Don't Build Multi-Agents》的直接回应表述。

---

# 源B：MetaGPT（FoundationAgents/MetaGPT）

## B0. 元信息
- URL: https://github.com/FoundationAgents/MetaGPT
- 页面标题: "🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming"
- Stars 69.7k / Forks 8.9k / Watchers 914 / Commits 6,367（main）
- 许可证: MIT
- 文档: https://docs.deepwisdom.ai
- 环境要求（README）: Python 3.9 ~ 3.12；安装需 node + pnpm

## B1. 定位
- README: "Assign different roles to GPTs to form a collaborative entity for complex tasks."
- 核心哲学: "Code = SOP(Team) is the core philosophy. We materialize SOP and apply it to teams composed of LLMs."
- 软件公司 as 多 agent 系统: "MetaGPT takes a one line requirement as input and outputs user stories / competitive analysis / requirements / data structures / APIs / documents, etc. Internally, MetaGPT includes product managers / architects / project managers / engineers."
- 研究论文锚点: MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework（ICLR 2024）

## B2. 能力与近期动态（README News）
- Data Interpreter（examples/di）: "Run data analysis on sklearn Iris dataset, include a plot"（数据分析/代码执行能力）
- 2025-02-17: 引入 SPO（arXiv:2502.06855）与 AOT（arXiv:2502.12018）两篇论文及代码
- 2025-01-22: AFlow: Automating Agentic Workflow Generation 被 ICLR 2025 接收为 oral（top 1.8%，LLM-based Agent 类目排名 #2）
- 2025-02-19: 发布 MGX（MetaGPT X，mgx.dev）——"the world's first AI agent development team"自然语言编程产品（2025-03 ProductHunt 当日/当周 #1）
- 文档 Use Cases: Data Interpreter、Debate、Researcher、Receipt Assistant

## B3. 与深度调研的关联（README 明示）
- Use Cases 文档含 Researcher 用例（docs use_cases/agent/researcher）
- 一行需求输入即输出 competitive analysis（竞争分析）等产物

## B4. 与 Cognition 批评相关（客观记录）
- 本仓库主页 README 未见对 Cognition《Don't Build Multi-Agents》的直接回应表述。

---

# 源C：OpenAI Swarm（openai/swarm）

## C0. 元信息
- URL: https://github.com/openai/swarm
- 页面标题: "Educational framework exploring ergonomic, lightweight multi-agent orchestration. Managed by OpenAI Solution team."
- Stars 21.9k / Forks 2.3k / Watchers 298 / Commits 29（main，实验性项目规模）
- 许可证: MIT
- 环境要求: Python 3.10+

## C1. 定位
- README 首行警示: "Swarm (experimental, educational)"
- README: "Swarm focuses on making agent coordination and execution lightweight, highly controllable, and easily testable. It accomplishes this through two primitive abstractions: Agents and handoffs."
- "Swarm is entirely powered by the Chat Completions API and is hence stateless between calls."
- "Swarm is an educational resource for developers curious to learn about multi-agent orchestration."

## C2. 维护状态（README 明示）
- "Important: Swarm is now replaced by the OpenAI Agents SDK（https://github.com/openai/openai-agents-python），which is a production-ready evolution of Swarm. The Agents SDK features key improvements and will be actively maintained by the OpenAI team. We recommend migrating to the Agents SDK for all production use cases."
- 即：Swarm 已停止演进，官方建议迁移至 OpenAI Agents SDK。

## C3. 与深度调研的关联
- 通用编排框架，examples 为客服/导购/分诊等场景（airline/support_bot/personal_shopper/triage_agent）；README 未列举深度调研场景。

## C4. 与 Cognition 批评相关（客观记录）
- 本仓库主页 README 未见对 Cognition《Don't Build Multi-Agents》的直接回应表述。

---

# 源D：Microsoft AutoGen（microsoft/autogen）

## D0. 元信息
- URL: https://github.com/microsoft/autogen
- 页面标题: "A programming framework for agentic AI"
- Stars 60.2k / Forks 9.1k / Watchers 525 / Commits 3,782（main）
- 许可证: 双许可——文档 CC-BY-4.0（LICENSE）、代码 MIT（LICENSE-CODE）
- 环境要求: Python 3.10 或更高

## D1. 定位
- README: "AutoGen is a framework for creating multi-agent AI applications that can act autonomously or work alongside humans."
- "Pioneered in Microsoft Research, AutoGen opened the door to experimental multi-agent orchestration patterns that inspired the community."
- 分层设计: Core API（消息传递、事件驱动 agents、本地与分布式 runtime，支持 .NET 与 Python 跨语言）、AgentChat API（快速原型）、Extensions API（LLM client 与工具扩展）

## D2. 维护状态（README 明示）
- 警示徽章 "Maintenance Mode": "AutoGen is now in maintenance mode. It will not receive new features or enhancements and is community managed going forward."
- "New users should start with Microsoft Agent Framework（https://github.com/microsoft/agent-framework）。Existing users are encouraged to migrate using the AutoGen → Microsoft Agent Framework migration guide."
- 继任者描述: "Microsoft Agent Framework (MAF) is the enterprise-ready successor to AutoGen... Microsoft Agent Framework 1.0 gives you enterprise-grade multi-agent orchestration, multi-provider model support, and cross-runtime interoperability via A2A and MCP."

## D3. 能力与工具
- AutoGen Studio: no-code GUI（autogenstudio，本地端口 8080）——README 明示 "not meant to be a production-ready app"
- AutoGen Bench（agbench）: "provides a benchmarking suite for evaluating agent performance"
- Magentic-One: "a state-of-the-art multi-agent team built using AgentChat API and Extensions API that can handle a variety of tasks that require web browsing, code execution, and file handling."
- MCP 集成示例: Playwright MCP server 构建 web browsing assistant（README 代码示例）

## D4. 与深度调研的关联（README 明示）
- Magentic-One 覆盖 web browsing / code execution / file handling 任务类型；未在 README 列举深度调研专用场景。

## D5. 与 Cognition 批评相关（客观记录）
- 本仓库主页 README 未见对 Cognition《Don't Build Multi-Agents》的直接回应表述；README 出现对多 agent 实验模式的自我定位（"experimental multi-agent orchestration patterns"）与继任框架（MAF）迁移主张。

---

# 跨源元观察（客观记录）

1. 四个框架均为**通用多 agent 编排框架**（非深度调研专用）：README 均以角色扮演/多 agent 协作/任务编排为定位，调研类用法（CAMEL Multi-Agent Research Assistant、MetaGPT Researcher 用例、AutoGen Magentic-One web browsing）为其适用场景之一。
2. 维护状态分化：OpenAI Swarm 已被 Agents SDK 取代（29 commits 实验项目）、AutoGen 进入 maintenance mode（由 Microsoft Agent Framework 接替）；CAMEL（2,282 commits）与 MetaGPT（6,367 commits）仍活跃。
3. 许可证：CAMEL Apache-2.0、MetaGPT MIT、Swarm MIT、AutoGen CC-BY-4.0（文档）+ MIT（代码）。
4. 各仓库主页均未出现对 Cognition《Don't Build Multi-Agents》批评的直接回应。

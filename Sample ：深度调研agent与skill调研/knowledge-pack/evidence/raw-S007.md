---
raw_metadata:
  raw_id: "raw-S007"
  source_type: "web_page"
  title: "Gemini Deep Research 官方说明合集（官方概览页 + 专项页 + API 文档 + 发布文 + 帮助中心）"
  original_url: "https://gemini.google/overview/"
  repo_url: ""
  local_repo_path: ""
  local_file_path: ""
  captured_at: "2026-08-04"
  files: []
  display_citation: "Gemini 官方 Deep Research 产品与 API 说明合集（gemini.google/overview/ 概览页、gemini.google/overview/deep-research 专项页、ai.google.dev 开发者文档、blog.google 发布文、support.google.com 帮助中心）"
---

# 原始资料

## 元数据
- 标题：Gemini Deep Research 官方说明合集
- 来源URL/文件路径：https://gemini.google/overview/ （主）等 6 个官方页面（详见各节）
- 来源类型：网络（官方产品页/开发者文档/官方博客/帮助中心）
- 采集时间：2026-08-04
- 采集ID：S007

## 正文

> 本文件为 CloakBrowser（defuddle 提取，JS 渲染模式）抓取的官方页面原文。按页面分节存档。所有内容为 Google 官方自我陈述。

---

### 页面 1：https://gemini.google/overview/deep-research/ （Gemini Deep Research 专项官方页，核心）

# Gemini Deep Research — your personal research assistant

### An agentic system

To build Deep Research, we developed a new planning system that enables Gemini app to work through complex problems. For Deep Research, we trained Gemini models to be capable of:

- **Breaking down the problem:** When presented with a complex user query, the system first formulates a detailed research plan, breaking the problem into a series of smaller, manageable sub-tasks. You're in control of the plan: Gemini presents it to you, and you can refine it to make sure it's focused on the right areas.
- **Research**: The model oversees the execution of this plan, and intelligently determines which sub-tasks can be tackled simultaneously and which need to be done sequentially. The model can use tools like search and web browsing to fetch information & reason over it. At each step the model reasons over information available to decide its next move. We introduced a thinking panel for users to follow what the model has learnt so far & what it intends to do next.
- **Synthesis:** Once the model determines enough information has been gathered, it synthesizes the findings into a comprehensive report. In building the report, Gemini critically evaluates the information, identifies key themes and inconsistencies, and structures the report in a logical and informative way, even performing multiple passes of self-critique to enhance clarity and detail.

### New category, new problems, new solutions

In building Deep Research, we had to work through three significant technical challenges:

#### Multi-step planning

Research tasks require multiple steps of iterative planning. At each step, the model has to ground itself on all information gathered so far, then identify missing information and discrepancies it wants to explore — all while trading off comprehensiveness with compute and user wait time. Training the model to be effective at long multi-step planning in a data efficient manner enabled us to make Deep Research function in an open domain setting across all topics.

#### Long-running inference

A typical Deep Research task involves many model calls over several minutes. This creates a challenge for building agents: It has to be built so that a single failure doesn't mean having to restart the task from the beginning.

To address this, we developed a novel asynchronous task manager that maintains a shared state between the planner and task models, allowing for graceful error recovery without restarting the entire task. This system is truly asynchronous: you can hop to a different app or quite literally turn off your computer after starting a Deep Research project and the next time you visit Gemini, you'll get notified when your research is done.

#### Context management

Over the course of a research session, Gemini can process hundreds of pages of content. To maintain continuity and enable follow-up questions, we use Gemini's industry-leading 1 million token context window complemented with a RAG setup. This effectively allows the system to "remember" everything it has learned during that chat session, making it smarter the longer you interact with it.

### Evolving with new models

When Deep Research launched in December it was powered by Gemini 1.5 Pro. With the introduction of Gemini 2.0 Flash Thinking (experimental) we were able to dramatically improve both the quality and serving efficiency of this product. With thinking models, Gemini takes more time to plan out its approach before it makes its next steps. This innate characteristic of self-reflection and planning makes it a great fit for these kind of long running agentic tasks. What we see is that now Gemini is even better at all stages of research and delivers more detailed reports. At the same time, the compute-efficiency of the Flash model allows us to expand access to Deep Research to far more users. We're really excited about developing on flash and thinking models in general and expect deep research to keep getting better and better.

And with our most capable model, Gemini 3, Deep Research is even better at all stages of research, delivering even more insightful and detailed reports

### What's next

We built the system to be versatile, so over time we can expand its capabilities by giving you more control over what it can browse and giving it sources beyond the open web.

We are excited to see how people use Deep Research, and these real-world experiences will inform how we continue to build and improve Deep Research. Ultimately, our goal is a truly agentic and universally helpful AI assistant.

（另含页面首屏文案，Tavily 摘要补充：Deep Research 是 Gemini 中的 agentic 功能，可自动浏览数百个网站乃至用户的 Gmail、Drive、Chat，思考其发现，并在数分钟内创建有洞察力的多页报告。With the Gemini 3 model, Deep Research is even better at all stages of research。支持桌面/移动端、150 国、45+ 语言、Google Workspace 用户。入口：提示栏选择 Deep Research。）

---

### 页面 2：https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/ （官方发布文，2025-12-11）

# Build with Gemini Deep Research

Dec 11, 2025 | We have reimagined Gemini Deep Research to be more powerful than ever. It is now accessible to developers via the new Interactions API, launching alongside DeepSearchQA, a benchmark for complex web search tasks.

Today, we are releasing a significantly more powerful Gemini Deep Research agent, available via the Interactions API. For the first time, developers can embed Google's most advanced autonomous research capabilities directly into their own applications. We are also open-sourcing a new web research agent benchmark, DeepSearchQA, designed to test agent comprehensiveness on web research tasks.

Gemini Deep Research is an agent optimized for long-running context gathering and synthesis tasks. The agent's reasoning core uses Gemini 3 Pro, our most factual model yet, and is specifically trained to reduce hallucinations and maximize report quality during complex tasks. By scaling multi-step reinforcement learning for search, the agent autonomously navigates complex information landscapes with high accuracy.

Deep Research iteratively plans its investigation – it formulates queries, reads results, identifies knowledge gaps, and searches again. This release features vastly improved web search, allowing it to navigate deep into sites for specific data.

The new Gemini Deep Research agent achieves state-of-the-art results on Humanity's Last Exam (HLE) and DeepSearchQA, and is our best on BrowseComp. It is optimized to generate well-researched reports at much lower cost. Deep Research is now more useful and intelligent than ever, and will soon be available in Google Search, NotebookLM, Google Finance and upgraded in the Gemini App.

Gemini Deep Research achieves state-of-the-art 46.4% on the full Humanity's Last Exam (HLE) set, 66.1% on DeepSearchQA and a high 59.2% on BrowseComp

### DeepSearchQA: a benchmark for deep research agents

Existing benchmarks often fail to capture the complexity of real-world, multi-step web research. This is why we are open-sourcing DeepSearchQA, a new benchmark to evaluate agents on intricate, multi-step information-seeking tasks.

DeepSearchQA features 900 hand-crafted "causal chain" tasks across 17 fields, where each step depends on prior analysis. Unlike traditional fact-based tests, DeepSearchQA measures comprehensiveness, requiring agents to generate exhaustive answer sets. This assesses both research precision and retrieval recall.

DeepSearchQA also serves as a diagnostic tool for the benefits of "thinking time." In our internal evaluations, we observed significant performance gains when allowing the agent to perform more searches and reasoning steps which we plan to explore in future releases.

Comparing pass@8 vs. pass@1 results demonstrates the value of letting the agent explore multiple parallel trajectories for answer verification. These results were computed on a 200-prompt subset of DeepSearchQA.

We are releasing the benchmark assets to drive future research toward more robust and capable agents: dataset, leaderboard, starter Colab, and a Technical Report.

### Gemini Deep Research agent in the real world

The Gemini Deep Research agent is already demonstrating profound, immediate results in complex fields demanding high precision and context based on early feedback and testing. This includes verticals such as financial services, biotech, and market research, which have used Gemini Deep Research to tackle preliminary research tasks.

Financial firms are using Gemini Deep Research to automate the labor-intensive initial stages of due diligence. By aggregating market signals, competitor analysis, and compliance risks from across the web and proprietary sources, the agent becomes a massive force multiplier for investment teams in their early research phases.

Customer quote (financial services): "Gemini Deep Research agent has been a huge accelerant to our diligence processes, shortening our research cycles from days to hours without loss of fidelity or quality. It feels like having an army of experts ready to go in support of our most ambitious analyses."

In the scientific community, Deep Research is helping to solve complex safety challenges. Axiom Bio, which builds AI systems to predict drug toxicity, found that Gemini Deep Research unlocked an unprecedented level of initial research depth and granularity across biomedical literature, accelerating drug discovery pipelines.

Customer quote (Axiom Bio): "Gemini Deep Research surfaces granular data and evidence at and beyond what previously only a human researcher could do. We're excited to build on this as a foundation for agentic systems that reason from molecular mechanisms to experimental data and clinical outcomes, and empower scientists to develop safer medicines."

### Build with Gemini Deep Research

For developers building the next generation of automated research tools, Gemini Deep Research agent offers unparalleled capabilities through which to synthesize information and generate a detailed report:

- **Unified information synthesis:** Gemini Deep Research analyzes your documents (PDFs, CSVs, docs) and public web data using File Upload and the File Search Tool. It also handles large context gracefully, allowing you to place extensive background information directly in the prompt.
- **Report steerability:** You control the output via prompting, defining the structure, headers, and subheaders, or specifying data table generation and formatting.
- **Detailed citations:** Granular sourcing is provided for claims, allowing users to verify data origin.
- **Structured outputs:** Supports JSON schema outputs for easy parsing of research results by downstream applications.

### Get started with Deep Research in the Interactions API

You can follow our developer documentation to start building with the Deep Research agent using the new Interactions API, which is our next-generation interface designed to simplify interactions with Gemini models and agents. You can access the Interactions API with your Gemini API key from Google AI Studio.

Future updates will also focus on richer outputs like native chart generation for visual analytical reports and expanding connectivity through Model Context Protocol (MCP) support to more easily tap into your custom data sources. We're also working to bring Gemini Deep Research to Vertex AI for enterprises.

---

### 页面 3：https://ai.google.dev/gemini-api/docs/deep-research （Gemini API 开发者文档，核心参数）

# Gemini Deep Research Agent | Gemini API

The Gemini Deep Research Agent autonomously plans, executes, and synthesizes multi-step research tasks. Powered by Gemini, it navigates complex information landscapes to produce detailed, cited reports. New capabilities allow you to collaboratively plan with the agent, connect to external tools using MCP servers, include visualizations (like charts and graphs), and provide documents directly as input.

Research tasks involve iterative searching and reading and can take several minutes to complete. You must use background execution (set background=true) to run the agent asynchronously and poll for results or stream updates.

（代码示例：通过 interactions.create 指定 agent="deep-research-preview-04-2026"、background=True 轮询结果；curl POST https://generativelanguage.googleapis.com/v1beta/interactions —— 从略）

## Supported versions

The Deep Research agent comes in two versions:

- **Deep Research** (`deep-research-preview-04-2026`): Designed for speed and efficiency, ideal to be streamed back to a client UI.
- **Deep Research Max** (`deep-research-max-preview-04-2026`): Maximum comprehensiveness for automated context gathering and synthesis.

## Collaborative planning

Collaborative planning gives you control over the research direction before the agent starts its work by letting you review and refine the research plan before execution. When enabled, the agent returns a proposed research plan instead of executing immediately. You can then review, modify, or approve the plan through multi-turn interactions.

（三步流程：Step 1 Request a plan 设 collaborative_planning=True 返回研究计划；Step 2 Refine the plan 用 previous_interaction_id 迭代；Step 3 Approve and execute 设 collaborative_planning=False 批准并启动研究 —— 从略代码）

## Visualization

When visualization is set to "auto", the agent can generate charts, graphs, and other visual elements to support its research findings. Generated images are included in the response steps and streamed as image deltas. For best results, explicitly ask for visuals in your query. Setting visualization to "auto" enables the capability, but the agent generates visuals only when the prompt requests them.

## Supported tools

Deep Research supports multiple built-in and external tools. By default (when no tools parameter is provided), the agent has access to Google Search, URL Context, and Code Execution. You can explicitly specify tools to restrict or extend the agent's capabilities.

| Tool | Type value | Description |
| --- | --- | --- |
| Google Search | google_search | Search the public web. Enabled by default. |
| URL Context | url_context | Read and summarize web page content. Enabled by default. |
| Code Execution | code_execution | Execute code to perform calculations and data analysis. Enabled by default. |
| MCP Server | mcp_server | Connect to remote MCP servers for external tool access. |
| File Search | file_search | Search your uploaded document corpora. |

## Steerability and formatting

You can steer the agent's output by providing specific formatting instructions in your prompt. This allows you to structure reports into specific sections and subsections, include data tables, or adjust tone for different audiences (e.g., "technical," "executive," "casual"). Define the desired output format explicitly in your input text.

## Multimodal inputs

Deep Research supports multimodal inputs, including images and documents (PDFs), allowing the agent to analyze visual content and conduct web-based research contextualized by the provided inputs.

### Document understanding

Document understanding allows passing documents directly as multimodal input. The agent analyzes the provided documents and conducts research grounded in their content.

## Handling long-running tasks

Deep Research is a multi-step process involving planning, searching, reading, and writing. This cycle typically exceeds the standard timeout limits of synchronous API calls.

Agents are required to use background=True. The API returns a partial Interaction object immediately. You can use the id property to retrieve an interaction for polling. The interaction state will transition from in_progress to completed or failed.

### Streaming

Deep Research supports streaming to receive real-time updates on the research progress including thought summaries, text output, and generated images. You must set stream=True and background=True. To receive intermediate reasoning steps (thoughts) and progress updates, you must enable thinking summaries by setting thinking_summaries to "auto" in the agent_config. Without this, the stream may only provide the final results.

Stream event types: step.delta with delta type thought (intermediate reasoning step), text (part of final text output), image (generated image, base64-encoded). Streaming supports automatic reconnection after connection drops (e.g., after the 600-second timeout) using interaction_id and last_event_id.

You can continue the conversation after the agent returns the final report by using the previous_interaction_id. This lets you ask for clarification, summarization or elaboration on specific sections of the research without restarting the entire task.

## When to use Gemini Deep Research Agent

Deep Research is an **agent**, not just a model. It is best suited for workloads that require an "analyst-in-a-box" approach rather than low-latency chat.

| Feature | Standard Gemini Models | Gemini Deep Research Agent |
| --- | --- | --- |
| **Latency** | Seconds | Minutes (Async/Background) |
| **Process** | Generate -> Output | Plan -> Search -> Read -> Iterate -> Output |
| **Output** | Conversational text, code, short summaries | Detailed reports, long-form analysis, comparative tables |
| **Best For** | Chatbots, extraction, creative writing | Market analysis, due diligence, literature reviews, competitive landscaping |

## Agent configuration

Deep Research uses the agent_config parameter to control behavior:

| Field | Type | Default | Description |
| --- | --- | --- | --- |
| type | string | Required | Must be "deep-research". |
| thinking_summaries | string | "none" | Set to "auto" to receive intermediate reasoning steps during streaming. Set to "none" to disable. |
| visualization | string | "auto" | Set to "auto" to enable agent-generated charts and images. Set to "off" to disable. |
| collaborative_planning | boolean | false | Set to true to enable multi-turn plan review before research begins. |

## Availability and pricing

You can access the Gemini Deep Research Agent using the Interactions API in Google AI Studio and the Gemini API.

Pricing follows a pay-as-you-go model based on the underlying Gemini models and the specific tools the agent utilizes. Unlike standard chat requests, where a request leads to one output, a Deep Research task is an agentic workflow. A single request triggers an autonomous loop of planning, searching, reading, and reasoning.

### Estimated costs

Costs vary based on the depth of research required. The agent autonomously determines how much reading and searching is necessary to answer your prompt.

- **Deep Research** (`deep-research-preview-04-2026`): For a typical query requiring moderate analysis, the agent might use ~80 search queries, ~250k input tokens (~50-70% cached), and ~60k output tokens.
	- **Estimated total:** ~$1.00 – $3.00 per task
- **Deep Research Max** (`deep-research-max-preview-04-2026`): For deep competitive landscape analysis or extensive due diligence, the agent might use up to ~160 search queries, ~900k input tokens (~50-70% cached), and ~80k output tokens.
	- **Estimated total:** ~$3.00 – $7.00 per task

## Safety considerations

Giving an agent access to the web and your private files requires careful consideration of safety risks.

- **Prompt injection using files:** The agent reads the contents of the files you provide. Ensure that uploaded documents (PDFs, text files) come from trusted sources. A malicious file could contain hidden text designed to manipulate the agent's output.
- **Web content risks:** The agent searches the public web. While we implement robust safety filters, there is a risk that the agent may encounter and process malicious web pages. We recommend reviewing the citations provided in the response to verify the sources.
- **Exfiltration:** Be cautious when asking the agent to summarize sensitive internal data if you are also allowing it to browse the web.

## Best practices

- **Prompt for unknowns:** Instruct the agent on how to handle missing data.
- **Provide context:** Ground the agent's research by providing background information or constraints directly in the input prompt.
- **Use collaborative planning:** For complex queries, enable collaborative planning to review and refine the research plan before execution.
- **Multimodal inputs:** Deep Research Agent supports multi-modal inputs. Use cautiously, as this increases costs and risks context window overflow.

## Limitations

- **Custom tools:** You cannot currently provide custom Function Calling tools but you can use remote MCP (Model Context Protocol) servers with the Deep Research agent.
- **Structured output:** The Deep Research Agent currently doesn't support structured outputs.
- **Max research time:** The Deep Research agent has a maximum research time of 60 minutes. Most tasks should complete within 20 minutes.
- **Store requirement:** Agent execution using background=True requires store=True.
- **Google search:** Google Search is enabled by default and specific restrictions apply to the grounded results.

---

### 页面 4：https://support.google.com/gemini/answer/15719111 （Gemini Apps 帮助中心：Deep Research 使用）

# Use Deep Research in Gemini Apps - Computer

You can conduct in-depth and real-time research on almost any subject with Deep Research in Gemini Apps. By default, Gemini includes Google Search as a source for your research. You can change or add other sources, like your personal Gmail or Drive, for your research. You can also upload files and add NotebookLM notebooks.

Tip: If you have a Google AI Ultra plan, Deep Research reports may include visuals like charts, diagrams, schematics, and interactive simulators.

## What you need

To use Deep Research, you need to: Be 18 or over. Be signed in to the Gemini app.

## About Deep Research models & limits

Deep Research models: （Google AI Pro 和 Google AI Ultra 用户可使用 Pro 生成报告以获得更高质量；所有用户可使用 Thinking；详见文档——标签页渲染节选）

Deep Research limits: In Gemini Apps, there are limits for: Daily research requests; Number of research requests you can run at the same time. If you're close to your limit, Gemini Apps notifies you how many research requests are left for the day.

## Start a Deep Research report

1. On your computer, go to gemini.google.com.
2. In the text box, click Add Files and then Deep Research.
3. (Optional) To upload files or an image with your prompt, click Add Files and then Files.
4. (Optional) To choose the sources for your research, click Sources and select the sources you want to include, like Gmail or Drive. Other Google services, like Gmail and Drive, are only available if the Google Workspace app is connected to Gemini Apps. Google Search is included as a source by default. To limit your research to other selected sources, deselect Google Search.
5. In the text box, enter a question or prompt that explains what you want to research.
6. Click Submit. Gemini will create a research plan for your topic. To update the research plan before you create a report, click Edit plan.
7. Click Start research.
8. When your report is ready, click Open.

Tips:
- It usually takes about 5-10 minutes to generate the report since Gemini analyzes many sources. For more complex reports, it may take longer.
- While you wait for the report, you can leave the chat. When it's ready, Gemini will notify you: In the web app: next to the chat thread with your completed report. In the mobile app: as a notification on your device.

## Find your research reports

You can only find past research reports if your Keep Activity setting is on.

## Listen to your research report

In the Canvas panel, click Create and then Audio Overview.

## Visualize your research report

In the Canvas panel, click Create. To create a custom visualization based on the report, enter the description as a prompt in the text box.

## Share, export, or copy your research report

In the Canvas panel, click Share & export. Select how you want to share or export the report: Share Canvas; Export to Docs; Copy Contents.

---

### 页面 5：https://support.google.com/gemini/answer/16275805 （Gemini Apps 帮助中心：额度与订阅层级）

# Gemini Apps limits & upgrades for Google AI subscribers

Gemini Apps have compute-based usage limits that determine how much you can interact with Gemini tools and features. These limits factor in the complexity of your prompt, the models and features you use, and the length of your chat. Your limit refreshes every 5 hours until you reach your weekly limit.

You can upgrade to a Google AI plan for expanded access to features and models in Gemini Apps. Gemini Apps upgrades are part of select Google One paid plans for personal accounts.

Important: Gemini Apps limits may change. Access is subject to change or may be limited based on testing, experimentation, or availability.

### Usage limits

| **Plan** | **Limit** |
| --- | --- |
| Without an AI plan | Standard limits |
| AI Plus | 2x higher than standard limits |
| AI Pro | 4x higher than standard limits |
| AI Ultra | 5x or 20x higher than AI Pro limits depending on your subscription |

### Context windows

| Plan | Context window |
| --- | --- |
| Without an AI plan | 32k tokens |
| AI Plus | 128k tokens |
| AI Pro & AI Ultra | 1 million tokens |

### Feature availability

Some features are only available with Google AI subscription plans. Some features (like media generation or Deep Research) will consume more of your usage.

（功能可用性表格：Deep Research 在无 AI 计划 / AI Plus / AI Pro / AI Ultra 各档位均列示可用（表格以图标呈现，无法区分具体可用性状态）；Early access 仅在订阅档提供）

More info about limits: What you can do when you reach a usage limit; Usage limit changes; How to tell if you're close to a limit & when it refreshes.

---

### 页面 6：https://gemini.google/overview/ （Gemini 官方概览页，2024-07-25 更新——通用 Gemini app 说明，非 Deep Research 专项）

# What is Gemini and how it works

An overview of the Gemini app。Gemini 是 Google 对多模态 LLM 的界面（处理文本、音频、图像等），基于 Google 在 LLM 上的研究（Word2Vec 2013、神经对话模型 2015、Transformer 2017、多轮对话 2020）。2023 年 3 月以 Bard 名义作为实验推出。

能力定位：Productivity（总结长文档、编码——编码是最流行应用之一）、Creativity（写博客提纲、生成图片）、Curiosity（解释复杂概念、表面相关见解；即将支持联网推荐内容）。

官方承认的 LLM 界面已知局限（六类）：
- Accuracy：回答可能不准确，尤其在复杂或事实性主题上
- Bias：回答可能反映训练数据中的偏见
- Multiple Perspectives：可能未能展示多视角
- Persona：可能错误暗示有个人观点或情感
- False positives and false negatives：可能对合理提示不回应（误报），也可能对不当提示生成回应（漏报）
- Vulnerability to adversarial prompting：用户会用无意义提示压力测试

技术发展：持续红队测试；隐私（Gemini Apps Privacy Hub）；用户控制（Gemini Apps Activity、Takeout 导出）；发布者控制（Google-Extended 管理是否用于模型训练与 grounding）。最后更新 2024-07-25。

（此页为 Gemini app 整体说明，Deep Research 未在其中单独展开；保留作为产品背景。）

---
> 不可变记录。后续分析不修改此文件。

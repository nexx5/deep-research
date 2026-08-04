---
source_id: S035
source_title: 浏览器代理流派评测标尺与竞品（OSWorld/WebArena/WebVoyager 基准 + Anthropic computer use/Google Project Mariner）
extraction_level: deep
model_used: deepseek-v4-flash
extracted_at: 2026-08-04
access_date: 2026-08-04
search_channel: 多源搜索 skill（arXiv 学术引擎 API + Tavily 搜索定位 + webfetch 官方页抓取）
note: 多来源合并采集。论文摘要由学术引擎返回作 content；竞品官网标注"官方声称"。任务给定 Project Mariner 官方页 deepmind.google/technologies/project-mariner/ 访问时重定向到 DeepMind 首页（内容不可得），改用官方博客两篇（2024-12-11 Gemini 2.0 发布文 + 2025-05-20 Google I/O 更新文）作竞品官方声称来源。
---

# raw-S035：浏览器代理流派评测标尺与竞品

## 分节 A｜OSWorld（arxiv 2404.07972）

- URL: https://arxiv.org/abs/2404.07972
- 引擎: arXiv API（export.arxiv.org/api/query, id_list=2404.07972）
- 标题: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments
- 发布: 2024-04-11（v2 更新 2024-05-30）；cs.AI / cs.CL
- 作者: Tianbao Xie 等 17 人（含 Shuyan Zhou, Victor Zhong, Tao Yu）
- 摘要（原文）:

> Autonomous agents that accomplish complex computer tasks with minimal human interventions have the potential to transform human-computer interaction, significantly enhancing accessibility and productivity. However, existing benchmarks either lack an interactive environment or are limited to environments specific to certain applications or domains, failing to reflect the diverse and complex nature of real-world computer use, thereby limiting the scope of tasks and agent scalability. To address this issue, we introduce OSWorld, the first-of-its-kind scalable, real computer environment for multimodal agents, supporting task setup, execution-based evaluation, and interactive learning across various operating systems such as Ubuntu, Windows, and macOS. OSWorld can serve as a unified, integrated computer environment for assessing open-ended computer tasks that involve arbitrary applications. Building upon OSWorld, we create a benchmark of 369 computer tasks involving real web and desktop apps in open domains, OS file I/O, and workflows spanning multiple applications. Each task example is derived from real-world computer use cases and includes a detailed initial state setup configuration and a custom execution-based evaluation script for reliable, reproducible evaluation. Extensive evaluation of state-of-the-art LLM/VLM-based agents on OSWorld reveals significant deficiencies in their ability to serve as computer assistants. While humans can accomplish over 72.36% of the tasks, the best model achieves only 12.24% success, primarily struggling with GUI grounding and operational knowledge. Comprehensive analysis using OSWorld provides valuable insights for developing multimodal generalist agents that were not possible with previous benchmarks. Our code, environment, baseline models, and data are publicly available at https://os-world.github.io.

- 关键数字（论文自称）: 369 个任务；人类 72.36%+；最佳模型 12.24%；跨 Ubuntu/Windows/macOS；开源（os-world.github.io）

## 分节 B｜WebArena（arxiv 2307.13854）

- URL: https://arxiv.org/abs/2307.13854
- 引擎: arXiv API
- 标题: WebArena: A Realistic Web Environment for Building Autonomous Agents
- 发布: 2023-07-25（v4 更新 2024-04-16）；cs.AI / cs.CL / cs.LG
- 作者: Shuyan Zhou 等 12 人（含 Daniel Fried, Uri Alon, Graham Neubig）
- 摘要（原文）:

> With advances in generative AI, there is now potential for autonomous agents to manage daily tasks via natural language commands. However, current agents are primarily created and tested in simplified synthetic environments, leading to a disconnect with real-world scenarios. In this paper, we build an environment for language-guided agents that is highly realistic and reproducible. Specifically, we focus on agents that perform tasks on the web, and create an environment with fully functional websites from four common domains: e-commerce, social forum discussions, collaborative software development, and content management. Our environment is enriched with tools (e.g., a map) and external knowledge bases (e.g., user manuals) to encourage human-like task-solving. Building upon our environment, we release a set of benchmark tasks focusing on evaluating the functional correctness of task completions. The tasks in our benchmark are diverse, long-horizon, and designed to emulate tasks that humans routinely perform on the internet. We experiment with several baseline agents, integrating recent techniques such as reasoning before acting. The results demonstrate that solving complex tasks is challenging: our best GPT-4-based agent only achieves an end-to-end task success rate of 14.41%, significantly lower than the human performance of 78.24%. These results highlight the need for further development of robust agents, that current state-of-the-art large language models are far from perfect performance in these real-life tasks, and that WebArena can be used to measure such progress.

- 关键数字（论文自称）: 四域（电商/社交论坛/协作软件开发/内容管理）；GPT-4 最佳 agent 14.41% vs 人类 78.24%；开源（webarena.dev）

## 分节 C｜WebVoyager（arxiv 2401.13919）

- URL: https://arxiv.org/abs/2401.13919
- 引擎: arXiv API
- 标题: WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models
- 发布: 2024-01-25（v4 更新 2024-06-06）；cs.CL / cs.AI；ACL 2024 main
- 作者: Hongliang He 等 8 人（含 Wenhao Yu, Dong Yu）
- 摘要（原文）:

> The rapid advancement of large language models (LLMs) has led to a new era marked by the development of autonomous applications in real-world scenarios, which drives innovation in creating advanced web agents. Existing web agents typically only handle one input modality and are evaluated only in simplified web simulators or static web snapshots, greatly limiting their applicability in real-world scenarios. To bridge this gap, we introduce WebVoyager, an innovative Large Multimodal Model (LMM) powered web agent that can complete user instructions end-to-end by interacting with real-world websites. Moreover, we establish a new benchmark by compiling real-world tasks from 15 popular websites and introduce an automatic evaluation protocol leveraging multimodal understanding abilities of GPT-4V to evaluate open-ended web agents. We show that WebVoyager achieves a 59.1% task success rate on our benchmark, significantly surpassing the performance of both GPT-4 (All Tools) and the WebVoyager (text-only) setups, underscoring the exceptional capability of WebVoyager. The proposed automatic evaluation metric achieves 85.3% agreement with human judgment, indicating its effectiveness in providing reliable and accurate assessments of web agents.

- 关键数字（论文自称）: 15 个流行网站真实任务；WebVoyager 59.1%；GPT-4V 自动评估与人类判断一致率 85.3%；开源（github.com/MinorJerry/WebVoyager）

## 分节 D｜Anthropic computer use 官方公告（官方声称）

- URL: https://www.anthropic.com/news/3-5-models-and-computer-use
- 抓取渠道: webfetch（官方新闻页）
- 标题: Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku
- 发布: 2024-10-22（页面内 12/03/2024 更新 3.5 Haiku 定价）
- 来源性质: 官方声称（厂商自报）
- 正文要点（原文摘录）:

> Today, we're announcing an upgraded Claude 3.5 Sonnet, and a new model, Claude 3.5 Haiku. ... We're also introducing a groundbreaking new capability in public beta: computer use. Available today on the API, developers can direct Claude to use computers the way people do—by looking at a screen, moving a cursor, clicking buttons, and typing text. Claude 3.5 Sonnet is the first frontier AI model to offer computer use in public beta. At this stage, it is still experimental—at times cumbersome and error-prone. We're releasing computer use early for feedback from developers, and expect the capability to improve rapidly over time.

> Asana, Canva, Cognition, DoorDash, Replit, and The Browser Company have already begun to explore these possibilities, carrying out tasks that require dozens, and sometimes even hundreds, of steps to complete. For example, Replit is using Claude 3.5 Sonnet's capabilities with computer use and UI navigation to develop a key feature that evaluates apps as they're being built for their Replit Agent product.

> Starting today, developers can build with the computer use beta on the Anthropic API, Amazon Bedrock, and Google Cloud's Vertex AI.

> To make these general skills possible, we've built an API that allows Claude to perceive and interact with computer interfaces. Developers can integrate this API to enable Claude to translate instructions ... into computer commands ...

> On OSWorld, which evaluates AI models' ability to use computers like people do, Claude 3.5 Sonnet scored 14.9% in the screenshot-only category—notably better than the next-best AI system's score of 7.8%. When afforded more steps to complete the task, Claude scored 22.0%.

> While we expect this capability to improve rapidly in the coming months, Claude's current ability to use computers is imperfect. Some actions that people perform effortlessly—scrolling, dragging, zooming—currently present challenges for Claude and we encourage developers to begin exploration with low-risk tasks. Because computer use may provide a new vector for more familiar threats such as spam, misinformation, or fraud, we're taking a proactive approach to promote its safe deployment. We've developed new classifiers that can identify when computer use is being used and whether harm is occurring.

- 其他数字: 升级版 Claude 3.5 Sonnet SWE-bench Verified 33.4%→49.0%；TAU-bench retail 62.6%→69.2%、airline 36.0%→46.0%（本文主文，与 computer use 相关但非核心维度，录作背景）

## 分节 E｜Google Project Mariner 官方博客一（官方声称）：Gemini 2.0 发布文

- URL: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/google-gemini-ai-update-december-2024/
- 抓取渠道: webfetch（Google 官方博客，The Keyword）
- 标题: Introducing Gemini 2.0: our new AI model for the agentic era
- 发布: 2024-12-11
- 作者: Sundar Pichai, Demis Hassabis, Koray Kavukcuoglu
- 来源性质: 官方声称（厂商自报）
- 正文要点（原文摘录）:

> Project Mariner is an early research prototype built with Gemini 2.0 that explores the future of human-agent interaction, starting with your browser. As a research prototype, it's able to understand and reason across information in your browser screen, including pixels and web elements like text, code, images and forms, and then uses that information via an experimental Chrome extension to complete tasks for you.

> When evaluated against the WebVoyager benchmark, which tests agent performance on end-to-end real world web tasks, Project Mariner achieved a state-of-the-art result of 83.5% working as a single agent setup.

> It's still early, but Project Mariner shows that it's becoming technically possible to navigate within a browser, even though it's not always accurate and slow to complete tasks today, which will improve rapidly over time.

> To build this safely and responsibly, we're conducting active research on new types of risks and mitigations, while keeping humans in the loop. For example, Project Mariner can only type, scroll or click in the active tab on your browser and it asks users for final confirmation before taking certain sensitive actions, like purchasing something.

> Trusted testers are starting to test Project Mariner using an experimental Chrome extension now, and we're beginning conversations with the web ecosystem in parallel.

- 其他背景: 同文中 Project Mariner 与 Project Astra、Jules 并列为 Gemini 2.0 时代 agentic 研究原型；安全段披露对 prompt injection 的对抗（"model learns to prioritize user instructions over 3rd party attempts at prompt injection"）

## 分节 F｜Google Project Mariner 官方博客二（官方声称）：Google I/O 2025 更新文

- URL: https://deepmind.google/blog/our-vision-for-building-a-universal-ai-assistant（原始域名 deepmind.google 路径；页面标题 "Our vision for building a universal AI assistant"，实际正文 canonical 为 blog.google/.../gemini-universal-ai-assistant/）
- 抓取渠道: webfetch（官方博客）
- 标题: Our vision for building a universal AI assistant
- 发布: 2025-05-20（Google I/O 2025）
- 作者: Demis Hassabis
- 来源性质: 官方声称（厂商自报）
- 正文要点（原文摘录）:

> We've also been exploring how agentic capabilities can help people multitask, with Project Mariner. This is a research prototype that explores the future of human-agent interaction, starting with browsers.

> Since launching Project Mariner last December, we've been working closely with a group of trusted testers to gather feedback and improve its experimental capabilities.

> Project Mariner now includes a system of agents that can complete up to ten different tasks at a time. These agents can help you look up information, make bookings, buy things, do research and more — all at the same time.

> The updated Project Mariner is available to Google AI Ultra subscribers in the U.S. We're bringing its computer use capabilities into the Gemini API, and we're planning to bring more of its capabilities to Google products throughout the year.

- 关键信息（官方声称）: 多 agent 系统（最多 10 个并行任务）；Google AI Ultra 美国订阅者可获取；computer use 能力进入 Gemini API 计划

## 访问记录

- 抓取时间: 2026-08-04（arXiv API 与官方页面均同日抓取）
- 抓取工具: arXiv 走 export.arxiv.org API（学术引擎）；官方页面走 webfetch
- 不可达记录: SearXNG（e.et:8388）Transport error；Bing 国内版 computer use 相关结果被本地法规移除；blog.google/technology/ai/project-mariner/ 404；任务给定 deepmind.google/technologies/project-mariner/ 重定向至 DeepMind 首页（内容不可得）

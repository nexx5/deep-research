# RAW-S001 原文存档

> 来源实体：assafelovic/gpt-researcher（GitHub 在线 README + release）
> 任务指派来源：assafelovic/deep-research —— 已确认该仓库不存在（GitHub 页面与 API 双 404）。经 GitHub API 检索验证，作者 assafelovic 名下真实存在的深度调研开源主项目为 gpt-researcher（官方描述 "An autonomous agent that conducts deep research on any data using any LLM providers"）。本 raw 存档即为该实体的原文。
> 抓取方式：webfetch GitHub 在线页面（https://github.com/assafelovic/gpt-researcher）+ GitHub API releases/latest
> 抓取日期：2026-08-04
> 当前版本：v3.6.0（release 发布于 2026-07-18）；stars 28.8k；forks 3.9k；commits 3,077；license Apache-2.0；language Python；官网 https://gptr.dev；docs https://docs.gptr.dev

---

## 一、README 原文（关键正文段，去导航噪音，保留原貌）

### 标题与定位

**GPT Researcher**

> GPT Researcher the first open deep research agent designed for both web and local research on any given task.

The agent produces detailed, factual, and unbiased research reports with citations. GPT Researcher provides a full suite of customization options to create tailor made and domain specific research agents. Inspired by the recent Plan-and-Solve and RAG papers, GPT Researcher addresses misinformation, speed, determinism, and reliability by offering stable performance and increased speed through parallelized agent work.

**Our mission is to empower individuals and organizations with accurate, unbiased, and factual information through AI.**

### Why GPT Researcher?

- Objective conclusions for manual research can take weeks, requiring vast resources and time.
- LLMs trained on outdated information can hallucinate, becoming irrelevant for current research tasks.
- Current LLMs have token limitations, insufficient for generating long research reports.
- Limited web sources in existing services lead to misinformation and shallow results.
- Selective web sources can introduce bias into research tasks.

### Install as Claude Skill

Extend Claude's deep research capabilities by installing GPT Researcher as a Claude Skill:

```
npx skills add assafelovic/gpt-researcher
```

Once installed, Claude can leverage GPT Researcher's deep research capabilities directly within your conversations.

### Architecture

The core idea is to utilize 'planner' and 'execution' agents. The planner generates research questions, while the execution agents gather relevant information. The publisher then aggregates all findings into a comprehensive report.

Steps:

- Create a task-specific agent based on a research query.
- Generate questions that collectively form an objective opinion on the task.
- Use a crawler agent for gathering information for each question.
- Summarize and source-track each resource.
- Filter and aggregate summaries into a final research report.

### Features

- 📝 Generate detailed research reports using web and local documents.
- 🖼️ Smart image scraping and filtering for reports.
- 🍌 **AI-generated inline images** using Google Gemini (Nano Banana) for visual illustrations.
- 📜 Generate detailed reports exceeding 2,000 words.
- 🌐 Aggregate over 20 sources for objective conclusions.
- 🖥️ Frontend available in lightweight (HTML/CSS/JS) and production-ready (NextJS + Tailwind) versions.
- 🔍 JavaScript-enabled web scraping.
- 📂 Maintains memory and context throughout research.
- 📄 Export reports to PDF, Word, and other formats.

### Getting Started（安装/依赖）

1. Install Python 3.11 or later.
2. Clone the project and navigate to the directory:
   ```
   git clone https://github.com/assafelovic/gpt-researcher.git
   cd gpt-researcher
   ```
3. Set up API keys by exporting them or storing them in a `.env` file:
   ```
   export OPENAI_API_KEY={Your OpenAI API Key here}
   export TAVILY_API_KEY={Your Tavily API Key here}
   ```
   (Optional) For enhanced tracing and observability, you can also set:
   ```
   # export LANGCHAIN_TRACING_V2=true
   # export LANGCHAIN_API_KEY={Your LangChain API Key here}
   ```
   For custom OpenAI-compatible APIs (e.g., local models, other providers), you can also set:
   ```
   export OPENAI_BASE_URL={Your custom API base URL here}
   ```
4. Install dependencies and start the server:
   ```
   pip install -r requirements.txt
   python -m uvicorn main:app --reload
   ```
   Visit http://localhost:8000 to start.

### Run as PIP package

```
pip install gpt-researcher
```

Example Usage:

```python
from gpt_researcher import GPTResearcher

query = "why is Nvidia stock going up?"
researcher = GPTResearcher(query=query)
# Conduct research on the given query
research_result = await researcher.conduct_research()
# Write the report
report = await researcher.write_report()
```

### MCP Client

GPT Researcher supports MCP integration to connect with specialized data sources like GitHub repositories, databases, and custom APIs. This enables research from data sources alongside web search.

```
export RETRIEVER=tavily,mcp  # Enable hybrid web + MCP research
```

```python
from gpt_researcher import GPTResearcher
import asyncio
import os

async def mcp_research_example():
    # Enable MCP with web search
    os.environ["RETRIEVER"] = "tavily,mcp"
    researcher = GPTResearcher(
        query="What are the top open source web research agents?",
        mcp_configs=[
            {
                "name": "github",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-github"],
                "env": {"GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")}
            }
        ]
    )
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    return report
```

### Inline Image Generation

GPT Researcher can automatically generate and embed AI-created illustrations in your research reports using Google's Gemini models (Nano Banana).

```
# Enable in your .env file
IMAGE_GENERATION_ENABLED=true
GOOGLE_API_KEY=your_google_api_key
IMAGE_GENERATION_MODEL=models/gemini-2.5-flash-image
```

When enabled, the system will:
1. Analyze your research context to identify visualization opportunities
2. Pre-generate 2-3 relevant images during the research phase
3. Embed them inline as the report is written

### Deep Research

GPT Researcher now includes Deep Research - an advanced recursive research workflow that explores topics with agentic depth and breadth. This feature employs a tree-like exploration pattern, diving deeper into subtopics while maintaining a comprehensive view of the research subject.

- 🌳 Tree-like exploration with configurable depth and breadth
- ⚡️ Concurrent processing for faster results
- 🤝 Smart context management across research branches
- ⏱️ Takes ~5 minutes per deep research
- 💰 Costs ~$0.4 per research (using `o3-mini` on "high" reasoning effort)

### Run with Docker

- Step 1: Install Docker
- Step 2: Clone the '.env.example' file, add your API Keys and save as '.env'
- Step 3: Within the docker-compose file comment out services that you don't want to run with Docker.
- Step 4: By default, this flow will start 2 processes: the Python server running on localhost:8000 and the React app running on localhost:3000.

```
docker-compose up --build
```

### Research on Local Documents

You can instruct the GPT Researcher to run research tasks based on your local documents. Currently supported file formats are: PDF, plain text, CSV, Excel, Markdown, PowerPoint, and Word documents.

Step 1: Add the env variable `DOC_PATH` pointing to the folder where your documents are located.
```
export DOC_PATH="./my-docs"
```

Step 2: If you're running the frontend app on localhost:8000, simply select "My Documents" from the "Report Source" Dropdown Options. If you're running the PIP package, pass the `report_source` argument as "local".

### MCP Server

> We've moved our MCP server to a dedicated repository: gptr-mcp (https://github.com/assafelovic/gptr-mcp).

The GPT Researcher MCP Server enables AI applications like Claude to conduct deep research. While LLM apps can access web search tools with MCP, GPT Researcher MCP delivers deeper, more reliable research results.

Features:
- Deep research capabilities for AI assistants
- Higher quality information with optimized context usage
- Comprehensive results with better reasoning for LLMs
- Claude Desktop integration

### Multi-Agent Assistant

As AI evolves from prompt engineering and RAG to multi-agent systems, we're excited to introduce multi-agent assistants built with LangGraph and AG2.

By using multi-agent frameworks, the research process can be significantly improved in depth and quality by leveraging multiple agents with specialized skills. Inspired by the recent STORM paper, this project showcases how a team of AI agents can work together to conduct research on a given topic, from planning to publication.

An average run generates a 5-6 page research report in multiple formats such as PDF, Docx and Markdown.

### Observability

GPT Researcher supports LangSmith for enhanced tracing and observability, making it easier to debug and optimize complex multi-agent workflows.

```
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=your_api_key
export LANGCHAIN_PROJECT="gpt-researcher"
```

All LangGraph-based agent interactions will be automatically traced and visualized in your LangSmith dashboard.

### Frontend Applications

- An intuitive interface for inputting research queries
- Real-time progress tracking of research tasks
- Interactive display of research findings
- Customizable settings for tailored research experiences

Two deployment options are available:
1. A lightweight static frontend served by FastAPI
2. A feature-rich NextJS application for advanced functionality

### Disclaimer（免责声明，官方原话）

This project, GPT Researcher, is an experimental application and is provided "as-is" without any warranty, express or implied. We are sharing codes for academic purposes under the Apache 2 license. Nothing herein is academic advice, and NOT a recommendation to use in academic or research papers.

Our view on unbiased research claims:

1. The main goal of GPT Researcher is to reduce incorrect and biased facts. How? We assume that the more sites we scrape the less chances of incorrect data. By scraping multiple sites per research, and choosing the most frequent information, the chances that they are all wrong is extremely low.
2. We do not aim to eliminate biases; we aim to reduce it as much as possible. **We are here as a community to figure out the most effective human/llm interactions.**
3. In research, people also tend towards biases as most have already opinions on the topics they research about. This tool scrapes many opinions and will evenly explain diverse views that a biased person would never have read.

---

## 二、Release v3.6.0 原文（GitHub API）

- tag: v3.6.0；published_at: 2026-07-18；pre-release: false
- 关键正文（节选）：
  - "Introducing a super stable version with enhanced improvements across security, stability and performance. We're also introducing a collaboration with Langchain with the latest deep agents framework here - https://github.com/assafelovic/gpt-researcher/tree/main/deep_agents"
  - security: sanitize untrusted content, add SECURITY.md, pin brotli (#1820)
  - Fix silently dropped token limits, real usage-based cost tracking, and research pipeline robustness (#1861)
  - Add Deep Agents example: GPT Researcher as the research engine in a LangChain deep agent (#1857)
  - Retriever hardening: 20 guard fixes against malformed results (#1907)
  - Scraper robustness: 6 fixes (title/PDF-detection/temp-file/dimensions) (#1908)
  - Multi-agent robustness: bound revision loops + exact sentinels (#1909)
  - feat: add Nebius Token Factory as LLM and embedding provider (#1891)
  - chore(multi_agents): nest AG2 variant under multi_agents/ag2 (#1912)

---

## 三、GitHub 仓库元数据（API）

- description: "An autonomous agent that conducts deep research on any data using any LLM providers"
- homepage: https://gptr.dev
- created_at: 2023-05-12
- pushed_at: 2026-07-18
- language: Python
- stargazers_count: 28,809（约 28.8k）
- forks_count: 3,886
- license: Apache-2.0
- topics: agent, ai, automation, deepresearch, llms, mcp, mcp-server, python, research, search, webscraping
- 顶层目录（README 页展示）：backend, deep_agents, docs, evals, frontend, gpt_researcher, mcp-server, multi_agents, skills/gpt-researcher, terraform, tests；根文件含 cli.py, langgraph.json, .mcp.json, Dockerfile, docker-compose.yml, Procfile

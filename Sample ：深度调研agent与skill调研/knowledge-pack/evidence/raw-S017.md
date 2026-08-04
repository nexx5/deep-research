---
source_id: S017
source_url: https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart
title: Gemini Fullstack LangGraph Quickstart
author: google-gemini（Google 官方 GitHub 组织）
date: 2025-05-22（仓库创建时间，GitHub API 确认）
fetched_at: 2026-08-04
content_type: github_repository
fetch_channel: GitHub API（api.github.com/repos）+ raw.githubusercontent.com（README 与源码）
note: 本 raw 存档由两部分组成——①GitHub API 返回的仓库元数据（独立可验证）；②README.md 全文（官方自我声称，经 raw.githubusercontent.com/main 分支抓取，与仓库 default_branch=main 一致）；③核心源码文件摘录（独立验证 agent 架构用）。README 正文未出现"Deep Research"字样，自述为"research-augmented conversational AI"示例。
---

# 一、仓库元数据（GitHub API 独立验证，2026-08-04 抓取）

```json
{
  "full_name": "google-gemini/gemini-fullstack-langgraph-quickstart",
  "description": "Get started with building Fullstack Agents using Gemini 2.5 and LangGraph",
  "owner": "google-gemini (Organization, GitHub id 161781182)",
  "created_at": "2025-05-22T11:59:02Z",
  "updated_at": "2026-08-04T07:44:31Z",
  "pushed_at": "2026-06-14T05:25:52Z",
  "stargazers_count": 18294,
  "forks_count": 3078,
  "open_issues_count": 77,
  "license": "Apache License 2.0 (spdx: Apache-2.0)",
  "language": "Jupyter Notebook",
  "topics": ["gemini", "gemini-api"],
  "homepage": "https://ai.google.dev/gemini-api/docs/google-search",
  "default_branch": "main",
  "archived": false,
  "fork": false
}
```

仓库文件清单（GitHub API git/trees/main?recursive=1 返回，blob 共 58 个，核心文件）：

```
README.md, LICENSE, Dockerfile, Makefile, docker-compose.yml, agent.png, app.png
backend/.env.example
backend/examples/cli_research.py
backend/langgraph.json
backend/pyproject.toml
backend/src/agent/app.py
backend/src/agent/configuration.py
backend/src/agent/graph.py
backend/src/agent/prompts.py
backend/src/agent/state.py
backend/src/agent/tools_and_schemas.py
backend/src/agent/utils.py
frontend/ (React+Vite+Tailwind+Shadcn UI 组件)
```

# 二、README.md 全文（官方自我声称，main 分支）

# Gemini Fullstack LangGraph Quickstart

This project demonstrates a fullstack application using a React frontend and a LangGraph-powered backend agent. The agent is designed to perform comprehensive research on a user's query by dynamically generating search terms, querying the web using Google Search, reflecting on the results to identify knowledge gaps, and iteratively refining its search until it can provide a well-supported answer with citations. This application serves as an example of building research-augmented conversational AI using LangGraph and Google's Gemini models.

## Features

- 💬 Fullstack application with a React frontend and LangGraph backend.
- 🧠 Powered by a LangGraph agent for advanced research and conversational AI.
- 🔍 Dynamic search query generation using Google Gemini models.
- 🌐 Integrated web research via Google Search API.
- 🤔 Reflective reasoning to identify knowledge gaps and refine searches.
- 📄 Generates answers with citations from gathered sources.
- 🔄 Hot-reloading for both frontend and backend during development.

## Project Structure

The project is divided into two main directories:

-   `frontend/`: Contains the React application built with Vite.
-   `backend/`: Contains the LangGraph/FastAPI application, including the research agent logic.

## Getting Started: Development and Local Testing

**1. Prerequisites:**

-   Node.js and npm (or yarn/pnpm)
-   Python 3.11+
-   **`GEMINI_API_KEY`**: The backend agent requires a Google Gemini API key.
    1.  Navigate to the `backend/` directory.
    2.  Create a file named `.env` by copying the `backend/.env.example` file.
    3.  Open the `.env` file and add your Gemini API key: `GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"`

**2. Install Dependencies:**

**Backend:** `cd backend; pip install .`

**Frontend:** `cd frontend; npm install`

**3. Run Development Servers:**

```bash
make dev
```
This will run the backend and frontend development servers. Open your browser and navigate to the frontend development server URL (e.g., `http://localhost:5173/app`).

_Alternatively, you can run the backend and frontend development servers separately. For the backend, open a terminal in the `backend/` directory and run `langgraph dev`. The backend API will be available at `http://127.0.0.1:2024`. It will also open a browser window to the LangGraph UI. For the frontend, open a terminal in the `frontend/` directory and run `npm run dev`. The frontend will be available at `http://localhost:5173`._

## How the Backend Agent Works (High-Level)

The core of the backend is a LangGraph agent defined in `backend/src/agent/graph.py`. It follows these steps:

1.  **Generate Initial Queries:** Based on your input, it generates a set of initial search queries using a Gemini model.
2.  **Web Research:** For each query, it uses the Gemini model with the Google Search API to find relevant web pages.
3.  **Reflection & Knowledge Gap Analysis:** The agent analyzes the search results to determine if the information is sufficient or if there are knowledge gaps. It uses a Gemini model for this reflection process.
4.  **Iterative Refinement:** If gaps are found or the information is insufficient, it generates follow-up queries and repeats the web research and reflection steps (up to a configured maximum number of loops).
5.  **Finalize Answer:** Once the research is deemed sufficient, the agent synthesizes the gathered information into a coherent answer, including citations from the web sources, using a Gemini model.

## CLI Example

For quick one-off questions you can execute the agent from the command line. The script `backend/examples/cli_research.py` runs the LangGraph agent and prints the final answer:

```bash
cd backend
python examples/cli_research.py "What are the latest trends in renewable energy?"
```

## Deployment

In production, the backend server serves the optimized static frontend build. LangGraph requires a Redis instance and a Postgres database. Redis is used as a pub-sub broker to enable streaming real time output from background runs. Postgres is used to store assistants, threads, runs, persist thread state and long term memory, and to manage the state of the background task queue with 'exactly once' semantics. For more details on how to deploy the backend server, take a look at the [LangGraph Documentation](https://langchain-ai.github.io/langgraph/concepts/deployment_options/). Below is an example of how to build a Docker image that includes the optimized frontend build and the backend server and run it via `docker-compose`.

_Note: For the docker-compose.yml example you need a LangSmith API key, you can get one from [LangSmith](https://smith.langchain.com/settings)._

_Note: If you are not running the docker-compose.yml example or exposing the backend server to the public internet, you should update the `apiUrl` in the `frontend/src/App.tsx` file to your host. Currently the `apiUrl` is set to `http://localhost:8123` for docker-compose or `http://localhost:2024` for development._

**1. Build the Docker Image:** `docker build -t gemini-fullstack-langgraph -f Dockerfile .`

**2. Run the Production Server:** `GEMINI_API_KEY=<your_gemini_api_key> LANGSMITH_API_KEY=<your_langsmith_api_key> docker-compose up`

Open your browser and navigate to `http://localhost:8123/app/` to see the application. The API will be available at `http://localhost:8123`.

## Technologies Used

- [React](https://reactjs.org/) (with [Vite](https://vitejs.dev/)) - For the frontend user interface.
- [Tailwind CSS](https://tailwindcss.com/) - For styling.
- [Shadcn UI](https://ui.shadcn.com/) - For components.
- [LangGraph](https://github.com/langchain-ai/langgraph) - For building the backend research agent.
- [Google Gemini](https://ai.google.dev/models/gemini) - LLM for query generation, reflection, and answer synthesis.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

# 三、核心源码摘录（独立验证，raw.githubusercontent.com/main 分支，2026-08-04 抓取）

## graph.py（agent 图结构核心）

```python
# Nodes
# generate_query: 用 ChatGoogleGenerativeAI(model=configurable.query_generator_model, temperature=1.0) 
#                  with_structured_output(SearchQueryList) 生成搜索查询
# continue_to_web_research: return [Send("web_research", {"search_query": q, "id": int(idx)}) for ...]
# web_research: genai_client.models.generate_content(model=..., config={"tools": [{"google_search": {}}], "temperature": 0})
#               从 response.candidates[0].grounding_metadata 提取引用
# reflection: llm.with_structured_output(Reflection) -> is_sufficient / knowledge_gap / follow_up_queries
# evaluate_research: if state["is_sufficient"] or research_loop_count >= max_research_loops: "finalize_answer" else Send(follow_up)
# finalize_answer: ChatGoogleGenerativeAI(model=reasoning_model, temperature=0) 合成答案 + 替换短 URL 回原 URL

builder = StateGraph(OverallState, config_schema=Configuration)
builder.add_node("generate_query", generate_query)
builder.add_node("web_research", web_research)
builder.add_node("reflection", reflection)
builder.add_node("finalize_answer", finalize_answer)
builder.add_edge(START, "generate_query")
builder.add_conditional_edges("generate_query", continue_to_web_research, ["web_research"])
builder.add_edge("web_research", "reflection")
builder.add_conditional_edges("reflection", evaluate_research, ["web_research", "finalize_answer"])
builder.add_edge("finalize_answer", END)
graph = builder.compile(name="pro-search-agent")
```

## configuration.py（默认配置）

```python
query_generator_model: str = "gemini-2.0-flash"   # 查询生成模型
reflection_model: str = "gemini-2.5-flash"         # 反思模型
answer_model: str = "gemini-2.5-pro"               # 最终答案模型
number_of_initial_queries: int = 3                 # 初始查询数
max_research_loops: int = 2                        # 最大研究循环数
```

## state.py（状态结构）

```python
class OverallState(TypedDict):
    messages, search_query, web_research_result, sources_gathered  # Annotated 累加
    initial_search_query_count: int
    max_research_loops: int
    research_loop_count: int
    reasoning_model: str
```

## prompts.py（四个指令模板：query_writer_instructions / web_searcher_instructions / reflection_instructions / answer_instructions）

关键指令要求摘录：
- query_writer: "Generate sophisticated and diverse web search queries... Don't produce more than {number_queries} queries... Query should ensure that the most current information is gathered. The current date is {current_date}."
- web_searcher: "Conduct targeted Google Searches to gather the most recent, credible information... Only include the information found in the search results, don't make up any information."
- reflection: "Identify knowledge gaps or areas that need deeper exploration and generate a follow-up query... If provided summaries are sufficient to answer the user's question, don't generate a follow-up query."
- answer: "Include the sources you used from the Summaries in the answer correctly, use markdown format (e.g. [apnews](https://vertexaisearch.cloud.google.com/id/1-0)). THIS IS A MUST."

## utils.py（引用处理）

```python
# resolve_urls: 将 grounding chunks 的原始 URI 映射为短 URL
#   prefix = f"https://vertexaisearch.cloud.google.com/id/"
#   resolved_map[url] = f"{prefix}{id}-{idx}"
# get_citations: 从 response.candidates[0].grounding_metadata.grounding_supports 提取
#   start_index / end_index / segments（label=web.title.split(".")[:-1][0], short_url, value=原始 uri）
# insert_citation_markers: 按 end_index 降序在文本中插入 "[label](short_url)" 引用标记
```

## pyproject.toml（后端依赖，backend/）

```toml
[project]
name = "agent"
version = "0.0.1"
authors = [{ name = "Philipp Schmid", email = "schmidphilipp1995@gmail.com" }]
license = { text = "MIT" }   # 注意：pyproject 声明 MIT，仓库根 LICENSE 为 Apache-2.0
requires-python = ">=3.11,<4.0"
dependencies = [
    "langgraph>=0.2.6", "langchain>=0.3.19", "langchain-google-genai",
    "python-dotenv>=1.0.1", "langgraph-sdk>=0.1.57", "langgraph-cli",
    "langgraph-api", "fastapi", "google-genai",
]
```

## langgraph.json（LangGraph 平台配置）

```json
{
  "dependencies": ["."],
  "graphs": { "agent": "./src/agent/graph.py:graph" },
  "http": { "app": "./src/agent/app.py:app" },
  "env": ".env"
}
```

## cli_research.py（CLI 入口，backend/examples/）

```python
# --initial-queries 默认 3, --max-loops 默认 2, --reasoning-model 默认 "gemini-2.5-pro-preview-05-06"
# state = {messages: [HumanMessage(question)], initial_search_query_count, max_research_loops, reasoning_model}
# result = graph.invoke(state); print(messages[-1].content)
```

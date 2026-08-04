---
source_id: S009
source_url: https://github.com/dzhng/deep-research
title: dzhng/deep-research (Open Deep Research) - GitHub 仓库
author: David Zhang (dzhng) / Duet
date: 2025-02-04（创建）
fetched_at: 2026-08-04
content_type: github_repo
---

# 原文存档说明

本存档为 dzhng/deep-research GitHub 仓库抓取记录，抓取日期 2026-08-04，渠道：
1. raw.githubusercontent.com/dzhng/deep-research/main/README.md（README 全文）
2. api.github.com/repos/dzhng/deep-research（仓库元数据，独立验证）
3. api.github.com/repos/dzhng/deep-research/releases?per_page=5（空数组：无正式 release）
4. api.github.com/repos/dzhng/deep-research/contents/ 与 /contents/src、/contents/src/ai（目录结构）
5. raw.githubusercontent.com/dzhng/deep-research/main/package.json、LICENSE、src/deep-research.ts、src/feedback.ts（源码/元数据）

注意：README 为官方自述；stars/forks/语言/许可证/创建时间等经 GitHub API 可独立确认；源码为公开可见实现。

---

## 一、README.md 全文（2026-08-04 抓取）

# Open Deep Research

An AI-powered research assistant that performs iterative, deep research on any topic by combining search engines, web scraping, and large language models.

The goal of this repo is to provide the simplest implementation of a deep research agent - e.g. an agent that can refine its research direction over time and deep dive into a topic. Goal is to keep the repo size at <500 LoC so it is easy to understand and build on top of.

If you like this project, please consider starring it and giving me a follow on X/Twitter (https://x.com/dzhng). This project is created by Duet (https://duet.so).

### How It Works（mermaid 流程图）

```
输入：User Query + Breadth Parameter + Depth Parameter
Deep Research → SERP Queries → Process Results
Results: Learnings + Directions
DP{depth > 0?}
RD["Next Direction: Prior Goals + New Questions + Learnings"]
MR[Markdown Report]
Q & B & D → DR；NL & ND → DP；DP Yes → RD → New Context → DR（循环）；DP No → MR
```

### Features

- **Iterative Research**: Performs deep research by iteratively generating search queries, processing results, and diving deeper based on findings
- **Intelligent Query Generation**: Uses LLMs to generate targeted search queries based on research goals and previous findings
- **Depth & Breadth Control**: Configurable parameters to control how wide (breadth) and deep (depth) the research goes
- **Smart Follow-up**: Generates follow-up questions to better understand research needs
- **Comprehensive Reports**: Produces detailed markdown reports with findings and sources
- **Concurrent Processing**: Handles multiple searches and result processing in parallel for efficiency

### Requirements

- Node.js environment
- API keys for:
  - Firecrawl API (for web search and content extraction)
  - OpenAI API (for o3 mini model)

### Setup

Node.js：clone 仓库 → npm install → 在 .env.local 中设置：

```
FIRECRAWL_KEY="your_firecrawl_key"
# 如使用自托管 Firecrawl，加：
# FIRECRAWL_BASE_URL="http://localhost:3002"
OPENAI_KEY="your_openai_key"
```

本地 LLM：注释 OPENAI_KEY，改用 OPENAI_ENDPOINT（本地服务器地址，如 "http://localhost:1234/v1"）和 OPENAI_MODEL（本地加载的模型名）。

Docker：clone → 重命名 .env.example 为 .env.local 并设置 key → docker build -f Dockerfile → docker compose up -d → docker exec -it deep-research npm run docker。

### Usage

```
npm start
```

交互式提示：输入研究查询 → 指定 breadth（推荐 3-10，默认 4）→ 指定 depth（推荐 1-5，默认 2）→ 回答追问以细化研究方向。

系统随后：1. 生成并执行搜索查询；2. 处理并分析搜索结果；3. 基于发现递归深入探索；4. 生成综合 Markdown 报告。

最终报告保存为工作目录下的 report.md 或 answer.md（取决于所选模式）。

### Concurrency

付费版或本地版 Firecrawl 可提高 CONCURRENCY_LIMIT 环境变量加速；免费版如遇限流可降到 1（但会慢很多）。

### DeepSeek R1

Deep research performs great on R1! 使用 Fireworks (http://fireworks.ai) 作为 R1 的主要 provider。设置 FIREWORKS_KEY 后系统自动切换为 R1 而非 o3-mini。

### Custom endpoints and models

另有 2 个可选环境变量可调整 endpoint（适配 OpenRouter 或 Gemini 等 OpenAI 兼容 API）及模型字符串：

```
OPENAI_ENDPOINT="custom_endpoint"
CUSTOM_MODEL="custom_model"
```

### How It Works（文字版）

1. **Initial Setup**：接收用户查询和研究参数（breadth & depth），生成追问问题以理解研究需求。
2. **Deep Research Process**：基于研究目标生成多条 SERP 查询；处理搜索结果提取关键 learnings；生成后续研究方向。
3. **Recursive Exploration**：若 depth > 0，取新研究方向继续探索；每次迭代构建于先前 learnings 之上；维持研究目标和发现上下文。
4. **Report Generation**：将全部发现汇编为综合 Markdown 报告，包含所有来源与引用。

### Community implementations

**Python**: https://github.com/Finance-LLMs/deep-research-python

### License

MIT License - feel free to use and modify as needed.

---

## 二、GitHub API 元数据（2026-08-04 独立验证）

- full_name: dzhng/deep-research
- description: "An AI-powered research assistant that performs iterative, deep research on any topic by combining search engines, web scraping, and large language models. The goal of this repo is to provide the simplest implementation of a deep research agent - e.g. an agent that can refine its research direction overtime and deep dive into a topic."
- 创建时间 created_at: 2025-02-04T01:27:56Z
- 最近推送 pushed_at: 2026-04-11T23:58:25Z
- 最近更新 updated_at: 2026-08-04T07:36:50Z
- stargazers_count: 19474
- forks_count: 1988
- watchers_count: 19474
- subscribers_count: 111
- open_issues_count: 93
- language: TypeScript
- license: MIT License (spdx_id: MIT)
- size: 74 KB
- topics: ["agent", "ai", "gpt", "o3-mini", "research"]
- default_branch: main
- archived: false
- releases: 空数组（无正式 release，按 per_page=5 查询）

## 三、仓库文件结构（2026-08-04 独立验证）

根目录：.env.example、.gitignore、.nvmrc、.prettierignore、Dockerfile、LICENSE、README.md、docker-compose.yml、package-lock.json、package.json、prettier.config.mjs、report.md（14.9KB 样例报告）、tsconfig.json、src/

src/：api.ts (2.4KB)、deep-research.ts (10.1KB)、feedback.ts (0.9KB)、prompt.ts (1.0KB)、run.ts (3.1KB)、ai/（providers.ts 2.6KB、text-splitter.ts 4.0KB、text-splitter.test.ts 2.5KB）

## 四、package.json（2026-08-04 独立验证）

- name: open-deep-research
- version: 0.0.1
- license: ISC（注意：与 LICENSE 文件的 MIT 不一致，客观记录）
- main: index.ts
- engines: node 22.x
- scripts: start = "tsx --env-file=.env.local src/run.ts"; api = "tsx --env-file=.env.local src/api.ts"; docker = "tsx src/run.ts"
- dependencies: @ai-sdk/fireworks ^0.1.14, @ai-sdk/openai ^1.1.9, @mendable/firecrawl-js ^1.16.0, ai ^4.1.17, cors ^2.8.5, express ^4.18.3, js-tiktoken ^1.0.17, lodash-es ^4.21.17, p-limit ^6.2.0, uuid ^9.0.1, zod ^3.24.1
- devDependencies: prettier, tsx, typescript, @types/* 等

## 五、LICENSE 文件（2026-08-04 独立验证）

MIT License, Copyright (c) 2025 David Zhang（标准 MIT 许可证全文）

## 六、核心源码摘录（src/deep-research.ts，2026-08-04 抓取）

### 导出类型与常量

```typescript
export type ResearchProgress = {
  currentDepth: number; totalDepth: number;
  currentBreadth: number; totalBreadth: number;
  currentQuery?: string; totalQueries: number; completedQueries: number;
};

// increase this if you have higher API rate limits
const ConcurrencyLimit = Number(process.env.FIRECRAWL_CONCURRENCY) || 2;

const firecrawl = new FirecrawlApp({
  apiKey: process.env.FIRECRAWL_KEY ?? '',
  apiUrl: process.env.FIRECRAWL_BASE_URL,
});
```

### generateSerpQueries（LLM 生成 SERP 查询）

输入 user query + 可选 learnings，输出最多 numQueries 条查询，每条含 query 和 researchGoal（说明该查询要达到的研究目标、如何深化、附加研究方向）。schema 为 zod 定义：queries: [{query, researchGoal}]。

### processSerpResult（处理搜索结果）

取 result.data 中每项的 markdown（经 trimPrompt 截断 25,000 字符），LLM 生成最多 numLearnings 条 learnings（要求信息密集、含实体/精确指标/数字/日期）和最多 numFollowUpQuestions 条后续问题。AbortSignal.timeout(60_000)（60 秒超时）。

### writeFinalReport / writeFinalAnswer

- writeFinalReport：LLM 生成 ≥3 页详细 Markdown 报告，要求包含全部 learnings；随后在文末附加 "## Sources" 段（visitedUrls 列表）。
- writeFinalAnswer：LLM 生成极简答案（通常几个词到一句话），遵守 prompt 指定格式（如 LaTeX 或选择题）。

### deepResearch（核心递归循环）

```typescript
export async function deepResearch({ query, breadth, depth, learnings = [], visitedUrls = [], onProgress }): Promise<ResearchResult> {
  // 1. 生成 SERP 查询：generateSerpQueries({ query, learnings, numQueries: breadth })
  // 2. pLimit(ConcurrencyLimit) 并发执行每条查询：
  //    - firecrawl.search(query, { timeout: 15000, limit: 5, scrapeOptions: { formats: ['markdown'] } })
  //    - newBreadth = Math.ceil(breadth / 2); newDepth = depth - 1;
  //    - processSerpResult 提取 learnings + followUpQuestions
  //    - allLearnings = [...learnings, ...newLearnings.learnings]; allUrls = [...visitedUrls, ...newUrls]
  //    - 若 newDepth > 0：构造 nextQuery（Previous research goal + Follow-up research directions），
  //      递归调用 deepResearch({ query: nextQuery, breadth: newBreadth, depth: newDepth, learnings: allLearnings, visitedUrls: allUrls })
  //    - 否则返回 { learnings: allLearnings, visitedUrls: allUrls }
  // 3. 汇总：learnings 与 visitedUrls 各取 Set 去重
}
```

关键实现事实（源码可见）：
- 单函数递归实现研究深化，无独立规划器/记忆模块；learnings 与 visitedUrls 数组随递归传递，无持久化。
- 搜索与抓取统一由 Firecrawl（search + markdown 抓取）承担，非自研爬虫。
- 并发度默认 2（FIRECRAWL_CONCURRENCY），搜索超时 15 秒，内容截断 25,000 字符，LLM 调用超时 60 秒。
- depth 递减 1，breadth 每层减半（向上取整）。

### feedback.ts（src/feedback.ts，全文核心）

generateFeedback({ query, numQuestions = 3 })：LLM 基于用户查询生成最多 numQuestions 个追问问题以澄清研究方向（zod schema: {questions: string[]}）。

## 七、报告输出形态（仓库自带 report.md，14.9KB）

仓库根目录含样例输出 report.md（14.9KB），具体内容未逐字存档（本次采录未读取全文，仅确认存在与大小）。

---

（存档结束，2026-08-04）

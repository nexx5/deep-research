---
source_id: S011
source_url: https://github.com/nickscamara/open-deep-research
title: nickscamara/open-deep-research（Open Deep Research）
author: nickscamara (Nicolas Camara)
date: 创建 2025-02-03；最后提交 2025-05-07；release v0.1 2025-02-12
fetched_at: 2026-08-04
content_type: github_repo
fetch_note: 通过「多源搜索」skill 的 GitHub API + raw.githubusercontent.com 渠道抓取（GitHub 页面 webfetch 直连超时）；含 README 全文、核心源码 route.ts 关键段、lib/ai、.env.example、package.json、LICENSE、releases/commits 元数据
---

# Open Deep Research（nickscamara/open-deep-research）原文存档

## 一、GitHub API 仓库元数据（2026-08-04 抓取，关键字段）

- full_name: nickscamara/open-deep-research
- description: "An open source deep research clone. AI Agent that reasons large amounts of web data extracted with Firecrawl"
- html_url: https://github.com/nickscamara/open-deep-research
- created_at: 2025-02-03T16:02:40Z
- pushed_at: 2025-05-07T15:38:28Z
- language: TypeScript
- stargazers_count: 6278
- forks_count: 746
- open_issues_count: 75
- subscribers_count: 29
- license: { key: "other", name: "Other", spdx_id: "NOASSERTION" }
- homepage: https://firecrawl.dev/extract
- default_branch: main
- archived: false

## 二、README.md 全文（英文原样）

```
# Open Deep Research

An Open-Source clone of Open AI's Deep Research experiment. Instead of using a fine-tuned version of o3, this method uses [Firecrawl's extract + search](https://firecrawl.dev/) with a reasoning model to deep research the web.

Check out the demo [here](https://x.com/nickscamara_/status/1886459999905521912)

## Features

- [Firecrawl](https://firecrawl.dev) Search + Extract
  - Feed realtime data to the AI via search
  - Extract structured data from multiple websites via extract
- [Next.js](https://nextjs.org) App Router
  - Advanced routing for seamless navigation and performance
  - React Server Components (RSCs) and Server Actions for server-side rendering and increased performance
- [AI SDK](https://sdk.vercel.ai/docs)
  - Unified API for generating text, structured objects, and tool calls with LLMs
  - Hooks for building dynamic chat and generative user interfaces
  - Supports OpenAI (default), Anthropic, Cohere, and other model providers
- [shadcn/ui](https://ui.shadcn.com)
  - Styling with [Tailwind CSS](https://tailwindcss.com)
  - Component primitives from [Radix UI](https://radix-ui.com) for accessibility and flexibility
- Data Persistence
  - [Vercel Postgres powered by Neon](https://vercel.com/storage/postgres) for saving chat history and user data
  - [Vercel Blob](https://vercel.com/storage/blob) for efficient file storage
- [NextAuth.js](https://github.com/nextauthjs/next-auth)
  - Simple and secure authentication

## Model Providers

This template ships with OpenAI `gpt-4o` as the default. However, with the [AI SDK](https://sdk.vercel.ai/docs), you can switch LLM providers to [OpenAI](https://openai.com), [Anthropic](https://anthropic.com), [Cohere](https://cohere.com/), and [many more](https://sdk.vercel.ai/providers/ai-sdk-providers) with just a few lines of code.

This repo is compatible with [OpenRouter](https://openrouter.ai/) and [OpenAI](https://openai.com/). To use OpenRouter, you need to set the `OPENROUTER_API_KEY` environment variable.

## Function Max Duration

By default, the function timeout is set to 300 seconds (5 minutes). If you're using Vercel's Hobby tier, you'll need to reduce this to 60 seconds. You can adjust this by changing the `MAX_DURATION` environment variable in your `.env` file:

```bash
MAX_DURATION=60
```

## Deploy Your Own

You can deploy your own version of the Next.js AI Chatbot to Vercel with one click:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fnickscamara%2Fopen-deep-research&env=AUTH_SECRET,OPENAI_API_KEY,OPENROUTER_API_KEY,FIRECRAWL_API_KEY,BLOB_READ_WRITE_TOKEN,POSTGRES_URL,UPSTASH_REDIS_REST_URL,UPSTASH_REDIS_REST_TOKEN,REASONING_MODEL,BYPASS_JSON_VALIDATION,TOGETHER_API_KEY,MAX_DURATION...)

## Running locally

1. Install Vercel CLI: `npm i -g vercel`
2. Link local instance with Vercel and GitHub accounts: `vercel link`
3. Download your environment variables: `vercel env pull`

# 1. First install all dependencies
pnpm install
# 2. Then run database migrations
pnpm db:migrate
# 3. Run the app
pnpm dev

Your app template should now be running on localhost:3000.

# Models dependencies

TogetherAI's Deepseek:
pnpm add @ai-sdk/togetherai

Note: Maximum rate limit https://docs.together.ai/docs/rate-limits

## Reasoning Model Configuration

The application uses a separate model for reasoning tasks (like research analysis and structured outputs). This can be configured using the `REASONING_MODEL` environment variable.

| Provider | Models | Notes |
|----------|--------|-------|
| OpenAI | gpt-4o, o1, o3-mini | Native JSON schema support |
| TogetherAI | deepseek-ai/DeepSeek-R1 | Requires BYPASS_JSON_VALIDATION=true |

### Important Notes

- Only certain OpenAI models (gpt-4o, o1, o3-mini) natively support structured JSON outputs
- Other models (deepseek-reasoner) can be used but may require disabling JSON schema validation
- When using models that don't support JSON schema: Set BYPASS_JSON_VALIDATION=true in your .env file. This allows non-OpenAI models to be used for reasoning tasks. Note: Without JSON validation, the model responses may be less structured
- The reasoning model is used for tasks that require structured thinking and analysis, such as: Research analysis / Document suggestions / Data extraction / Structured responses
- If no REASONING_MODEL is specified, it defaults to o1-mini
- If an invalid model is specified, it will fall back to o1-mini

### Usage

Add to your .env file:
# Choose one of: deepseek-reasoner, deepseek-ai/DeepSeek-R1
REASONING_MODEL=deepseek-ai/DeepSeek-R1
# Required when using models that don't support JSON schema (like deepseek-reasoner)
BYPASS_JSON_VALIDATION=true

The reasoning model is automatically used when the application needs structured outputs or complex analysis, regardless of which model the user has selected for general chat.
```

（README 中 Vercel 一键部署按钮 URL 含长串 env 参数，此处省略 URL 编码细节；公开图片 open-hero.png 等为仓库图片资源，未下载。）

## 三、核心源码摘录（raw.githubusercontent.com 抓取，2026-08-04）

### 3.1 app/(chat)/api/chat/route.ts（26195 字节，agent 主逻辑，关键段）

```typescript
import FirecrawlApp from '@mendable/firecrawl-js';

type AllowedTools = 'deepResearch' | 'search' | 'extract' | 'scrape';
const firecrawlTools: AllowedTools[] = ['search', 'extract', 'scrape'];
const allTools: AllowedTools[] = [...firecrawlTools, 'deepResearch'];

const app = new FirecrawlApp({ apiKey: process.env.FIRECRAWL_API_KEY || '' });

export async function POST(request: Request) {
  const maxDuration = process.env.MAX_DURATION ? parseInt(process.env.MAX_DURATION) : 300;
  // 请求体: { id, messages, modelId, reasoningModelId, experimental_deepResearch = false }
  // ... 匿名会话创建、用户校验、Upstash 限流（rateLimiter.limit(identifier) → 429）...
  const model = models.find((model) => model.id === modelId);
  const reasoningModel = reasoningModels.find((model) => model.id === reasoningModelId);

  return createDataStreamResponse({
    execute: (dataStream) => {
      const result = streamText({
        // Router model
        model: customModel(model.apiIdentifier, false),
        system: systemPrompt,
        messages: coreMessages,
        maxSteps: 10,
        experimental_activeTools: experimental_deepResearch ? allTools : firecrawlTools,
        tools: {
          search: {
            description: "Search for web pages. Normally you should call the extract tool after this one...",
            parameters: z.object({ query: z.string(), maxResults: z.number().optional().describe('... (default 10)') }),
            execute: async ({ query, maxResults = 5 }) => {
              const searchResult = await app.search(query);
              // 给结果加 favicon: https://www.google.com/s2/favicons?domain=...
            },
          },
          extract: {
            description: 'Extract structured data from web pages. Use this to get whatever data you need from a URL...',
            parameters: z.object({ urls: z.array(z.string()), prompt: z.string() }),
            execute: async ({ urls, prompt }) => {
              const scrapeResult = await app.extract(urls, { prompt });
            },
          },
          scrape: {
            description: 'Scrape web pages. Use this to get from a page when you have the url.',
            parameters: z.object({ url: z.string() }),
            execute: async ({ url }) => {
              const scrapeResult = await app.scrapeUrl(url);
              // 返回 scrapeResult.markdown
            },
          },
          deepResearch: {
            description: 'Perform deep research on a topic using an AI agent that coordinates search, extract, and analysis tools with reasoning steps.',
            parameters: z.object({ topic: z.string() }),
            execute: async ({ topic, maxDepth = 7 }) => {
              const startTime = Date.now();
              const timeLimit = 4.5 * 60 * 1000; // 4 minutes 30 seconds
              const researchState = {
                findings: [], summaries: [], nextSearchTopic: '',
                urlToSearch: '', currentDepth: 0,
                failedAttempts: 0, maxFailedAttempts: 3,
                completedSteps: 0, totalExpectedSteps: maxDepth * 5,
              };
              // dataStream 事件: progress-init / source-delta / activity-delta / depth-delta / finish

              const analyzeAndPlan = async (findings) => {
                // 用 reasoning 模型 generateText，prompt 要求返回精确 JSON:
                // { "analysis": { "summary", "gaps", "nextSteps", "shouldContinue", "nextSearchTopic", "urlToSearch" } }
                // 若剩余时间 < 1 分钟则 shouldContinue=false；信息足够则 shouldContinue=false
              };

              const extractFromUrls = async (urls) => {
                // 对每个 URL 并行 app.extract([url], { prompt: 'Extract key information about {topic}. Focus on facts, data, and expert opinions...' })
              };

              while (researchState.currentDepth < maxDepth) {
                if (Date.now() - startTime >= timeLimit) break;
                researchState.currentDepth++;
                // Search phase: app.search(searchTopic)
                //   失败: failedAttempts++, >=3 则 break
                // Extract phase: topUrls = searchResult.data.slice(0, 3).map(url); 加 researchState.urlToSearch
                // Analysis phase: analyzeAndPlan(findings) → nextSearchTopic / urlToSearch / summary
                //   analysis 为 null: failedAttempts++, >=3 则 break
                //   if (!analysis.shouldContinue || analysis.gaps.length === 0) break;
                //   topic = analysis.gaps.shift() || topic;
              }
              // Final synthesis: generateText({ model: reasoningModel, maxTokens: 16000,
              //   prompt: 'Create a comprehensive long analysis of {topic} based on these findings: ... Include citations to sources where appropriate. It is expected to be very long, detailed and comprehensive.' })
            },
          },
        },
        onFinish: async ({ response }) => { /* saveMessages 持久化 */ },
        experimental_telemetry: { isEnabled: true, functionId: 'stream-text' },
      });
      result.mergeIntoDataStream(dataStream);
    },
  });
}
```

### 3.2 lib/ai/index.ts（全文）

```typescript
import { openai } from '@ai-sdk/openai';
import { experimental_wrapLanguageModel as wrapLanguageModel } from 'ai';
import { openrouter } from '@openrouter/ai-sdk-provider';
import { togetherai } from '@ai-sdk/togetherai';
import { customMiddleware } from "./custom-middleware";

const VALID_REASONING_MODELS = ['o1', 'o1-mini', 'o3-mini', 'deepseek-ai/DeepSeek-R1', 'gpt-4o'] as const;
const JSON_SUPPORTED_MODELS = ['gpt-4o', 'gpt-4o-mini'] as const;

const REASONING_MODEL = process.env.REASONING_MODEL || 'o1-mini';
const BYPASS_JSON_VALIDATION = process.env.BYPASS_JSON_VALIDATION === 'true';

function getReasoningModel(modelId: string) {
  if (VALID_REASONING_MODELS.includes(modelId)) return modelId;
  const configuredModel = REASONING_MODEL;
  if (!VALID_REASONING_MODELS.includes(configuredModel)) { /* warn */ return 'o1-mini'; }
  if (!BYPASS_JSON_VALIDATION && !supportsJsonOutput(configuredModel)) { /* warn */ }
  return configuredModel;
}

export const customModel = (apiIdentifier: string, forReasoning: boolean = false) => {
  const hasOpenRouterKey = process.env.OPENROUTER_API_KEY && process.env.OPENROUTER_API_KEY !== "****";
  const modelId = forReasoning ? getReasoningModel(apiIdentifier) : apiIdentifier;
  if (hasOpenRouterKey) return wrapLanguageModel({ model: openrouter(modelId), middleware: customMiddleware });
  const model = modelId === 'deepseek-ai/DeepSeek-R1' ? togetherai(modelId) : openai(modelId);
  return wrapLanguageModel({ model, middleware: customMiddleware });
};
```

### 3.3 lib/ai/models.ts（全文）

```typescript
export interface Model { id: string; label: string; apiIdentifier: string; description: string; }

export const models = [
  { id: 'gpt-4o', label: 'GPT 4o', apiIdentifier: 'gpt-4o', description: 'For complex, multi-step tasks' },
  { id: 'gpt-4o-mini', label: 'GPT 4o Mini', apiIdentifier: 'gpt-4o-mini', description: 'Affordable for complex, multi-step tasks' },
] as const;

export const reasoningModels = [
  { id: 'o1', label: 'o1', apiIdentifier: 'o1', description: 'For deep reasoning and complex, multi-step tasks' },
  { id: 'o1-mini', label: 'o1-mini', apiIdentifier: 'o1-mini', description: '... cheaper.' },
  { id: 'o3-mini', label: 'o3-mini', apiIdentifier: 'o3-mini', description: '... cheaper.' },
] as const;

export const DEFAULT_MODEL_NAME: string = 'gpt-4o';
export const DEFAULT_REASONING_MODEL_NAME: string = 'o1';
```

### 3.4 .env.example（全文）

```
OPENAI_API_KEY=****
OPENROUTER_API_KEY=****
FIRECRAWL_API_KEY=****
AUTH_SECRET=****
MAX_DURATION=60
BLOB_READ_WRITE_TOKEN=****
POSTGRES_URL=****
UPSTASH_REDIS_REST_URL=****
UPSTASH_REDIS_REST_TOKEN=****
# REASONING_MODEL=deepseek-reasoner
BYPASS_JSON_VALIDATION=false
TOGETHER_API_KEY=****
```

### 3.5 package.json（依赖要点）

- name: "ai-chatbot", version: "0.1.0"
- 关键运行时依赖：ai 4.1.16、@ai-sdk/openai 1.1.9、@ai-sdk/deepseek ^0.1.8、@ai-sdk/togetherai ^0.1.9、@openrouter/ai-sdk-provider ^0.2.0、@mendable/firecrawl-js ^1.15.7、next 15.0.3-canary.2、next-auth 5.0.0-beta.25、drizzle-orm ^0.34.0、@vercel/postgres ^0.10.0、@vercel/blob ^0.24.1、@upstash/ratelimit ^2.0.5、@upstash/redis ^1.34.3、react 19.0.0-rc、zod ^3.23.8、prosemirror 系列、@codemirror 系列
- scripts: dev/build/start、db:generate/db:migrate/db:studio 等（drizzle-kit）

### 3.6 LICENSE（全文）

```
Copyright 2024 Vercel, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## 四、Releases 与提交记录（GitHub API，2026-08-04）

### Releases（仅 1 个）

- tag: v0.1（2025-02-12 published）
- name: "Introducing Search Mode"
- body 要点：新增普通搜索模式与深度研究切换；支持选择不同 router 与 reasoning 模型；含 PR #3/#4/#6/#5（支持 OpenRouter、Deepseek R1 Reasoning Model 与 UI 模型选择等社区贡献）；视频 https://x.com/nickscamara_/status/1889711210066854240

### 提交记录（最近 8 条）

- 2025-05-07 "Update README.md"（最后提交）
- 2025-05-07 "Nick:"
- 2025-05-07 "Update README.md"
- 2025-02-23 "(update) model selector correctly sets the reasoning model 🤖 (#52)"（社区贡献）
- 2025-02-13 前后多条（README 更新 / Fixed a few issues / Update page.tsx）

## 五、仓库目录结构要点（git trees API）

- app/(chat)/api/chat/route.ts（26195B，核心）
- app/(chat)/api/document|files/upload|history|suggestions|vote（辅助 API）
- components/：deep-research.tsx、search-results.tsx、extract-results.tsx、scrape-results.tsx、activity 面板相关、spreadsheet-editor.tsx、editor.tsx（ProseMirror 文档/表格编辑）、weather.tsx（模板示例）
- lib/ai/：index.ts、models.ts、prompts.ts、custom-middleware.ts
- lib/db/：schema.ts、queries.ts、migrate.ts、migrations/（0000-0005）
- lib/：deep-research-context.tsx（5760B）、rate-limit.ts、utils.ts、types.ts、spreadsheet.ts、editor/
- Dockerfile、docker-compose.yml、start.sh（自部署）

# 采录文件格式标准

> 版本：2.0
> 日期：2026-08-02
> 定位：**key_claims 格式的单一权威定义**。所有采录/分析 prompt 模板、03-分析提取.md、knowledge-ingest 解析都必须以本文件为准，不得各自再定义。
> 变更：v1.0 用 bullet + `**CL{id}**` 前缀，导致 4 种格式变体、合并员每次重写解析器。v2.0 统一为 SPO 表格。

## raw-S*.md（原始捕获）

```markdown
---
source_id: S0001
source_url: https://example.com/article
title: 文章标题
author: 作者
date: 2026-03-23
fetched_at: 2026-07-06T10:00:00
content_type: web_page | github_repo | paper | official_doc | community_post
---

（原始正文内容，尽量保留完整）
```

## 采录-S*.md（证据化摘录+断言提取）

```markdown
---
source_id: S0001
extraction_level: light | deep
model_used: qwen3.6-27b | deepseek-v4-flash | glm-5.2
extracted_at: 2026-07-06T10:05:00
discovered_via: "搜索词/线索来源"   # provenance溯源链：这个来源是通过什么搜索词/什么线索发现的（必填）
discovered_from: "LD000001 | 手动 | 跨项目 | 引用追溯"  # 发现渠道（线索ID/手动添加/跨项目复用/引用追溯）
---

## 摘要

（一句话概括本文核心内容）

## key_claims

> **格式权威：见 standards/extraction-format.md（本文件），唯一格式，禁止 bullet 前缀、禁止 CL 预占位。**
> 每条断言 = 主体 + 关系 + 客体 + 边界条件 + 置信度 + 来源。一行一断言。
> claim_id 不在采录阶段预占——知识管理员 ingest 时统一分配 CLxxxxx，本表用 # 序号。

| # | subject | predicate | object | boundary | confidence | sources | characteristics |
|---|---|---|---|---|---|---|---|
| 1 | 知识图谱 | 优于 | 纯向量检索 | 需要跨步追踪信息变化的多跳推理 | H | S0048 | 知识图谱,多跳推理 |
| 2 | RedFoxHub | 提供 | 微信公众号正文读取路径 | 使用第三方数据源且RedFoxHub数据来源合规 | M | S0062 | 第三方数据源,微信生态 |

字段约束：
- `#`：表内序号（1,2,3...），不是 claim_id
- `subject/predicate/object`：简洁概念/关系/客体，**不是完整句子**（❌"知识图谱优于纯向量检索..."）
- `boundary`：在什么条件下成立，禁止空（写"未明确"也比空好）
- `confidence`：H=多源交叉验证 / M=单源但来源可信 / L=推测/二手转述（也可填 0.0-1.0）
- `sources`：来源 S-id（可多个用逗号），来自本文件 source_id
- `characteristics`：特点标签逗号分隔（跨源关联依赖，必填）

## evidence

（证据链详情，每条证据指向原文位置）

### 证据1
- source: S0001
- location: L45-52
- quote: "原文摘录..."
- context: 该结论在原文中的论证上下文

## characteristics

（本文涉及的主要特点标签）

- 向量检索
- 需embedding服务
- 语义匹配

## possible_relations

（弱模型推断的可能关联，不读全局）

- 与纯文件检索方案可能对立
- 与知识图谱方案可能互补

## discovered_leads

（线索识别结果，每条线索格式：）

- LD000001 | 新采集 | 论文 | "Mem0: ..." | context: "..." | priority: P0
- LD000002 | 新采集 | 仓库 | github.com/mem0ai/mem0 | context: "..." | priority: P1
```

## 分析-A*.md（单源分析）

```markdown
---
source_id: S0001
analysis_id: A0001
model_used: qwen3.6-27b
analyzed_at: 2026-07-06T10:10:00
---

## summary

（单源分析摘要：本文讲了什么，核心论点是什么）

## key_claims

> **格式权威：见 standards/extraction-format.md，唯一格式。**
> 分析档 key_claims 在采录档基础上加 `analysis_note` 列（本文对此断言的论证强度/局限性）。

| # | subject | predicate | object | boundary | confidence | sources | characteristics | analysis_note |
|---|---|---|---|---|---|---|---|---|
| 1 | 知识图谱 | 优于 | 纯向量检索 | 多跳推理场景 | H | S0048 | 知识图谱,多跳推理 | 强论证：有HotpotQA实验数据支撑 |
| 2 | RedFoxHub | 提供 | 微信公众号正文读取 | 使用第三方数据源 | M | S0062 | 第三方数据源 | 中等论证：逻辑推导但缺实测 |

## characteristics

（本文方案/观点的特点标签）

## opposing_to

（本文观点可能与哪些特点的观点对立）

- 与"纯文件检索"特点的方案可能对立，因为本文主张向量检索的语义优势
```

## 格式约定

1. frontmatter使用YAML格式，三横线包围
2. 正文使用Markdown，key_claims 必须用 SPO 表格（一行一断言）
3. 文件编码UTF-8无BOM
4. 换行符LF
5. claim_id 不在采录/分析阶段预占——知识管理员 ingest 时统一分配 CLxxxxx 并回写 `db_claim_id`（见 03-分析提取.md 的 extracted_claims_confirmation 段）

# 单源分析模板

> 用途：对采录文件做单源分析，产出分析-A*.md
> 模型：弱模型（qwen3.6-27b / deepseek-v4-flash）
> 约束：基于采录内容分析，不补充文章未提及的信息

## 输入

- 采录-S*.md文件内容（含key_claims, evidence, characteristics, possible_relations）

## 分析要求

### 1. summary（分析摘要）

概括本文的核心论点和论证逻辑，不超过100字。重点说明：
- 本文主张什么
- 用什么证据支撑
- 在什么边界下成立

### 2. key_claims（核心断言）

> **格式权威：见 standards/extraction-format.md，唯一格式，禁止 bullet 前缀、禁止 CL 预占位。**
> 深量档分析档表格在采录档基础上加 `analysis_note` 列（本文对此断言的论证强度/局限性）。

从采录中提炼核心断言，加分析视角的判断：

每条断言 analysis_note 候选值：
- "强论证：有实验数据支撑"
- "中等论证：有逻辑推导但缺数据"
- "弱论证：仅作者观点无支撑"

### 3. characteristics（特点标签）

本文方案/观点的特点标签，用于跨源关联。

### 4. opposing_to（可能对立）

本文观点可能与哪些特点的观点对立：
- "与{纯文件检索}特点的方案可能对立，因为本文主张向量检索的语义优势"
- 列出2-3个可能对立的方向

## 输出格式

按分析-A*.md格式输出：

```markdown
---
source_id: {从采录文件提取}
analysis_id: A{id}
model_used: {模型名}
analyzed_at: {ISO时间}
---

## summary

{分析摘要}

## key_claims

| # | subject | predicate | object | boundary | confidence | sources | characteristics | analysis_note |
|---|---|---|---|---|---|---|---|---|
| 1 | 知识图谱 | 优于 | 纯向量检索 | 多跳推理场景 | H | S0048 | 知识图谱,多跳推理 | 强论证：有HotpotQA实验数据支撑 |
| 2 | RedFoxHub | 提供 | 微信公众号正文读取 | 使用第三方数据源 | M | S0062 | 第三方数据源 | 中等论证：逻辑推导但缺实测 |

## characteristics

- {特点1}
- {特点2}

## opposing_to

- 与{某特点}方案可能对立，因为{理由}
```

## 禁止行为

- 不要用 bullet + `**CL{id}**` 前缀格式（已废弃，v2.0 统一 SPO 表格，分析档加 analysis_note 列）
- 不要在表格里预占 CL 编号（CL id 由知识管理员 ingest 分配）
- 不要补充文章未提及的信息
- 不要做跨源对比（那是知识管理员的事）
- 不要评判对错（只标注论证强度）

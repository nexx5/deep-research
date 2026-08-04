---
source_id: S027
source_url: https://arxiv.org/abs/2601.08536
title: "DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Report"
author: "Ruizhe Li, Mingxuan Du, Benfeng Xu, Chiwei Zhu, Xiaorui Wang, Zhendong Mao"
date: 2026-01-13
updated: 2026-01-30
version: v2
fetched_at: 2026-08-04T09:20:00
content_type: paper
arxiv_id: 2601.08536
categories: cs.CL
---

# raw 原文存档：DeepResearch Bench II

> 获取渠道：arXiv API（https://export.arxiv.org/api/query?id_list=2601.08536），多源搜索 skill 学术引擎
> 原文为 arXiv Atom XML <entry> 内容，以下保留摘要英文原文与元数据；未获取全文 PDF 正文。

## 元数据

- 标题（原文）：DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Report
- 作者（原文）：Ruizhe Li, Mingxuan Du, Benfeng Xu, Chiwei Zhu, Xiaorui Wang, Zhendong Mao
- arXiv ID：2601.08536
- 版本：v2（updated 2026-01-30T14:15:10Z）
- 首次发布：published 2026-01-13T13:18:39Z
- 主分类：cs.CL
- 摘要页：https://arxiv.org/abs/2601.08536v2
- PDF：https://arxiv.org/pdf/2601.08536v2

## 摘要（英文原文，一字未改）

Deep Research Systems (DRS) aim to help users search the web, synthesize information, and deliver comprehensive investigative reports. However, how to rigorously evaluate these systems remains under-explored. Existing deep-research benchmarks often fall into two failure modes. Some do not adequately test a system's ability to analyze evidence and write coherent reports. Others rely on evaluation criteria that are either overly coarse or directly defined by LLMs (or both), leading to scores that can be biased relative to human experts and are hard to verify or interpret. To address these issues, we introduce Deep Research Bench II, a new benchmark for evaluating DRS-generated reports. It contains 132 grounded research tasks across 22 domains; for each task, a system must produce a long-form research report that is evaluated by a set of 9430 fine-grained binary rubrics in total, covering three dimensions: information recall, analysis, and presentation. All rubrics are derived from carefully selected expert-written investigative articles and are constructed through a four-stage LLM+human pipeline that combines automatic extraction with over 400 human-hours of expert review, ensuring that the criteria are atomic, verifiable, and aligned with human expert judgment. We evaluate several state-of-the-art deep-research systems on Deep Research Bench II and find that even the strongest models satisfy fewer than 50% of the rubrics, revealing a substantial gap between current DRSs and human experts.

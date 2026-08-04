---
source_id: S029
source_url: https://arxiv.org/abs/2607.04718
title: "FORGE: Research-Trajectory Hijacking Attacks on Deep Research Agents（轨迹劫持）；Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions（误导知识）；Search-Time Contamination in Deep Research Agents（搜索时污染）"
author: "Yue Pan, Ziheng Zhang, Junxiang Lei, Changhao Jia, Qingyi Si, Hongcheng Guo；Pengyu Zhu, Lijun Li, Longju Yang, Sen Su, Jing Shao；Yongjie Wang, Xinyue Zhang, Kunhong Yao, Zhiwei Zeng, Kaisong Song, Jun Lin, Zhiqi Shen"
date: 2026-06-03
fetched_at: 2026-08-04T09:20:00
content_type: paper
---

# S029：三项深度调研安全/可靠性学术证据（轨迹劫持 + 误导知识 + 搜索时污染）

> 采集说明：本 raw 文件含三篇 arXiv 预印本，均于 Batch 3 采录引用可靠性证据（S024）时顺带发现，属深度调研 agent 已知局限/失败场景/攻击面证据（limitation 节点 + 安全维度）：
> 1. FORGE（arXiv 2607.04718，2026-07，轨迹劫持攻击）
> 2. MisKnow-Agent（arXiv 2607.20891，2026-07，误导知识注入）
> 3. Search-Time Contamination（arXiv 2606.05241，2026-06，搜索时基准污染）
> 内容由多源搜索 skill 学术引擎（arXiv API）直接返回元数据与摘要，摘要即原文。客观记录，不评判。

---

## 论文一：FORGE: Research-Trajectory Hijacking Attacks on Deep Research Agents

- **arXiv ID**: 2607.04718v1
- **URL**: https://arxiv.org/abs/2607.04718
- **PDF**: https://arxiv.org/pdf/2607.04718v1
- **作者**: Yue Pan, Ziheng Zhang, Junxiang Lei, Changhao Jia, Qingyi Si, Hongcheng Guo
- **发布**: 2026-07-06T06:43:21Z
- **分类**: cs.AI
- **arxiv comment**: 20 pages, 8 figures, Code available at https://github.com/yvepan/FORGE
- **获取渠道**: arXiv API（多源搜索 skill 学术引擎），2026-08-04

### 摘要（原文）

Deep research agents decompose open-ended queries into subtasks, retrieve web evidence over multiple rounds, and synthesize long-form reports. This workflow creates a planning-layer poisoning surface: adversarial documents that enter the retrieval pool can steer follow-up questions and turn a local injection into report-level contamination. We present FORGE (Fabricated Orchestrated Reasoning chain for aGent Exploitation), a two-level attack that combines intra-document reasoning fabrication with inter-document chain coordination to hijack subtask planning. We further introduce the PRISM metric, which weights infected report claims by cognitive type, and Root Query Anchoring, a lightweight defense that ties recursive follow-up generation to the root query. Across 25 queries, Network FORGE reaches 26.4% PRISM with five injected documents and exhibits depth migration, in which recursive synthesis shifts poisoned content from overt framing into factual premises. On the 10-query defense subset, RQA (Root Query Anchoring) reduces PRISM from 38.5% to 18.3%.

---

## 论文二：Is Deep Research Reliable? Misleading Knowledge Induces False Conclusions（MisKnow-Agent）

- **arXiv ID**: 2607.20891v2
- **URL**: https://arxiv.org/abs/2607.20891
- **PDF**: https://arxiv.org/pdf/2607.20891v2
- **作者**: Pengyu Zhu, Lijun Li, Longju Yang, Sen Su, Jing Shao
- **发布**: 2026-07-23T03:28:08Z（v2 更新 2026-07-30T04:45:04Z）
- **分类**: cs.AI
- **代码**: https://github.com/whfeLingYu/MisKnow-Agent
- **数据集**: https://huggingface.co/datasets/whfeLingYu/Misleading_Knowledge
- **获取渠道**: arXiv API（多源搜索 skill 学术引擎），2026-08-04

### 摘要（原文）

Deep Research agents conduct long-horizon investigations by iteratively planning, retrieving evidence, and generating reports. However, it remains unclear whether they can resist apparently credible but factually false information introduced into these workflows. To study this failure mode, we introduce MisKnow-Agent, a controlled evaluation framework that constructs task-specific documents supporting manually audited false conclusions with controlled authority cues and source styles. Applied to the tasks from DeepResearch Bench, it generates 5,933 misleading documents after filtering. We evaluate DeerFlow and WebThinker with three backbone LLMs, together with Gemini Deep Research, using a report-level false-conclusion adoption rate (FCAR) that counts only reports endorsing the false conclusion. Across the configurations, introducing one misleading document increases the mean FCAR from 0\% in the no-injection control to 54.7\%. FCAR varies substantially with lifecycle stage and framework design, and also with source authority and presentation style, whereas search-result rank and additional documents beyond the first have limited influence. Although cross-model verification consistently classifies retained instances as misleading, Deep Research agents can still adopt the corresponding false conclusions during long-horizon research. Pre- and post-research defenses reduce FCAR but do not eliminate adoption, motivating continuous verification when evidence enters intermediate research states and final synthesis. To facilitate reproducibility, our code and dataset are publicly available at https://github.com/whfeLingYu/MisKnow-Agent and https://huggingface.co/datasets/whfeLingYu/Misleading_Knowledge, respectively.

---

## 论文三：Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation

- **arXiv ID**: 2606.05241v1
- **URL**: https://arxiv.org/abs/2606.05241
- **PDF**: https://arxiv.org/pdf/2606.05241v1
- **作者**: Yongjie Wang, Xinyue Zhang, Kunhong Yao, Zhiwei Zeng, Kaisong Song, Jun Lin, Zhiqi Shen
- **发布**: 2026-06-03T07:11:36Z
- **分类**: cs.CR（主）、cs.AI
- **arxiv comment**: Under Review
- **获取渠道**: arXiv API（多源搜索 skill 学术引擎），2026-08-04

### 摘要（原文）

Public benchmarks enable fair and reproducible evaluation of LLM reasoning, but they become fragile for deep research agents that actively search the web during inference. Such agents may retrieve public benchmark metadata, question context, or even ground-truth answers via web search. This gives rise to Search-Time Contamination (STC), where external retrieval bypasses intended reasoning and inflates measured performance. We systematically study STC in deep research agent evaluation. We define three contamination types with increasing severity, namely Benchmark Metadata Leakage, Question-Context Leakage, and Explicit Answer Leakage, and develop detection algorithms to identify them and quantify their impact on agent performance. Evaluating modern deep research agents on six public benchmarks, we find that STC is widespread and can inflate performance by up to 4%. Our findings show that existing evaluations may overestimate true reasoning ability. We therefore advocate contamination-aware practices, including isolated sandboxes, transparent search trajectories, and controlled benchmark access.

---
> 不可变记录。后续分析不修改此文件。

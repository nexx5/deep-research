---
source_id: S024
source_url: https://arxiv.org/abs/2604.03173
title: "Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents（引用幻觉审计）；Deep-Research Agents Can Be Poisoned via User-Generated Content（UGC污染漏洞）"
author: "Delip Rao, Eric Wong, Chris Callison-Burch；Tingwei Zhang, Harold Triedman, Vitaly Shmatikov"
date: 2026-04-03
fetched_at: 2026-08-04T09:10:00
content_type: paper
---

# S024：两项学术证据（引用幻觉审计 + UGC 污染漏洞）

> 采集说明：本 raw 文件含两篇 arXiv 预印本。第一项为任务指定主来源（arXiv 2604.03173，引用幻觉审计论文）；第二项为任务要求搜索定位的 Cornell Tech 2026-05 preprint（污染漏洞论文，arXiv 2605.24245）。内容由多源搜索 skill 学术引擎（arXiv API）直接返回元数据与摘要，摘要即原文。

---

## 论文一：Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents

- **arXiv ID**: 2604.03173v1
- **URL**: https://arxiv.org/abs/2604.03173
- **PDF**: https://arxiv.org/pdf/2604.03173v1
- **作者**: Delip Rao, Eric Wong, Chris Callison-Burch
- **发布**: 2026-04-03T16:49:02Z
- **分类**: cs.CL
- **页数**: 25 pages（arxiv comment）
- **获取渠道**: arXiv API（多源搜索 skill 学术引擎），2026-08-04

### 摘要（原文）

Large language models and deep research agents supply citation URLs to support their claims, yet the reliability of these citations has not been systematically measured. We address six research questions about citation URL validity using 10 models and agents on DRBench (53,090 URLs) and 3 models on ExpertQA (168,021 URLs across 32 academic fields). We find that 3--13\% of citation URLs are hallucinated -- they have no record in the Wayback Machine and likely never existed -- while 5--18\% are non-resolving overall. Deep research agents generate substantially more citations per query than search-augmented LLMs but hallucinate URLs at higher rates. Domain effects are pronounced: non-resolving rates range from 5.4\% (Business) to 11.4\% (Theology), with per-model effects even larger. Decomposing failures reveals that some models fabricate every non-resolving URL, while others show substantial link-rot fractions indicating genuine retrieval. As a solution, we release urlhealth, an open-source tool for URL liveness checking and stale-vs-hallucinated classification using the Wayback Machine. In agentic self-correction experiments, models equipped with urlhealth reduce non-resolving citation URLs by $6\textrm{--}79\times$ to under 1\%, though effectiveness depends on the model's tool-use competence. The tool and all data are publicly available. Our characterization findings, failure taxonomy, and open-source tooling establish that citation URL validity is both measurable at scale and correctable in practice.

---

## 论文二：Deep-Research Agents Can Be Poisoned via User-Generated Content

- **arXiv ID**: 2605.24245v1
- **URL**: https://arxiv.org/abs/2605.24245
- **PDF**: https://arxiv.org/pdf/2605.24245v1
- **作者**: Tingwei Zhang, Harold Triedman, Vitaly Shmatikov
- **发布**: 2026-05-22T21:46:32Z
- **分类**: cs.CR
- **机构关联**: Vitaly Shmatikov 为 Cornell Tech 教授（论文团队定位为 Cornell Tech 团队）
- **获取渠道**: arXiv API（多源搜索 skill 学术引擎，搜索词 abs:"deep research" AND abs:vulnerability），2026-08-04

### 摘要（原文）

Deep-research agents, i.e., systems that rely on multi-agent pipelines to iteratively retrieve, synthesize, and cite Web content in order to produce structured reports, are rapidly replacing traditional search for both routine and complex information needs. These agents issue many related queries during a single research session. We show that for many common search topics, they repeatedly retrieve the same user-generated content (UGC) pages from platforms such as Reddit and Wikipedia. Next, we argue that this retrieval overlap creates a concentrated attack surface: an adversary who appends a short, crafted text to a single, frequently retrieved UGC page can cause the agent to cite attacker-chosen content and promote attacker-chosen entities across many related queries.
We evaluate this attack on three representative deep-research systems (STORM, Co-STORM, and OmniThink) across multiple query clusters. We also study defenses at different stages of the pipeline, including source-level filtering and output-based detection. Our findings highlight a fundamental vulnerability in how deep-research agents retrieve and integrate web content.

---

## 采集备注

- 访问日期：2026-08-04
- 两篇论文均为 arXiv 预印本，未注明同行评审状态
- 论文一（2604.03173）为独立商业 LLM/DR agent 引用可靠性测量，与付费 DR 服务的"详细引用/减少幻觉"官方声称形成对照证据
- 论文二（2605.24245）为对开源 deep-research 系统（STORM、Co-STORM、OmniThink）的污染攻击研究，指出 UGC 检索重叠造成的攻击面
- 本文件仅如实存档学术引擎返回的元数据与摘要原文，不做评判

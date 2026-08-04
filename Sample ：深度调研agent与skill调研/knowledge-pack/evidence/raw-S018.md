---
source_id: S018
source_url: https://github.com/stanfordnlp/dspy ; https://storm.genie.stanford.edu
title: "dspy 框架（stanfordnlp/dspy）+ STORM live research preview（storm.genie.stanford.edu）"
author: stanfordnlp / stanford-oval（Stanford University）
date: 2026-08-04（访问日期）
fetched_at: 2026-08-04T17:00:00
content_type: github_repo + official_doc（两源合并）
note: "本条为 Batch1 补采：①dspy 作为论文驱动方案的技术底座；②STORM live preview 在线服务形态。原始正文分节存档，各节标注 URL。"
---

# 第一节：dspy GitHub README 原文（stanfordnlp/dspy，main 分支）

来源：https://raw.githubusercontent.com/stanfordnlp/dspy/main/README.md（经 GitHub raw 通道抓取，2026-08-04 访问）

## DSPy: _Programming_—not prompting—Foundation Models

**Documentation:** [DSPy Docs](https://dspy.ai/)

DSPy is the framework for _programming—rather than prompting—language models_. It allows you to iterate fast on **building modular AI systems** and offers algorithms for **optimizing their prompts and weights**, whether you're building simple classifiers, sophisticated RAG pipelines, or Agent loops.

DSPy stands for Declarative Self-improving Python. Instead of brittle prompts, you write compositional _Python code_ and use DSPy to **teach your LM to deliver high-quality outputs**. Learn more via our official documentation site or meet the community, seek help, or start contributing via this GitHub repo and our Discord server.

## Installation

```bash
pip install dspy
```
To install the very latest from `main`:
```bash
pip install git+https://github.com/stanfordnlp/dspy.git
```

## Citation & Reading More（论文清单，官方列出）

- **[Jul'25] GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning** — https://arxiv.org/abs/2507.19457
- **[Jun'24] Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs** — https://arxiv.org/abs/2406.11695
- **[Oct'23] DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines** — https://arxiv.org/abs/2310.03714
- [Jul'24] Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together — https://arxiv.org/abs/2407.10930
- [Jun'24] Prompts as Auto-Optimized Training Hyperparameters — https://arxiv.org/abs/2406.11706
- [Feb'24] Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models — https://arxiv.org/abs/2402.14207（STORM 论文，作者含 Omar Khattab）
- [Jan'24] In-Context Learning for Extreme Multi-Label Classification — https://arxiv.org/abs/2401.12178
- [Dec'23] DSPy Assertions: Computational Constraints for Self-Refining Language Model Pipelines — https://arxiv.org/abs/2312.13382
- [Dec'22] Demonstrate-Search-Predict: Composing Retrieval & Language Models for Knowledge-Intensive NLP — https://arxiv.org/abs/2212.14024.pdf

DSPy 主论文引用（README 提供）：
```
@inproceedings{khattab2024dspy,
  title={DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines},
  author={Khattab, Omar and Singhvi, Arnav and Maheshwari, Paridhi and Zhang, Zhiyuan and Santhanam, Keshav and Vardhamanan, Sri and Haq, Saiful and Sharma, Ashutosh and Joshi, Thomas T. and Moazam, Hanna and Miller, Heather and Zaharia, Matei and Potts, Christopher},
  journal={The Twelfth International Conference on Learning Representations},
  year={2024}
}
```

## dspy 仓库元数据（GitHub API，2026-08-04 访问）

- full_name: stanfordnlp/dspy（组织 stanfordnlp）
- description: "DSPy: The framework for programming—not prompting—language models"
- license: MIT License（spdx_id: MIT）
- language: Python
- created_at: 2023-01-09T21:01:51Z
- stargazers_count: 36,610；forks_count: 3,164；subscribers_count: 204；open_issues_count: 632
- homepage: https://dspy.ai
- default_branch: main；pushed_at: 2026-08-03T22:21:04Z；updated_at: 2026-08-04T08:34:15Z

# 第二节：STORM live research preview 页面（storm.genie.stanford.edu）

来源：https://storm.genie.stanford.edu（2026-08-04 访问）

## 2.1 首访实测（webfetch 通道）

首访页面仅返回服务条款确认框：

```
I agree to the terms of service.
Please check the box above
Close
```

说明：页面为 JS 渲染的单页应用，需勾选服务条款后方可进入；webfetch 静默提取无法完成该交互。

## 2.2 渲染后页面内容（CloakBrowser 通道，networkidle 渲染后提取）

```
# STORM
Source: https://storm.genie.stanford.edu/
Render mode: js

STORM（Stanford University logo）
✨ We thank Microsoft Azure for cloud credits

## Co-STORM

## Get a Wikipedia-like report on your topic with AI

STORM is a research prototype that supports interactive knowledge curation.

STORM & Co-STORM
```

关键声明：
- 项目归属：Stanford University
- 资助致谢：Microsoft Azure 云信用（cloud credits）
- 产品定位：research prototype，支持 interactive knowledge curation
- 核心功能宣传语："Get a Wikipedia-like report on your topic with AI"、"STORM & Co-STORM"

（注：页面主体功能区需勾选条款并登录/交互后方可完整呈现，本次仅采集到首屏。）

# 第三节：STORM 官方仓库 README 原文（stanford-oval/storm，main 分支）

来源：https://raw.githubusercontent.com/stanford-oval/storm/main/README.md（经 CloakBrowser 抓取，2026-08-04 访问）
补充说明：任务主源给出的预览地址 storm.genie.stanford.edu 指向 stanford-oval/storm 仓库（非 stanfordnlp/storm）；本节约录 README 中与"dspy 技术关系 / 服务形态"相关的原文。

## Overview

> STORM is a LLM system that writes Wikipedia-like articles from scratch based on Internet search. Co-STORM further enhanced its feature by enabling human to collaborative LLM system to support more aligned and preferred information seeking and knowledge curation.
>
> While the system cannot produce publication-ready articles that often require a significant number of edits, experienced Wikipedia editors have found it helpful in their pre-writing stage.
>
> **More than 70,000 people have tried our live research preview.** Try it out to see how STORM can help your knowledge exploration journey and please provide feedback to help us improve the system!

## How STORM & Co-STORM works（原文）

### STORM
STORM breaks down generating long articles with citations into two steps:
1. **Pre-writing stage**: The system conducts Internet-based research to collect references and generates an outline.
2. **Writing stage**: The system uses the outline and references to generate the full-length article with citations.

STORM identifies the core of automating the research process as automatically coming up with good questions to ask. To improve the depth and breadth of the questions, STORM adopts two strategies:
1. **Perspective-Guided Question Asking**: Given the input topic, STORM discovers different perspectives by surveying existing articles from similar topics and uses them to control the question-asking process.
2. **Simulated Conversation**: STORM simulates a conversation between a Wikipedia writer and a topic expert grounded in Internet sources to enable the language model to update its understanding of the topic and ask follow-up questions.

### Co-STORM
Co-STORM proposes **a collaborative discourse protocol** which implements a turn management policy to support smooth collaboration among:
- **Co-STORM LLM experts**: generate answers grounded on external knowledge sources and/or raise follow-up questions based on the discourse history.
- **Moderator**: generates thought-provoking questions inspired by information discovered by the retriever but not directly used in previous turns.
- **Human user**: either observe the discourse, or actively engage by injecting utterances to steer the discussion focus.

Co-STORM also maintains a dynamic updated **mind map**, which organizes collected information into a hierarchical concept structure, aiming to **build a shared conceptual space between the human user and the system**.

> **Both STORM and Co-STORM are implemented in a highly modular way using [dspy](https://github.com/stanfordnlp/dspy).**

## API / 实现相关（原文要点）

- Language model components: All language models supported by litellm（https://docs.litellm.ai/docs/providers）
- Embedding model components: 同 litellm 支持列表
- retrieval module components: YouRM, BingSearch, VectorRM, SerperRM, BraveRM, SearXNG, DuckDuckGoSearchRM, TavilySearchRM, GoogleSearch, AzureAISearch
- STORM 引擎 = `STORMWikiRunner` 类；多 LM 系统范式，不同组件可配不同模型（例：conv_simulator_lm 用便宜/快模型，article_gen_lm 用更强模型）
- 四模块：Knowledge Curation Module / Outline Generation Module / Article Generation Module / Article Polishing Module

## Latest News（时间线，原文）

- [2025/01] litellm 集成（language models and embedding models）knowledge-storm v1.1.0
- [2024/09] Co-STORM codebase 发布，集成入 knowledge-storm python package v1.0.0
- [2024/09] Co-STORM 论文被 EMNLP 2024 主会议接收
- [2024/07] pip install knowledge-storm 可用
- [2024/07] VectorRM（用户文档 grounding）支持
- [2024/07] streamlit demo light 发布（本地开发用）
- [2024/06] NAACL 2024 展示 STORM
- [2024/05] Bing Search 支持；demo 文章生成改用 GPT-4o
- [2024/04] refactored codebase，定义 interface.py

## Datasets（官方发布）

- **FreshWiki**: 100 篇高质量维基文章（2022-02 至 2023-09 高编辑量页面），huggingface: EchoShao8899/FreshWiki
- **WildSeek**: 基于 web research preview 用户数据构建（每项 = 主题 + 用户深搜目标），huggingface: YuchengJiang/WildSeek

## 仓库元数据（GitHub API，2026-08-04 访问）

- full_name: stanford-oval/storm（组织 stanford-oval）
- description: "An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations."
- license: MIT License；language: Python
- created_at: 2024-03-24T16:23:39Z；pushed_at: 2025-09-30T18:07:21Z
- stargazers_count: 30,778；forks_count: 2,883；subscribers_count: 187；open_issues_count: 107
- homepage: http://storm.genie.stanford.edu
- topics: agentic-rag, deep-research, emnlp2024, knowledge-curation, large-language-models, naacl, nlp, report-generation, retrieval-augmented-generation
- 致谢：Vercel 支持开源软件（storm.genie.stanford.edu）；FreshWiki 数据集 CC BY-SA

## requirements.txt（stanford-oval/storm main 分支，2026-08-04 访问）

```text
dspy_ai==2.4.9
wikipedia==1.4.0
sentence-transformers
toml
langchain-text-splitters
trafilatura
langchain-huggingface
qdrant-client
langchain-qdrant
numpy
litellm
diskcache
```

→ STORM 直接依赖 dspy_ai==2.4.9（dspy 的 PyPI 包名），与 README"implemented using dspy"声明互证。

# 第四节：第三方独立验证（Tavily 搜索补充，2026-08-04）

以下为外部内容对官方声称的补充/交叉验证，非官方原文；与官方声称分开记录：

| 来源 | 类型 | 内容 |
|---|---|---|
| https://towardsdatascience.com/running-the-storm-ai-research-system-with-your-local-documents-e413ea2ae064 | 技术博客（第三方） | 称 online UI 很好用；仓库自带 demo UI 很基础，不可用于生产 |
| https://the-decoder.com/stanford-ai-experiment-storm-generates-wikipedia-style-articles | 新闻（2024-09-25） | STORM 自动化维基式文章写作的准备阶段（研究+大纲） |
| https://www.youtube.com/watch?v=0j2fXxNcvlk | 教程视频 | 称免费使用；报告含目录、引用、参考文献，可 PDF 下载 |
| https://www.edtechinnovationhub.com/news/pn7fo3f7xehe5gfj24mcjuntt7ormz | 新闻（第三方转述） | 称 Co-STORM 达到 99% factual accuracy（官方未作此声明，第三方转述） |
| https://www.linkedin.com/posts/manishatnere_github-stanfordnlpdspy-dspy-the-framework-activity-7382994434839379970-FEug | 社区帖子 | 称 DSPy 优化运行约 $2 / 20 分钟（第三方经验数值，官方未作此声明） |

（注：所有第三方内容仅作为独立验证记录，不参与断言置信度提升，除非与官方声明一致。）

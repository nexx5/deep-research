# raw-S010：DeepResearch Bench (Ayanami0730/deep_research_bench) 原文存档

## 抓取元信息

| 项 | 值 |
|---|---|
| source_id | S010 |
| 主来源 | https://github.com/Ayanami0730/deep_research_bench |
| 副来源 | https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard |
| 任务指定 URL | https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard（**2026-08-04 访问返回 404**，见下方源偏差说明） |
| 官方论文 | https://arxiv.org/abs/2506.11763 |
| 访问日期 | 2026-08-04 |
| 抓取渠道 | GitHub：GitHub API（readme base64 + repo 元信息）+ CloakBrowser 渲染（渠道3）；HuggingFace：CloakBrowser（渠道3）；arXiv：API 直调（渠道 API） |
| 抓取工具 | 多源搜索 skill（webfetch 直连 GitHub/HuggingFace/HF-API 均 Transport error，SearXNG Transport error，改用 CloakBrowser socks5://127.0.0.1:4040） |

**源偏差说明**：任务指定的 HuggingFace Space `Ayanami0730/DeepResearch-Leaderboard` 于 2026-08-04 经 CloakBrowser 访问返回 404（页面不存在）。GitHub README 徽标仍指向该 Space，但实际在用/可访问的官方 Leaderboard 为 `muset-ai/DeepResearch-Bench-Leaderboard`（README "View Latest Leaderboard" 链接）。本条以 muset-ai Space 为榜单数据源，并在 raw 中保留 404 事实。

---

## 一、GitHub 仓库元信息（GitHub API，2026-08-04）

```json
{
  "full_name": "Ayanami0730/deep_research_bench",
  "description": "DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents",
  "created_at": "2025-06-13T09:36:49Z",
  "updated_at": "2026-08-04T03:47:20Z",
  "pushed_at": "2026-05-11T06:14:30Z",
  "stargazers_count": 805,
  "forks_count": 85,
  "watchers_count": 805,
  "open_issues_count": 23,
  "language": "Python",
  "license": "Apache License 2.0",
  "homepage": "https://arxiv.org/pdf/2506.11763",
  "topics": ["agent", "benchmark", "deepresearch", "nlp"],
  "fork": false,
  "has_pages": false
}
```

---

## 二、GitHub README 全文（CloakBrowser 渲染提取，2026-08-04）

> 来源：https://github.com/Ayanami0730/deep_research_bench （Render mode: js）

## DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents

[![license](Apache-2.0)](https://github.com/Ayanami0730/deep_research_bench/blob/main/LICENSE) [![website](https://deepresearch-bench.github.io/)](https://deepresearch-bench.github.io/) [![Dataset](https://huggingface.co/datasets/muset-ai/DeepResearch-Bench-Dataset)](https://huggingface.co/datasets/muset-ai/DeepResearch-Bench-Dataset) [![Leaderboard](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard) [![Hugging Face](https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard)](https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard) [![arXiv](https://arxiv.org/abs/2506.11763)](https://arxiv.org/abs/2506.11763) [![AGI-Eval](https://agi-eval.cn/evaluation/detail?id=67)](https://agi-eval.cn/evaluation/detail?id=67)

##### If you like our project, please give us a star ⭐ on GitHub for the latest update.

## ✨ News

- \[11 May 2026\] 🎯 **Official Evaluator Switched to GPT-5.5**: Following Google's announced June 17, 2026 deprecation of Gemini-2.5-Pro, we benchmarked three frontier reasoning models as candidate replacements on the human-annotated subset (50 tasks × 4 target DRAs = 200 articles), measuring each candidate's alignment with human judgments (human inter-annotator agreement baseline = **68.78%**). All three candidates exceed this baseline by 1.3–3 points; **GPT-5.5 wins on Overall, PAR, and FAS**. We are adopting it as the new RACE evaluator (with **GPT-5.4-mini** for the FACT pipeline). Scores:
	| Candidate evaluator | Overall ↑ | PAR | OPC | FAP | FAS |
	| --- | --- | --- | --- | --- | --- |
	| **GPT-5.5** 🥇 | **71.82** | **73.00** | 89.70 | 65.35 | **59.23** |
	| Gemini-3.1-Pro | 70.58 | 71.33 | **90.14** | 65.39 | 55.45 |
	| Claude-Opus-4-7 | 70.11 | 71.00 | 86.76 | **66.70** | 55.99 |
- \[11 May 2026\] 📢 **Leaderboard Migration Plan**:
	> - **Now – 31 May 2026 (dual-acceptance window)**: We accept submissions evaluated under **both** the legacy evaluator (Gemini-2.5-Pro) **and** the new one (GPT-5.5). Results are displayed on **two separate leaderboards** so the rankings remain directly comparable within each evaluator.
	> - **By 1 June 2026 (full migration)**: For the results reported in the original DRB paper, we will re-evaluate them under GPT-5.5 and migrate them to the new leaderboard automatically. For prior community submissions evaluated under Gemini-2.5-Pro, if you would like to keep your entry on the new leaderboard, please contact us per [Submit to Leaderboard](#submit-to-leaderboard) and re-submit following the updated requirements. New submitters: follow the keys / config in [API Configuration](#api-configuration) below. After 1 June, Gemini-2.5-Pro acceptance ends and only the GPT-5.5 leaderboard is maintained going forward.
	> - **GPT-5.5 leaderboard status**: still under construction — expected to launch within a week, alongside the migrated scores.
	> - **Legacy code**: the previous Gemini-2.5-Pro / Gemini-2.5-Flash evaluation code is preserved on the [`Gemini-2.5`](https://github.com/Ayanami0730/deep_research_bench/tree/Gemini-2.5) branch.
- \[11 May 2026\] 🔧 **Evaluation Pipeline v2**: In the new release we have refined the article-cleaning logic, using a chunk-based strategy to better support very long articles.
- \[6 Feb 2026\] 🚀 **DeepResearch Bench II Release**: We have released **DeepResearch Bench II (DRB II)** ([homepage](https://agentresearchlab.org/benchmarks/deepresearch-bench-ii/index.html#home) ｜ [repo](https://github.com/imlrz/DeepResearch-Bench-II) ｜ [paper](https://arxiv.org/abs/2601.08536)). We welcome you to evaluate and exchange ideas. Note that DRB II, as a follow-up to DRB, has a different evaluation focus from DRB; **DRB will continue to be maintained and updated** after the release of DRB II. For more details, please refer to the [DRB II paper](https://arxiv.org/abs/2601.08536).
- \[6 Feb 2026\] 📚 **New Papers from Our Lab**: We welcome you to check out the new papers from our lab ([Agent Research Lab](https://agentresearchlab.org/index.html)):
	- **Benchmarks**:
		- [DeepResearch Bench II](https://arxiv.org/abs/2601.08536): Evaluates DRA-generated reports with 9,430 fine-grained binary rubrics (information recall, analysis, presentation) derived from expert-written articles.
		- [Wiki Live Challenge](https://arxiv.org/abs/2602.01590): A live benchmark that uses Wikipedia Good Articles as expert-level references, with fine-grained criteria for writing quality and factual verifiability.
		- [WildGraphBench](https://arxiv.org/abs/2602.02053): Benchmarks GraphRAG on long, heterogeneous documents with 1,100 questions spanning single-fact QA, multi-fact QA, and section-level summarization.
	- **Agents**:
		- [A-RAG](https://arxiv.org/abs/2602.03442): An agentic RAG framework that exposes hierarchical retrieval interfaces (keyword search, semantic search, chunk read) to the model for adaptive multi-granularity retrieval.
		- [FS-Researcher](https://arxiv.org/abs/2602.01566): A file-system-based dual-agent framework (Context Builder + Report Writer) that scales deep research beyond the context window via a persistent knowledge base.
	**If you want to evaluate your deep research agent** please see the leaderboard submission requirements below and contact us at [dumingxuan@mail.ustc.edu.cn](mailto:dumingxuan@mail.ustc.edu.cn) and [imlrz@mail.ustc.edu.cn](mailto:imlrz@mail.ustc.edu.cn).
- \[18 July 2025\] 🎉 We have established a partnership with **AGI-Eval** platform. DeepResearch Bench is now available on [**AGI-Eval**](https://agi-eval.cn/evaluation/detail?id=67), providing a more convenient evaluation interface for researchers and practitioners to test their deep research agents.
- \[15 July 2025\] ⚡️⚡️ **Major Update**: Added comprehensive evaluation of **Kimi-Researcher**, **Doubao-DeepResearch**, and **Claude-Researcher**. Upgraded evaluation infrastructure with **Gemini-2.5-Pro** for RACE and **Gemini-2.5-Flash** for FACT evaluation (since superseded — see top of News). All raw research articles and evaluation scores are now available on our [**Hugging Face Leaderboard**](https://huggingface.co/spaces/Ayanami0730/DeepResearch-Leaderboard) for comprehensive analysis and comparison.

For detailed evaluation results and comprehensive comparisons, please refer to the evaluation results table below.

## 📖 Overview

DeepResearch Bench addresses the absence of a comprehensive benchmark for systematically evaluating Deep Research Agents (DRAs). Our benchmark consists of **100 PhD-level research tasks**, each meticulously crafted by domain experts across **22 distinct fields**, including:

- 🔬 **Science & Technology**: Physics, chemistry, biology, environmental science, and engineering
- 💼 **Finance & Business**: investments, personal finance, marketing, and human resources
- 💻 **Software**: Topics related to the use of software and the internet
- 🌍 **Others**: Art & Design, Entertainment, History, Industrial, Transportation, Travel, and more

## Benchmark Construction

### Topic Distribution Analysis

To ensure DeepResearch Bench reflects real-world research demands, we analyzed **96,147 anonymized user queries** from web search-enabled LLM interactions. These queries were classified into **22 topic domains** based on the WebOrganizer taxonomy, revealing the authentic distribution of human deep research needs across different fields.

### Expert Task Collection

Guided by real-world demand distribution, we invited **PhD-level experts and senior practitioners** (5+ years experience) to design challenging research tasks within their domains. Each submission underwent rigorous manual screening for:

- **Quality**: High research standards and complexity
- **Clarity**: Clear task definitions and requirements
- **Authenticity**: Grounded in real research scenarios
- **Challenge Level**: Testing upper limits of DRA capabilities

This process yielded **100 high-quality benchmark tasks** (50 Chinese, 50 English) that maintain the same topical balance as observed in real-world usage.

## Evaluation Framework

DeepResearch Bench introduces two complementary evaluation methodologies designed to comprehensively assess Deep Research Agents:

### 🎯 RACE (Reference-based Adaptive Criteria-driven Evaluation)

RACE evaluates **report generation quality** through a sophisticated multi-step process:

- **Dynamic Criteria Generation**: Automatically generates task-specific evaluation criteria across four key dimensions:
	- 📚 **Comprehensiveness**: Coverage breadth and depth of the research topic
	- 🔍 **Insight/Depth**: Quality of analysis and insight generation
	- 📋 **Instruction-Following**: Adherence to specific task requirements
	- 📖 **Readability**: Clarity, organization, and presentation quality
- **Reference-Based Scoring**: Compares target reports against high-quality reference reports to ensure discriminative evaluation
- **Weighted Assessment**: Uses dynamic weights adapted to each task's specific requirements

### 🔗 FACT (Framework for Factual Abundance and Citation Trustworthiness)

FACT evaluates **information retrieval and grounding capabilities** through:

- **Statement-URL Extraction**: Automatically extracts factual claims and their cited sources from generated reports
- **Deduplication**: Removes redundant statement-URL pairs to focus on unique factual claims
- **Support Verification**: Uses web scraping and LLM judgment to verify whether cited sources actually support the claims
- **Citation Metrics**: Calculates:
	- **Citation Accuracy**: Percentage of correctly supported citations
	- **Effective Citations**: Average number of verifiably supported citations per task

## 📊 Evaluation Results

### Main Results

**View Latest Leaderboard**: Visit our [**DeepResearch Bench Leaderboard**](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard) for real-time updated evaluation results, detailed comparative analysis, and raw data.

### Submit to Leaderboard

If you would like to obtain an **official leaderboard entry** on DeepResearch Bench, please prepare the following materials and send them by email to:

- `dumingxuan@mail.ustc.edu.cn`
- `imlrz@mail.ustc.edu.cn`

**Required submission materials:**

1. **A temporary key with access to GPT-5.5**
	- This key is used only for verification/evaluation.
	- It should remain valid during the evaluation window.
	- Supported providers: OpenAI (official), OpenRouter
2. **The raw generated articles**
	- Please provide your model outputs in the same format as the benchmark raw data.
	- Reference example: [`data/test_data/raw_data/claude-3-7-sonnet-latest.jsonl`](https://github.com/Ayanami0730/deep_research_bench/blob/main/data/test_data/raw_data/claude-3-7-sonnet-latest.jsonl)
3. **Reproducibility link**
	- If your model/agent is **open-source**, please provide a repository link that allows others to reproduce the results.
	- If your model/agent is **closed-source**, please provide the product page and/or API link used for reproduction and verification.
4. **Model metadata**
	- **Model name**
	- **Model/project link**
	- **Open-source license** (for open-source submissions; if closed-source, please clearly indicate that it is proprietary)

**Recommended additional files:**

- `results/race/<model_name>/race_result.txt`
- `results/fact/<model_name>/fact_result.txt`

Providing these files can help us speed up verification, but the raw generated reports and the temporary evaluation key are the most important requirements.

---

## 🛠️ Installation and Usage

### Prerequisites

- Python 3.9+
- OpenRouter or OpenAI API key (for LLM evaluation)
- Jina API key (for web scraping in FACT evaluation)

### Setup

```
git clone https://github.com/your-username/deep_research_bench.git
cd deep_research_bench
pip install -r requirements.txt
```

### API Configuration

Set the required API keys as environment variables:

```
# Pick one backend. OpenRouter is the default.
export LLM_BACKEND="openrouter"               # or "openai"

# OpenRouter (default):
export OPENROUTER_API_KEY="sk-or-v1-xxxxx"

# Or OpenAI direct:
# export LLM_BACKEND="openai"
# export OPENAI_API_KEY="sk-xxxxx"

# Set Jina API key for web scraping (FACT pipeline only)
export JINA_API_KEY="your_jina_api_key_here"
```

Default models per backend (override with `RACE_MODEL` / `FACT_MODEL` env vars):

| Backend | RACE judge (`Model`) | FACT judge (`FACT_Model`) |
| --- | --- | --- |
| openrouter | `openai/gpt-5.5` | `openai/gpt-5.4-mini` |
| openai | `gpt-5.5` | `gpt-5.4-mini` |

## Project Structure

```
deep_research_bench/
├── data/
│   ├── criteria_data/      # Evaluation criteria data
│   ├── prompt_data/        
│   │   └── query.jsonl     # ← 100 benchmark queries for your agent
│   └── test_data/          
│       ├── cleaned_data/   # Cleaned article data
│       └── raw_data/       # ← Put your model outputs here (model_name.jsonl)
├── prompt/                 # Prompt templates
├── utils/                  # Utility functions
├── deepresearch_bench_race.py  # RACE evaluation script
├── run_benchmark.sh        # ← Add your model names here, then run
└── requirements.txt        # Dependencies
```

**Quick Start Flow:**

1. Use queries from `data/prompt_data/query.jsonl` → Run your Deep Research Agent
2. Save outputs to `data/test_data/raw_data/<model_name>.jsonl`
3. Add model name to `TARGET_MODELS` in `run_benchmark.sh`
4. Run: `bash run_benchmark.sh`

## Quick Start

### 1. Prepare Your Model Data

Run your Deep Research Agent on the benchmark queries and save outputs in the required format:

**Input**: Use queries from `data/prompt_data/query.jsonl` (100 benchmark tasks)

**Output**: Save results to `data/test_data/raw_data/<model_name>.jsonl`

**Required format** (each line should contain):

```
{
    "id": "task_id", 
    "prompt": "original_query_text", 
    "article": "generated_research_article_with_citations"
}
```

### 2. Configure Models to Evaluate

Edit `run_benchmark.sh` and add your model name:

```
TARGET_MODELS=("your-model-name")
```

### 3. Run Evaluation

```
bash run_benchmark.sh
```

Results will be saved to:

- RACE evaluation: `results/race/<model_name>/race_result.txt`
- FACT evaluation: `results/fact/<model_name>/fact_result.txt`

### Custom LLM Integration

If you're not using OpenRouter or the official OpenAI API, or want to use other LLMs for evaluation, modify the `AIClient` class in `utils/api.py` to implement your custom LLM interface.

## Acknowledgements

We would like to express our gratitude to the following contributors who helped us collect evaluation data. Since many models and agents do not provide public APIs, manual data collection was necessary, and we deeply appreciate their dedicated efforts:

**Xin Yang**, **Jie Yang**, **Yawen Li**, **Xinyu Ouyang**, **Jiaqi He**, **Gefan Zhang**, **Jinfu Liao**, **Qiuyue Chen**, **Yulin Wang**, and **Lina Wang**.

Their contributions were essential to the comprehensive evaluation presented in this benchmark.

## Citation

If you use DeepResearch Bench in your research, please cite our paper:

```
@article{du2025deepresearch,
  author    = {Mingxuan Du and Benfeng Xu and Chiwei Zhu and Xiaorui Wang and Zhendong Mao},
  title     = {DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents},
  journal   = {arXiv preprint},
  year      = {2025},
}
```

---

## 三、官方论文摘要（arXiv 2506.11763，2026-08-04 API 获取）

- 标题：DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents
- 作者：Mingxuan Du, Benfeng Xu, Chiwei Zhu, Xiaorui Wang, Zhendong Mao
- 发布：2025-06-13，31 pages, 5 figures，分类 cs.CL / cs.IR
- 摘要原文：

> Deep Research Agents are a prominent category of LLM-based agents. By autonomously orchestrating multistep web exploration, targeted retrieval, and higher-order synthesis, they transform vast amounts of online information into analyst-grade, citation-rich reports--compressing hours of manual desk research into minutes. However, a comprehensive benchmark for systematically evaluating the capabilities of these agents remains absent. To bridge this gap, we present DeepResearch Bench, a benchmark consisting of 100 PhD-level research tasks, each meticulously crafted by domain experts across 22 distinct fields. Evaluating DRAs is inherently complex and labor-intensive. We therefore propose two novel methodologies that achieve strong alignment with human judgment. The first is a reference-based method with adaptive criteria to assess the quality of generated research reports. The other framework is introduced to evaluate DRA's information retrieval and collection capabilities by assessing its effective citation count and overall citation accuracy. We have open-sourced DeepResearch Bench and key components of these frameworks at https://github.com/Ayanami0730/deep_research_bench to accelerate the development of practical LLM-based agents.

---

## 四、HuggingFace Leaderboard 榜单数据（muset-ai/DeepResearch-Bench-Leaderboard，2026-08-04 CloakBrowser 抓取）

### 4.1 Space 结构说明（create_leaderboard.py + tabs/leaderboard_tab_gpt55.py）

- 应用为 Gradio v2.1，含两个榜单 Tab：
  - **Leaderboard（GPT-5.5 Eval）**：Race judge GPT-5.5，Fact-check GPT-5.4-mini；数据文件 `data_gpt55/leaderboard.csv`
  - **Leaderboard (Gemini-2.5 Eval)**（legacy）：Race judge gemini-2.5-pro，Fact-check gemini-2.5-flash；数据文件 `data/leaderboard.csv`
- 简介："The research aims to comprehensively evaluate the capabilities of Deep Research Agents."
- GPT-5.5 Tab 的模型显示名/链接/许可证映射（MODEL_LINKS / MODEL_LICENSE_TYPE）节选：
  - gemini-2.5-pro-deepresearch → Proprietary
  - openai-deepresearch → Proprietary
  - perplexity-Research → Proprietary
  - grok-deeper-search → Proprietary
  - dalpha-deepresearch → Closed-source proprietary system（GitHub: dalphakr/Dalpha-DeepResearch）
  - sourcery → Closed source for now（sourceryintel.com）
  - bodhi → Proprietary（publicissapient.com/platforms/bodhi，显示名 "Sapient Bodhi-DeepResearch"）
  - lunon_full100_FINAL.submission → MIT（GitHub: LunonAI/lunon-deep-research，显示名 "Lunon Deep Research"）
  - WhaleCloud-DocChain_0612 → Proprietary（lab.hjcloud.com/chat-agent/deepresearch）
  - cellcog-max → Proprietary（cellcog.ai/super-agents）

### 4.2 Legacy 榜单 data/leaderboard.csv（Gemini-2.5 评估，45 条目，全量原文）

列：model,overall_score,comprehensiveness,insight,instruction_following,readability,citation_accuracy,effective_citations

```
qianfan_deepresearch_0430,58.03,59.48,61.48,53.87,54.34,-,-
ZTE-Nebula-DeepResearch-V20260519,57.27,58.37,59.76,54.06,54.66,-,-
Link,57.08,58.24,59.74,53.24,55.05,-,-
zhipu_deep_research,57.06,58.15,60.14,53.47,53.88,-,-
xiaoyi,57.00,58.58,59.38,53.58,53.99,-,-
WhaleCloud-DocChain,56.81,57.13,59.30,53.98,54.97,-,-
cellcog-max,56.67,57.40,60.01,53.25,53.21,-,-
1688AILab-DeepResearch-0428,56.53,57.32,59.27,53.51,53.36,-,-
octen-deepresearch-0508,56.31,56.89,59.00,53.39,53.83,-,-
grep-v5,56.23,56.82,58.92,53.38,53.44,-,-
nvidia-aiq-nemotron-gpt52-updated,55.95,56.90,58.49,52.89,53.43,-,-
1688AILab-DeepResearch-0325,55.39,55.48,57.59,53.38,53.50,-,-
ms_deepresearch_gpt52mixqwen35_09_edit_restart09_think_medium,55.31,56.76,56.79,53.10,52.28,-,-
drb_cellcog,55.31,55.41,58.21,52.50,53.12,-,-
deepinsight,55.24,55.66,58.70,52.53,50.94,-,-
ms_deepresearch,54.97,56.45,56.22,53.25,51.71,-,-
TrajectoryKit,54.92,54.10,57.90,52.91,52.72,-,-
onyx,54.54,54.67,56.43,53.08,52.02,-,-
deepsynth,54.22,54.23,56.09,52.86,51.81,-,-
deepdog,53.52,53.14,56.10,51.83,51.18,-,-
RecallRadar,53.19,53.91,53.53,52.18,52.38,-,-
MindDR-V1.5,52.54,51.54,55.30,50.45,51.26,-,-
tavily-research,52.44,52.84,53.59,51.92,49.21,-,-
thinkdepthai-deepresearch,52.43,52.02,53.88,52.04,50.12,-,-
salesforce-air-deep-research,50.65,50.00,51.09,50.77,50.32,-,-
gensee-search-gpt-5,50.60,50.06,50.76,51.31,49.72,32.94,21.06
gemini-2.5-pro-deepresearch,49.71,49.51,49.45,50.12,50.00,78.30,165.34
langchain-open-deep-research-gpt-5,49.33,49.80,47.34,51.05,48.99,34.74,22.44
openai-deepresearch,46.45,46.46,43.73,49.39,47.22,75.01,39.79
raaa-deep-research,46.13,43.77,48.34,47.21,43.78,-,-
dr-tulu,45.49,44.08,44.65,49.56,42.30,-,-
claude-research,45.00,45.34,42.79,47.58,44.66,-,-
kimi-researcher,44.64,44.96,41.97,47.14,45.59,-,-
doubao-deepresearch,44.34,44.84,40.56,47.95,44.69,52.86,52.62
langchain-open-deep-research,43.44,42.97,39.17,48.09,45.22,49.10,29.49
nvidia-aiq-research-assistant,40.52,37.98,38.39,44.59,42.63,-,-
tongyi-deepresearch-30B-A3B,40.46,39.46,34.44,46.22,44.27,-,-
perplexity-Research,40.46,39.10,35.65,46.11,43.08,82.63,31.20
grok-deeper-search,38.22,36.08,30.89,46.59,42.17,73.08,8.58
sonar-reasoning-pro,37.76,34.96,31.65,44.93,42.42,45.19,9.39
sonar-reasoning,37.75,34.73,32.59,44.42,42.39,52.58,13.37
claude-3-7-sonnet-with-search,36.63,35.95,31.29,44.05,36.07,87.32,24.51
sonar-pro,36.19,33.92,29.69,43.39,41.07,79.72,16.75
gemini-2.5-pro-preview-05-06,31.90,31.75,24.61,40.24,32.76,-,-
gpt-4o-search-preview,30.74,27.81,20.44,41.01,37.60,86.63,5.05
```

### 4.3 GPT-5.5 新榜单 data_gpt55/leaderboard.csv（10 条目，全量原文）

```
cellcog-max,55.78,56.34,57.08,55.30,51.94,-,-
WhaleCloud-DocChain_0612,54.78,55.14,55.33,54.85,52.48,-,-
bodhi,54.07,54.15,54.60,54.41,51.87,-,-
lunon_full100_FINAL.submission,53.51,53.42,54.83,53.41,50.48,-,-
dalpha-deepresearch,53.10,52.58,52.94,53.87,53.20,-,-
sourcery,51.17,50.53,52.22,51.06,49.68,-,-
gemini-2.5-pro-deepresearch,49.98,50.01,49.92,50.22,49.58,-,-
openai-deepresearch,47.84,48.05,46.69,49.29,47.62,-,-
perplexity-Research,43.05,41.78,41.27,45.31,46.03,-,-
grok-deeper-search,41.22,39.65,38.12,44.62,45.72,-,-
```

---

## 五、相关基准/论文检索结果（arXiv API，2026-08-04）

检索式 `all:"Deep Research Bench"` 命中 4 篇，全量摘要见 raw 附注（此处记录可区分条目）：

| arXiv ID | 标题 | 作者 | 与本源关系 |
|---|---|---|---|
| 2506.06287 | Deep Research Bench: Evaluating AI Web Research Agents | FutureSearch（Nikos I. Bosse 等 8 人） | **同名不同源的另一个 DRB**：89 个多步 web 研究任务实例、8 类任务、RetroSearch 冻结网页环境、leaderboard 在 drb.futuresearch.ai；评估 o3、Gemini 2.5 Pro 等 "thinking" 模型及 "Deep Research/Deep Search" 商业产品 |
| 2601.08536 | DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Report | Ruizhe Li, Mingxuan Du, Benfeng Xu, Chiwei Zhu, Xiaorui Wang, Zhendong Mao | 本仓库团队的后续基准（DRB II）：132 任务、22 域、9,430 细粒度二元 rubrics（信息回忆/分析/呈现三维），四阶段 LLM+人工流水线、400+ 人工小时；最强模型满足 <50% rubrics |
| 2509.25106 | Towards Personalized Deep Research: Benchmarks and Evaluations | Yuan Liang 等 15 人 | PDR-Bench：50 任务×10 域×25 用户画像=250 查询；PQR 评估框架（Personalization Alignment / Content Quality / Factual Reliability） |
| 2605.26958 | Tournament-GRPO: Group-Wise Tournament Rewards for RL in Open-Ended Long-Form Generation | Zixuan Yang 等 10 人 | 在 Deep Research Bench 上实验 Tournament-GRPO，较最强 baseline 提升 4.52 分 overall score |

> 注：2506.11763（本仓库论文）在 `all:"Deep Research Bench"` 检索中未直接返回（arXiv 全文检索未覆盖其摘要用词差异），通过 id_list 直查确认存在。

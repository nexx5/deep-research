---
source_id: S003
source_title: STORM（stanford-oval/storm）
source_url: https://github.com/stanford-oval/storm
source_type: GitHub 在线页面（README + 仓库元数据 + issues）
access_date: 2026-08-04
fetch_channel: webfetch（渠道1，GitHub 主页/Issues 页面）+ arXiv API（学术引擎）
raw_note: 本文件为 GitHub 页面 markdown 提取的正文存档（剔除导航噪音，保留 README 原文文本）+ arXiv 论文元数据；非逐字全页快照。LICENSE 全文抓取超时，许可证以仓库页面标注"MIT license"为准。
---

# raw-S003：STORM（stanford-oval/storm）GitHub 页面原文存档

## 1. 仓库元数据（GitHub 页面，2026-08-04 访问）

- 仓库：stanford-oval/storm（Public）
- 描述（About）："An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations."
- 统计：Star 30.8k / Fork 2.9k / Watchers 187 / Issues 58 / Pull requests 49 / 238 Commits / main 分支
- License：MIT license（仓库标注；LICENSE 文件存在于仓库根目录）
- 主页链接：Research preview（http://storm.genie.stanford.edu）、Website（https://storm-project.stanford.edu/）
- 主题标签：agentic-rag, deep-research, emnlp2024, knowledge-curation, large-language-models, naacl, nlp, report-generation, retrieval-augmented-generation
- 仓库文件结构：.github/、assets/、examples/、frontend/demo_light/、knowledge_storm/、.gitignore、.pre-commit-config.yaml、CONTRIBUTING.md、LICENSE、MANIFEST.in、README.md、requirements.txt、setup.py

## 2. README 原文（核心正文，webfetch markdown 提取）

### 2.1 标题与链接

> # STORM: Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking
>
> | Research preview | STORM Paper | Co-STORM Paper | Website |
> | http://storm.genie.stanford.edu | https://arxiv.org/abs/2402.14207 | https://www.arxiv.org/abs/2408.15232 | https://storm-project.stanford.edu/ |

### 2.2 Latest News（时间线）

- [2025/01] We add litellm integration for language models and embedding models in knowledge-storm v1.1.0.
- [2024/09] Co-STORM codebase is now released and integrated into knowledge-storm python package v1.0.0. Run pip install knowledge-storm --upgrade.
- [2024/09] We introduce collaborative STORM (Co-STORM) to support human-AI collaborative knowledge curation! Co-STORM Paper has been accepted to EMNLP 2024 main conference.
- [2024/07] You can now install our package with pip install knowledge-storm!
- [2024/07] We add VectorRM to support grounding on user-provided documents, complementing existing support of search engines (YouRM, BingSearch). (#58)
- [2024/07] We release demo light for developers a minimal user interface built with streamlit framework in Python. (#54)
- [2024/06] We will present STORM at NAACL 2024! Poster Session 2 on June 17, presentation material: assets/storm_naacl2024_slides.pdf.
- [2024/05] We add Bing Search support in rm.py. Test STORM with GPT-4o - we now configure the article generation part in our demo using GPT-4o model.
- [2024/04] We release refactored version of STORM codebase! We define interface for STORM pipeline and reimplement STORM-wiki (src/storm_wiki) to demonstrate how to instantiate the pipeline. We provide API to support customization of different language models and retrieval/search integration.

### 2.3 Overview（官方定位声明）

> STORM is a LLM system that writes Wikipedia-like articles from scratch based on Internet search. Co-STORM further enhanced its feature by enabling human to collaborative LLM system to support more aligned and preferred information seeking and knowledge curation.
>
> While the system cannot produce publication-ready articles that often require a significant number of edits, experienced Wikipedia editors have found it helpful in their pre-writing stage.
>
> More than 70,000 people have tried our live research preview. Try it out to see how STORM can help your knowledge exploration journey.

### 2.4 How STORM & Co-STORM works（架构与工作流）

#### STORM

> STORM breaks down generating long articles with citations into two steps:
> 1. Pre-writing stage: The system conducts Internet-based research to collect references and generates an outline.
> 2. Writing stage: The system uses the outline and references to generate the full-length article with citations.
>
> STORM identifies the core of automating the research process as automatically coming up with good questions to ask. Directly prompting the language model to ask questions does not work well. To improve the depth and breadth of the questions, STORM adopts two strategies:
> 1. Perspective-Guided Question Asking: Given the input topic, STORM discovers different perspectives by surveying existing articles from similar topics and uses them to control the question-asking process.
> 2. Simulated Conversation: STORM simulates a conversation between a Wikipedia writer and a topic expert grounded in Internet sources to enable the language model to update its understanding of the topic and ask follow-up questions.

#### Co-STORM

> Co-STORM proposes a collaborative discourse protocol which implements a turn management policy to support smooth collaboration among
> - Co-STORM LLM experts: This type of agent generates answers grounded on external knowledge sources and/or raises follow-up questions based on the discourse history.
> - Moderator: This agent generates thought-provoking questions inspired by information discovered by the retriever but not directly used in previous turns. Question generation can also be grounded!
> - Human user: The human user will take the initiative to either (1) observe the discourse to gain deeper understanding of the topic, or (2) actively engage in the conversation by injecting utterances to steer the discussion focus.
>
> Co-STORM also maintains a dynamic updated mind map, which organize collected information into a hierarchical concept structure, aiming to build a shared conceptual space between the human user and the system. The mind map has been proven to help reduce the mental load when the discourse goes long and in-depth.
>
> Both STORM and Co-STORM are implemented in a highly modular way using dspy.

### 2.5 Installation

> To install the knowledge storm library, use pip install knowledge-storm.
> You could also install the source code which allows you to modify the behavior of STORM engine directly.
> 1. Clone the git repository: git clone https://github.com/stanford-oval/storm.git; cd storm
> 2. Install the required packages: conda create -n storm python=3.11; conda activate storm; pip install -r requirements.txt

### 2.6 API（能力与模型/检索集成）

> Currently, our package support:
> - Language model components: All language models supported by litellm
> - Embedding model components: All embedding models supported by litellm
> - retrieval module components: YouRM, BingSearch, VectorRM, SerperRM, BraveRM, SearXNG, DuckDuckGoSearchRM, TavilySearchRM, GoogleSearch, and AzureAISearch
>
> PRs for integrating more search engines/retrievers into knowledge_storm/rm.py are highly appreciated!
>
> Both STORM and Co-STORM are working in the information curation layer, you need to set up the information retrieval module and language model module to create their Runner classes respectively.

#### STORM Runner 示例（原文代码）

```python
lm_configs = STORMWikiLMConfigs()
openai_kwargs = {'api_key': os.getenv("OPENAI_API_KEY"), 'temperature': 1.0, 'top_p': 0.9}
# STORM is a LM system so different components can be powered by different models to reach a good balance between cost and quality.
# For a good practice, choose a cheaper/faster model for conv_simulator_lm which is used to split queries, synthesize answers in the conversation.
# Choose a more powerful model for article_gen_lm to generate verifiable text with citations.
gpt_35 = LitellmModel(model='gpt-3.5-turbo', max_tokens=500, **openai_kwargs)
gpt_4 = LitellmModel(model='gpt-4o', max_tokens=3000, **openai_kwargs)
lm_configs.set_conv_simulator_lm(gpt_35)
lm_configs.set_question_asker_lm(gpt_35)
lm_configs.set_outline_gen_lm(gpt_4)
lm_configs.set_article_gen_lm(gpt_4)
lm_configs.set_article_polish_lm(gpt_4)
engine_args = STORMWikiRunnerArguments(...)
rm = YouRM(ydc_api_key=os.getenv('YDC_API_KEY'), k=engine_args.search_top_k)
runner = STORMWikiRunner(engine_args, lm_configs, rm)
```

```python
runner.run(topic=topic, do_research=True, do_generate_outline=True, do_generate_article=True, do_polish_article=True)
runner.post_run()
runner.summary()
```

> - do_research: if True, simulate conversations with difference perspectives to collect information about the topic; otherwise, load the results.
> - do_generate_outline: if True, generate an outline for the topic; otherwise, load the results.
> - do_generate_article: if True, generate an article for the topic based on the outline and the collected information; otherwise, load the results.
> - do_polish_article: if True, polish the article by adding a summarization section and (optionally) removing duplicate content; otherwise, load the results.

#### Co-STORM Runner 示例（要点）

- 类：CoStormRunner（from knowledge_storm.collaborative_storm.engine import CollaborativeStormLMConfigs, RunnerArgument, CoStormRunner）
- 多 LM 配置：question_answering_lm / discourse_manage_lm / utterance_polishing_lm / warmstart_outline_gen_lm / question_asking_lm / knowledge_base_lm
- 调用：costorm_runner.warm_start() → costorm_runner.step()（观察对话）或 costorm_runner.step(user_utterance="YOUR UTTERANCE HERE")（注入话语）→ costorm_runner.knowledge_base.reorganize() → article = costorm_runner.generate_report()

### 2.7 Customization of the Pipeline（模块化）

#### STORM 4 模块（原文）

> STORM engine consists of 4 modules:
> 1. Knowledge Curation Module: Collects a broad coverage of information about the given topic.
> 2. Outline Generation Module: Organizes the collected information by generating a hierarchical outline for the curated knowledge.
> 3. Article Generation Module: Populates the generated outline with the collected information.
> 4. Article Polishing Module: Refines and enhances the written article for better presentation.
>
> The interface for each module is defined in knowledge_storm/interface.py, while their implementations are instantiated in knowledge_storm/storm_wiki/modules/*. These modules can be customized (e.g., generating sections in bullet point format instead of full paragraphs).

#### Co-STORM 定制

> 1. Co-STORM introduces multiple LLM agent types (i.e. Co-STORM experts and Moderator). LLM agent interface is defined in knowledge_storm/interface.py, implementation in knowledge_storm/collaborative_storm/modules/co_storm_agents.py.
> 2. Co-STORM introduces a collaborative discourse protocol, with its core function centered on turn policy management. We provide an example implementation through DiscourseManager in knowledge_storm/collaborative_storm/engine.py.

### 2.8 Datasets（数据集）

- FreshWiki Dataset：a collection of 100 high-quality Wikipedia articles focusing on the most-edited pages from February 2022 to September 2023. 下载：huggingface.co/datasets/EchoShao8899/FreshWiki；数据构建源码存档于 NAACL-2024-code-backup/FreshWiki（为缓解数据污染）。
- WildSeek：data collected from the web research preview；downsampled；每个数据点为 topic + user's goal for conducting deep search on the topic。详见 Co-STORM 论文 Section 2.2 / Appendix A。下载：huggingface.co/datasets/YuchengJiang/WildSeek。

### 2.9 Replicate paper result

- STORM 论文实验：切换分支 NAACL-2024-code-backup。
- Co-STORM 论文实验：切换分支 EMNLP-2024-code-backup（README 标注 placeholder，will be updated soon）。

### 2.10 Roadmap & Contributions（官方路线图）

> Our team is actively working on:
> 1. Human-in-the-Loop Functionalities: Supporting user participation in the knowledge curation process.
> 2. Information Abstraction: Developing abstractions for curated information to support presentation formats beyond the Wikipedia-style report.
>
> Contact person: Yijia Shao (shaoyj@stanford.edu) and Yucheng Jiang (yuchengj@stanford.edu)

### 2.11 Acknowledgement（致谢）

> FreshWiki dataset is sourced from Wikipedia, licensed under the Creative Commons Attribution-ShareAlike (CC BY-SA) license.
> Thanks to Vercel for their support of open-source software (storm.genie.stanford.edu)。

### 2.12 Citation（论文引用，官方给出 BibTeX）

1. STORM 论文：Shao, Yijia; Jiang, Yucheng; Kanell, Theodore; Xu, Peter; Khattab, Omar; Lam, Monica. "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models". Proceedings of NAACL 2024 (Volume 1: Long Papers), pp. 6252–6278, Mexico City, Mexico, June 2024. DOI: 10.18653/v1/2024.naacl-long.347
2. Co-STORM 论文：Jiang, Yucheng; Shao, Yijia; Ma, Dekun; Semnani, Sina; Lam, Monica. "Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations". EMNLP 2024, pp. 9917–9955, Miami, Florida, USA, Nov 2024. DOI: 10.18653/v1/2024.emnlp-main.554

## 3. arXiv 论文元数据（arXiv API，2026-08-04 抓取，论文 2402.14207）

- 标题：Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models
- arXiv ID：2402.14207（v2，更新 2024-04-08；published 2024-02-22）
- 分类：cs.CL, cs.AI；27 pages，NAACL 2024 Main Conference
- 作者：Yijia Shao, Yucheng Jiang, Theodore A. Kanell, Peter Xu, Omar Khattab, Monica S. Lam
- 摘要原文：

> We study how to apply large language models to write grounded and organized long-form articles from scratch, with comparable breadth and depth to Wikipedia pages. This underexplored problem poses new challenges at the pre-writing stage, including how to research the topic and prepare an outline prior to writing. We propose STORM, a writing system for the Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking. STORM models the pre-writing stage by (1) discovering diverse perspectives in researching the given topic, (2) simulating conversations where writers carrying different perspectives pose questions to a topic expert grounded on trusted Internet sources, (3) curating the collected information to create an outline.
> For evaluation, we curate FreshWiki, a dataset of recent high-quality Wikipedia articles, and formulate outline assessments to evaluate the pre-writing stage. We further gather feedback from experienced Wikipedia editors. Compared to articles generated by an outline-driven retrieval-augmented baseline, more of STORM's articles are deemed to be organized (by a 25% absolute increase) and broad in coverage (by 10%). The expert feedback also helps identify new challenges for generating grounded long articles, such as source bias transfer and over-association of unrelated facts.

## 4. Issues 页面观察（2026-08-04 访问，58 open issues）

- 页面提示："New issue Issue creation is restricted in this repository"（新 issue 创建受限，需登录/组织限制，页面状态观察）。
- 代表性 open issues（标题节选，社区输入，非官方声称）：
  - #547 Handle empty retrieval tables during article generation（2026-07-20）
  - #409 [Feature Request] Add a small "knowledge curation & memory failure modes" doc (docs only)（2026-02-19）
  - #378 [FEATURE] Don't just search in English, search in other languages relevant to the query too.（2025-07-07）
  - #371 [FEATURE] Enhancing project with limitless context injection…
  - #368 [BUG] deepseek model error（2025-06-13）
  - #375 Security contact request – TLS-certificate bypass high-severity security issue
  - 其余为通用 bug/feature 报告

## 5. 采集说明

- 全部信息为官方仓库/论文/官方页面声称或页面状态观察，无独立第三方验证。
- LICENSE 全文抓取超时（raw.githubusercontent.com），许可证以仓库页面标注 "MIT license" 为准。

# raw-S028: LiveResearchBench (arXiv:2510.14240) + GAIA (arXiv:2311.12983)

> 双基准合并原文存档。获取方式：arXiv API 学术引擎（元数据+摘要）+ arXiv HTML 全文（LRB）+ HuggingFace 官方页（GAIA leaderboard README / dataset card，经远程代理渠道）。访问日期：2026-08-04。
> 说明：本文件为原始材料存档，非采录分析。LRB 含全文关键章节节选；GAIA 因 arXiv 无 HTML 版，仅存档摘要+官方页面原文节选。

---

## 一、LiveResearchBench（arXiv:2510.14240）

### 1.1 元数据（arXiv API 获取）

- 标题：LiveResearchBench: A Live Benchmark for User-Centric Deep Research in the Wild
- 作者：Jiayu Wang（UW-Madison）、Yifei Ming（Salesforce AI Research）、Riya Dulepet（Stanford）、Qinglin Chen、Austin Xu、Zixuan Ke（Salesforce AI Research）、Frederic Sala（UW-Madison）、Aws Albarghouthi（UW-Madison）、Caiming Xiong（Salesforce AI Research）、Shafiq Joty（Salesforce AI Research）
- 提交：2025-10-16（v1），最后修订 2026-04-18（v5）
- 分类：cs.AI；状态：Accepted to ICLR 2026
- URL：https://arxiv.org/abs/2510.14240 ；DOI：10.48550/arXiv.2510.14240
- 代码：https://github.com/SalesforceAIResearch/LiveResearchBench
- 许可：CC BY-NC-SA 4.0
- OpenAlex：W7092298889（2025-10-16 收录，cited_by_count=0，preprint/arXiv repository 收录）

### 1.2 摘要（原文）

> Deep research -- producing comprehensive, citation-grounded reports by searching and synthesizing information from hundreds of live web sources -- marks an important frontier for agentic systems. To rigorously evaluate this ability, four principles are essential: tasks should be (1) user-centric, reflecting realistic information needs, (2) dynamic, requiring up-to-date information beyond parametric knowledge, (3) unambiguous, ensuring consistent interpretation across users, and (4) multi-faceted and search-intensive, requiring search over numerous web sources and in-depth analysis. Existing benchmarks fall short of these principles, often focusing on narrow domains or posing ambiguous questions that hinder fair comparison. Guided by these principles, we introduce LiveResearchBench, a benchmark of 100 expert-curated tasks spanning daily life, enterprise, and academia, each requiring extensive, dynamic, real-time web search and synthesis. Built with over 1,500 hours of human labor, LiveResearchBench provides a rigorous basis for systematic evaluation. To evaluate citation-grounded long-form reports, we introduce DeepEval, a comprehensive suite covering both content- and report-level quality, including coverage, presentation, citation accuracy and association, consistency and depth of analysis. DeepEval integrates four complementary evaluation protocols, each designed to ensure stable assessment and high agreement with human judgments. Using LiveResearchBench and DeepEval, we conduct a comprehensive evaluation of 17 frontier deep research systems, including single-agent web search, single-agent deep research, and multi-agent systems. Our analysis reveals current strengths, recurring failure modes, and key system components needed to advance reliable, insightful deep research. Our code is available at: https://github.com/SalesforceAIResearch/LiveResearchBench.

### 1.3 关键章节节选（arXiv HTML 全文 v5）

#### Introduction（节选）

- "Deep research is the process of addressing complex, open-ended questions that require long-horizon, multi-step reasoning and planning. It involves exploring hundreds of live web sources and synthesizing them into comprehensive, citation-grounded, and structured outputs such as reports (openai2025deepresearch)."
- 四原则："(a) user-centric, reflecting realistic information needs; (b) dynamic, requiring up-to-date information beyond parametric knowledge; (c) unambiguous, ensuring consistent interpretation across users; and (d) multi-faceted and search-intensive, requiring multi-hop search across diverse web sources and in-depth analysis."
- 对现有基准的批评："Recent benchmarks have introduced search-intensive tasks (gou2025mindweb), but these are often static (and thus prone to contamination) (bosse2025deep), domain-specific (xu2025researcherbench; patel2025deepscholarbenchlivebenchmarkautomated), coarse-grained, or ambiguous (du2025deepresearch)—frequently omitting details such as the intended audience, required output format, or scope."
- 基准规模："LiveResearchBench, a benchmark of 100 expert-curated queries paired with detailed checklists, constructed with over 1,500 hours of human labor. The tasks we benchmark span seven diverse domains (e.g., science, business, healthcare) and ten categories such as market analysis, literature review, policy evaluation, and topic exploration."
- 动态任务示例："one task asks for a comprehensive report on the evolution of artistic styles 'up to the present {{date}}'…{{date}} will be replaced by the evaluation date."
- 贡献四点：(1) 四任务设计原则；(2) LiveResearchBench 100 任务；(3) DeepEval 六维度评估套件；(4) 17 系统综合评估，"reveal systematic vulnerabilities and error patterns, and that most models are yet incapable of writing insightful reports."

#### Related Work（节选）

- 系统分类："Single-agent systems place all tool-use decisions in one model. Examples include function-calling LLMs (yang2025qwen3; agarwal2025gpt) and ReAct-style agents (react_yao2022react). Multi-agent systems (MAS) instead coordinate specialized roles such as planner, researcher, and writer in a predefined workflow. Proprietary multi-agent systems such as Grok 4 Heavy (Grok4Heavy2025) and Manus (manus2025) remain undisclosed, while examples of open-source systems include Open Deep Research (alzubi2025opendeepsearch), DeerFlow (DeerFlow2025), and OpenManus (OpenManus2025)."
- 现有基准对照："DeepScholarBench (patel2025deepscholarbenchlivebenchmarkautomated) targets related-work generation; DeepResearch Bench (du2025deepresearch) include 100 short open-ended questions; Deep Research Bench (bosse2025deep), LiveDRBench (java2025characterizing_dr), and Mind2Web2 (gou2025mindweb) primarily target closed-ended information-seeking tasks… they are domain-specific, restricted to short-form or closed-ended answers, and static."
- "Recent efforts such as DeepResearchGym (coelho2025deepresearchgym) adopts short and static tasks, while ResearcherBench (xu2025researcherbench) focuses narrowly on AI domain."
- 对比示例："Deep Research Bench (bosse2025deep) includes search-intensive queries such as How many IM and GM account closures did chess.com report for 2024?, but these are static, time-bounded, and require minimal reasoning"; "DeepResearch Bench (du2025deepresearch) often omits crucial elements such as the target audience, content and format requirements, or a clearly defined scope."

#### 3.1 Task Design Principles（节选）

- 原则来源："we conducted a user survey with participants from diverse backgrounds and occupations, including enterprise professionals, academic researchers and students, and users performing everyday tasks"
- 四原则原文：User-centric（反映目标受众需求）；Unambiguous（明确指定）；Time-varying（"Task requiring real-time search represent a large share of user queries. Such tasks are inherently resistant to data contamination from pretraining corpora, unlike static or time-bounded queries that risk becoming outdated or leaked as LLMs evolve."）；Multi-faceted and search-intensive（多跳搜索+深度分析）。

#### 3.2 Benchmark Overview（节选）

- "It consists of 100 expert-curated questions, each paired with detailed checklists, created through a six-stage curation pipeline…and validated via a five-step quality control process."
- 七个领域：Science & Technology, Economy & Business, Health & Wellbeing, Law & Governance, Society & Culture, Education & Knowledge, Media & Entertainment。
- 十个任务类别：market analysis, technical support, decision support, policy and regulation, literature review, competitive analysis, pros-and-cons comparison, wide information search, topic exploration（等）。

#### 3.3 Benchmark Construction（节选）

- 六阶段管线：用户访谈与群体调查（"What questions would you ask a deep research agent?"）→ 领域专家起草初始问题 → 用两个顶级深度研究模型（OpenAI o3 Deep Research 和 Gemini Deep Research）生成可能的澄清问题 → 人类专家审查并精炼查询（明确 scope/audience/format）→ GPT-5 生成初始 checklists（将查询分解为单元问题/unit tests，如 US enterprise AI services market 任务含 9 个 checklist items）→ 专家验证。

#### 3.4 Data Verification（节选）

- 五阶段验证：专家标注员独立评估每个 query 与 checklist item（appropriate / not appropriate；valid but not necessary / needs modification）→ 质量控管专家审阅标注并判定同意与否 → 第二轮质控抽样检测系统性偏差（"ensure that overall quality deviates by no more than 5% from the true data quality"）→ 第三组专家最终验证与交叉检查、解决冲突、精炼、定稿。

#### 4 DeepEval（节选）

- 六维度：❶ Presentation & Organization，❷ Factual & Logical Consistency，❸ Coverage & Comprehensiveness，❹ Analysis Depth，❺ Citation Association，❻ Citation Accuracy。
- 协议选择：Checklist-based（❶ 和 ❸，binary 0/1）；Pointwise additive（❷ 和 ❺，按发现错误数扣分 0-100）；Pairwise comparison（❹ Analysis Depth，1-5 分/维、位置交换平均、win rate）；Rubric-tree（❻ Citation Accuracy，agentic judge 带 web 访问，结构化验证 URL 可达性与支持性）。
- 单一评分方式被弃用："prompt an LLM judge to assign a single rating within a fixed range (e.g., 0-10)…this approach is unsuitable for any of our metrics. Even with SoTA judges (Gemini-2.5 Pro and GPT-5), agreement with human judgments fell below 60%…differences exceeding 50 points when directly rating analysis depth."
- Agent-Ensemble-as-a-Judge："Gemini 2.5 Pro aligned most closely, followed by GPT-5, while Claude 4 Sonnet exhibited inconsistent and low agreement with human experts…we use Gemini 2.5 Pro and GPT-5 as independent judges and report final scores as the average of their assessments."
- 人类对齐率：Presentation 98.3%；Coverage 100.0% 偏好；Analysis Depth 92.5%；Citation Traceability 85.9%。

#### 5 Main Results（节选）

- 17 个系统分三类：
  - (1) Single-agent + web search：GPT-5, GPT-4.1, GPT-5-mini, Gemini 2.5 Pro, Gemini 2.5 Flash, Claude 4 Sonnet, Claude 4.1 Opus, Perplexity Sonar Reasoning, Perplexity Sonar Reasoning Pro
  - (2) Single-agent deep research：OpenAI o3 Deep Research, OpenAI o4-mini Deep Research, Perplexity Sonar Deep Research, Grok-4 Deep Research (Expert), Gemini Deep Research
  - (3) Multi-agent deep research：Manus, Grok-4 Heavy Deep Research, Open Deep Research, Deerflow+（作者对 DeerFlow 的增强实现："adds inline citations, reference mapping, and robust long-context management"）
  - 备注："Non-reasoning models and multi-agent systems that do not excel at generating long-form reports are excluded due to poor performance in our pilot study."；开源系统 Deerflow+ 与 Open Deep Research 以 GPT-5 为 backbone。
- 四维度评分（Table 1，0-100，judge ensemble 平均）节选：
  - GPT-5：Presentation 71.6 / Fact-Logic 68.3 / Coverage 83.4 / Citation Association 67.6
  - Gemini 2.5 Pro：51.9 / 76.5 / 73.1 / 38.5
  - Claude 4 Sonnet：81.9 / 67.3 / 49.2 / 37.9
  - OpenAI o3 Deep Research：71.3 / 64.2 / 85.0 / 25.6
  - Grok-4 Heavy Deep Research：75.9 / 59.4 / 89.3 / 48.0
  - Deerflow+（w. GPT-5）：78.8 / 69.9 / 61.6 / 77.0
  - Open Deep Research（w. GPT-5）：81.0 / 71.3 / 65.3 / 76.9
- 关键观察（Obs. 原文）：
  - "Multi-agent families lead on average. …Open Deep Research achieves the highest average (73.6), followed by GPT-5 (72.7) and Deerflow+. Averaged by family, multi-agent deep research systems (69.5) outperform both single-agent web (62.8) and single-agent deep research."
  - "Single web agent excels in consistency, multi-agent systems in association, while single-agent deep research lags. …Gemini 2.5 Pro achieves the highest consistency score overall (76.5)…multi-agent systems dominate Citation Association (61.9 avg)…OpenAI o3 Deep Research often produces long reports but leaves key statements/facts uncited, while Grok-4 Heavy Deep Research often cites URLs that fail to support the associated claims. Another common recurring issue is the use of fictional or non-existent links, as seen in Manus."
  - "Models struggle most with citation correctness and formatting, rather than surface fluency."
  - "Coverage benefits from specialization…Grok-4 Heavy Deep Research achieving the highest score (89.3). By contrast, Deerflow+ (61.6) and Open Deep Research…"（截断）
- 引文准确率深层分析（Table 7，附录 E）：对 GPT-5、Grok-4 Deep Research、Open Deep Research 在最需搜索的两类任务上统计 E1 URL 无效 / E2 URL 无关 / E3 未支持主张三类错误，按报告平均：
  - Wide Info Search：GPT-5 4.2/1.7/13.3（合计 19.2）；Grok-4 DR 6.8/6.8/33.4（47.0）；Open DR 5.0/5.2/19.7（29.9）
  - Market Analysis：GPT-5 11.1/10.1/43.8（65.0）；Grok-4 DR 6.3/6.4/61.5（74.2）；Open DR 11.9/11.6/68.4（91.9）
  - 论文原文结论："all models produce non-trivial citation errors. In wide information search, most errors stem from unsupported claims (claims not verifiable from the cited link) rather than invalid or irrelevant URLs…highlighting that hallucinations persist even with web access. The problem is worse for market analysis…underscoring citation accuracy as a persistent bottleneck in deep research."

#### 6 Conclusion（原文）

> "We introduced LiveResearchBench, a benchmark of 100 expert-curated, dynamic tasks for deep research, and DeepEval, a comprehensive evaluation suite spanning six dimension for citation-grounded reports. Our evaluation of 17 leading systems shows that while agents can gather and organize information, they struggle with citation reliability and analytical depth. LiveResearchBench and DeepEval establish a rigorous foundation for benchmarking and point toward future advances in memory, compression, and synthesis as key to enabling truly insightful deep research."

---

## 二、GAIA（arXiv:2311.12983）

### 2.1 元数据（arXiv API 获取）

- 标题：GAIA: a benchmark for General AI Assistants
- 作者：Grégoire Mialon、Clémentine Fourrier、Craig Swift、Thomas Wolf、Yann LeCun、Thomas Scialom
- 提交：2023-11-21（v1，无后续版本）
- 分类：cs.CL, cs.AI
- URL：https://arxiv.org/abs/2311.12983 ；DOI：10.48550/arXiv.2311.12983
- OpenAlex：W4388964563（2023-11-21 收录，arXiv 收录 cited_by_count=9，counts_by_year: 2024=3, 2025=5, 2026=1）
- Meta 官方研究页：https://ai.meta.com/research/publications/gaia-a-benchmark-for-general-ai-assistants （2024-05-06 发布）

### 2.2 摘要（原文）

> We introduce GAIA, a benchmark for General AI Assistants that, if solved, would represent a milestone in AI research. GAIA proposes real-world questions that require a set of fundamental abilities such as reasoning, multi-modality handling, web browsing, and generally tool-use proficiency. GAIA questions are conceptually simple for humans yet challenging for most advanced AIs: we show that human respondents obtain 92% vs. 15% for GPT-4 equipped with plugins. This notable performance disparity contrasts with the recent trend of LLMs outperforming humans on tasks requiring professional skills in e.g. law or chemistry. GAIA's philosophy departs from the current trend in AI benchmarks suggesting to target tasks that are ever more difficult for humans. We posit that the advent of Artificial General Intelligence (AGI) hinges on a system's capability to exhibit similar robustness as the average human does on such questions. Using GAIA's methodology, we devise 466 questions and their answer. We release our questions while retaining answers to 300 of them to power a leader-board available at https://huggingface.co/gaia-benchmark.

### 2.3 GAIA Leaderboard README（官方原文节选，huggingface.co/spaces/gaia-benchmark/leaderboard）

- "GAIA is made of more than 450 non-trivial question with an unambiguous answer, requiring different levels of tooling and autonomy to solve. It is therefore divided in 3 levels, where level 1 should be breakable by very good LLMs, and level 3 indicate a strong jump in model capabilities. Each level is divided into a fully public dev set for validation, and a test set with private answers and metadata."
- 禁止条款："**Please do not repost the public dev set, nor use it in training data for your models.**"
- 提交与评估："Submission made by our team are labelled 'GAIA authors'. While we report average scores over different runs when possible in our paper, we only report the best run in the leaderboard."；"Results can be submitted for the test set (we closed the validation leaderboard, as it was no longer informative)."
- 评估方式："Each question calls for an answer that is either a string (one or a few words), a number, or a comma separated list of strings or floats…There is only one correct answer. Hence, evaluation is done via quasi exact match between a model's answer and the ground truth (up to some normalization that is tied to the 'type' of the ground truth)."
- 系统提示词模板（要求 FINAL ANSWER: [YOUR FINAL ANSWER] 格式）；提交格式 {"task_id", "model_answer", "reasoning_trace"(optional)}；scoring function 公开在 https://huggingface.co/spaces/gaia-benchmark/leaderboard/blob/main/scorer.py。

### 2.4 GAIA Dataset Card（官方原文节选，huggingface.co/datasets/gaia-benchmark/GAIA）

- 防爬/防转发官方声明（泄露事件官方应对）："We added gating to prevent bots from scraping the dataset. Please do not reshare the validation or test set in a crawlable format."
- "GAIA is made of more than 450 non-trivial question with an unambiguous answer, requiring different levels of tooling and autonomy to solve. It is therefore divided in 3 levels…Each level is divided into a fully public dev set for validation, and a test set with private answers and metadata."
- 2025-10 格式更新（官方）："To keep GAIA compatible with HF datasets 4.x where code-based dataset loaders are deprecated—we now ship Parquet-backed splits that mirror the former JSONL structure: metadata.parquet carries the full split, and companion files like metadata.level1.parquet retain the per-level views…Columns remain task_id, Question, Level, Final answer, file_name, file_path, and the struct-valued Annotator Metadata."
- 数据规模（官方）："GAIA is made of more than 450 non-trivial question"（leaderboard README 同）；论文摘要表述为 "we devise 466 questions and their answer. We release our questions while retaining answers to 300 of them"。

---

*存档完毕。本文件内容均为上述官方来源的原文或节选；LRB 全文节选来自 arXiv HTML v5（https://arxiv.org/html/2510.14240v5），GAIA 节选来自 arXiv 摘要 + HuggingFace 官方空间/数据集页（访问日期 2026-08-04）。*

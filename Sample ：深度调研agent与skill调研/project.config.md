# 项目配置：深度调研agent与skill调研

> 本项目级的配置文件。Agent 在进入本项目时读取此文件获取上下文。
> 所有路径以本项目目录为基准。
> **本文件只承载静态定义，PLAN_REVIEW 后冻结**——批次进度、keywords、dead_ends、用户阶段性意见一律写入 `run-state.md`，不写本文件。

---

## 元信息

- **项目名：** 深度调研agent与skill调研
- **创建日期：** 2026-08-04
- **当前 Phase：** 1
- **内存分区标签：** `research:深度调研agent与skill调研`
- **qmd 集合名：** `深度调研agent与skill调研`
- **plan_status：** approved（2026-08-04 用户确认客观生态观察方案）
- **execution_mode：** continuous
- **execution_status：** not_started
- **research_type：** 技术调研
- **research_subtype：** 生态调研（客观横向观察）
- **strategy_tags：** [官方参数, 专业评测, 社区反馈, 论文]
- **research_axis：** { primary: "深度调研agent与skill生态能力/架构/工作流/成本/开放度/局限客观横向对比（开源框架/skill + 付费服务）", secondary: ["生态方法/技术流派与趋势观察（论文驱动 vs 工程驱动、agent loop 流派等）", "付费服务市场与定价（市场商业维度）"] }
- **type_notes：** 混合任务：研究对象为"深度调研服务"技术产品生态（开源框架/skill + 付费服务），主类型按研究对象与最终产物定为技术调研；定位为**客观生态观察**——如实收集证据、横向对比、观察方法流派，不产出改进方向建议；与自有平台（调研管理平台：状态机+证据链+知识底座）的对比不写入调研任务，由最终知识分析自然得出；付费服务涉及定价/成本与市场格局，带市场商业副轴。付费/开源可能重叠，按产品形态归类（如 open-source Deep Research 复刻 vs 闭源商业服务），不按是否收费一刀切。

---

## 调研目标（四问，必填，一句话填不下是项目定义不清）

> **禁止循环定义**：objectives 是调研**之前**就定义的起点，不准引用调研产物（CLxxxx/Sxxxx/Axxxx）--那些是调研后才有。场景只写"场景名+一句话说明"，不写证据锚点（证据是调研结果，不是目标）。
> **禁止内部ID**：本段面向人类，必须业务性表述（见根 AGENTS.md "面向人类表述规范"）。

> 目标回答**为什么、给谁、产出什么、服务哪些场景**——不写"工艺"（怎么挖怎么沉淀属下方"调研工艺"段）。

```yaml
objectives:
  problem: "当前可用的'深度调研服务'生态（开源框架/skill 与付费服务）各自具备什么能力、采用什么架构与工作流、成本与开放程度如何、存在哪些已知局限，生态内有哪些方法/技术流派与趋势？本调研客观收集证据并横向对比，不做改进方向建议；与自有平台（调研管理平台：状态机管控 + raw/采录/分析/知识包证据链 + zhishibao 可持续复用知识底座 + 无付费 API 依赖）的对比不写入调研任务，由最终知识分析自然得出。"
  audience: "用户本人（深度调研平台维护者/使用者，首要服务对象）"
  deliverables: "生态横向对比知识包（可复用、可追溯、可持续扩展）+ 生态横向对比报告（客观观察，无改进建议）+ 深度调研工具生态对比维度体系（能力/架构/工作流/成本/开放度/局限六维）"
  scenarios:                              # 重点支撑场景，多场景枚举（只写场景名+一句话说明，不引用CL/S/A）
    - name: "生态理解与对外汇报"
      desc: "向他人清晰说明深度调研工具生态的格局、产品形态分类、方法流派、趋势与各方案差异"
    - name: "工具/框架参考依据"
      desc: "为后续可能的引入/选型提供证据化横向对比事实（本调研只提供客观事实，不产出推荐结论）"
    - name: "最终知识分析锚点"
      desc: "本平台 vs 生态的对比由最终知识分析自然得出，本调研不采集该对比内容，仅保留作为知识分析的可选锚点"
```
> 注：scenarios 是"这套知识体系用在哪"（平台维护/选型/汇报），不是"要研究什么机制"（研究目标归 core_questions）。

---

## 调研工艺/流程（怎么挖、怎么沉淀）

> 工艺与目标是正交维度。目标回答"为什么/给谁/产出什么"，本段回答"怎么做"——挖掘策略、采录档位、采录模板、关系型/对比导向、合并节奏。

```yaml
process:
  collection_mode: "MapReduce(新协议)"
  extraction_levels: ["deep", "light"]      # 开源框架/架构类 deep，付费服务功能/定价类 light
  merge_cadence: "每5批次 consolidation（知识管理员）"
  relation_orientation: "关系型 为主 + 冲突导向 (opposing 必须仲裁)"
  schema_granularity: "断言=主体+关系+客体+边界+置信度+来源（见 standards/extraction-format.md SPO 表格）"
  saturation_gate: "8条饱和判定（见知识管理员 AGENTS.md Step 5）"
```

---

## 策略映射

> 策略映射表是 PLAN_REVIEW 方案草案的第一个结构化产物（固定 6 列），并作为机器读取对象落入本段 yaml 与 `1-规划/1-任务规划.md`、`1-规划/task_queue.md`、`1-规划/4-知识包设计.md`。

```yaml
strategy_mapping:
  classification:
    research_type: "技术调研"
    research_subtype: "生态调研（客观横向观察）"
    strategy_tags: [官方参数, 专业评测, 社区反馈, 论文]
    research_axis:
      primary: "深度调研agent与skill生态能力/架构/工作流/成本/开放度/局限客观横向对比（开源框架/skill + 付费服务）"
      secondary: ["生态方法/技术流派与趋势观察（论文驱动 vs 工程驱动、agent loop 流派等）", "付费服务市场与定价（市场商业维度）"]
    type_notes: "混合任务：研究对象为深度调研服务技术产品生态，主类型技术调研；定位为客观生态观察——如实收集证据、横向对比、观察方法流派，不产出改进方向建议；本平台对比由最终知识分析自然得出，不写入调研任务；付费服务含市场/定价副轴。付费/开源按产品形态归类，不按是否收费一刀切。"
    confidence: 0.7
    rationale: "研究对象是技术产品（agent 深度调研系统/skill），最终产物是客观生态横向对比知识包与报告，符合技术调研定位；STORM 等方案有论文溯源（arXiv），故加'论文'标签启用学术引擎；付费服务定价/成本与社区口碑分别由'官方参数''社区反馈'覆盖。生态调研无专用 scenario 策略文件，采集字段模型复用 scenarios/技术选型.md（仅作客观采集，不做选型推荐）。"
    counter_risks: ["付费服务能力信息多来自官方营销声明，须以专业评测/社区反馈交叉验证", "生态更新快（2025-2026 密集迭代），存在时效性风险，需记录采集时间点", "开源项目功能迭代快，能力描述可能落后于最新 commit，需以 README/release 为准并标注版本/时间", "不同方案评测基准不统一，性能数据须注明测试条件", "客观观察定位下须防'本平台先入为主的对比视角'污染采录，调研阶段不得产出改进/借鉴判断"]
    alternatives: ["市场商业（若用户重点转向付费服务市场份额与商业模式时采用）", "通用（若仅做概览不做横向对比时采用）"]
  rows:
    - strategy_file: "types/技术调研.md"
      field_model: ["source_strategy：官方文档/架构说明/API、GitHub README/examples/issues/releases、论文/技术报告/benchmark/评测、生产案例/迁移经验/故障复盘、竞品/替代方案文档、反方观点/已知缺陷/限制说明", "evidence_ranking：源码/官方文档/论文原文 > 可复现实验/benchmark > issue 与真实案例 > 深度技术文章 > 一般博客/转述", "extraction_questions：解决什么问题/依赖前提/核心架构组件/数据流状态流调用链/对外接口配置/性能测试条件/替代方案取舍/已知限制失败场景/官方声称vs独立验证", "synthesis_dimensions：架构模式/能力边界/工程复杂度/性能表现/可维护性/生态成熟度/风险/替代方案/落地路径"]
      collection_direction: "每个开源方案（deep-research/OpenDeepResearch/STORM/hyperresearch/深度调研类 skill/agent框架内置能力）抓 GitHub README+docs+release+issues 与官方架构说明；付费服务抓产品官网能力页/定价页/帮助文档；有论文的（STORM 等）走 arxiv/openalex 取摘要；采集时标注版本与时间"
      evidence_questions: ["该方案解决什么核心问题？", "核心架构组件与 agent loop/规划/检索/记忆/工具如何组织？", "数据流/状态流/调用链如何运转？", "官方声称能力 vs 独立验证证据分别是什么？", "已知限制/失败场景/迁移成本有哪些？"]
      expected_outputs: ["raw-S*.md（每方案 1 篇以上）→ 采集记录-S*.md → 单源分析-A*.md（能力/架构/工作流/局限）→ 知识包断言与关系（solution→capability/architecture/limitation）", "支撑报告：生态横向对比报告（客观观察，无改进建议）"]
      strategy_gap: "无"
    - strategy_file: "scenarios/技术选型.md"   # 生态调研无专用 scenario 文件，复用技术选型采集字段模型（仅客观采集，不做选型推荐）
      field_model: ["技术目标", "业务/调研场景", "候选方案", "方案类型", "核心能力", "关键组件", "接口/协议", "部署方式", "运行环境", "依赖条件", "数据输入", "数据输出", "性能指标", "稳定性指标", "安全风险", "合规边界", "成本结构", "维护活跃度", "社区生态", "文档质量", "许可证", "集成复杂度", "迁移成本", "扩展能力", "失败场景", "替代方案", "适用条件", "排除条件", "验证状态", "证据来源", "可信度"]
      collection_direction: "按候选方案矩阵逐项填写：每个方案覆盖'核心能力/关键组件/部署方式/依赖条件/成本结构/维护活跃度/许可证/失败场景/替代方案/适用排除条件'；付费服务补'接口协议（API 可用性）/合规边界（ToS/隐私）'；开源补'自托管/集成复杂度'；最终形成能力覆盖/可获得性/稳定性/成本/合规/生态/集成/可迁移/失败降级九维客观对比矩阵（只记录事实，不产出推荐结论）"
      evidence_questions: ["每个方案属于官方 API/开源工具/商业服务/自研哪类路径？", "核心能力哪些是声明、哪些已被验证？", "依赖什么外部条件（API 配额/浏览器环境/代理/账号权限）？", "成本结构（订阅/API/自托管资源/代理）如何？", "失败场景与降级策略是什么？", "许可证与合规边界（平台 ToS/数据授权）是什么？", "方案间在六维锚点上呈现哪些客观差异？"]
      expected_outputs: ["跨源对比-C*.md（候选方案矩阵/能力覆盖/成本/合规/失败降级）", "知识包 comparison_anchors 与 limitation 节点", "支撑报告：生态横向对比报告（六维矩阵客观对照）"]
      strategy_gap: "有：scenarios/生态调研.md 策略文件缺失，复用 scenarios/技术选型.md 的采集字段模型（去掉'推荐结论'列，仅客观采集），待策略库补齐"
    - strategy_file: "sources/官方参数.md"
      field_model: ["参数定义和测试条件", "硬约束 vs 营销表达", "对用户场景真正重要的参数", "第三方实测/社区反馈/投诉验证", "口径包装/缺省条件/不可比指标"]
      collection_direction: "采集各方案官网能力页/定价页/技术文档/API 文档与 GitHub README 中的声明能力、接口、许可证、版本边界；标注'官方声称'性质，禁止直接当作真实性能"
      evidence_questions: ["该官方参数是硬约束还是营销表达？", "测试条件/口径是什么？", "是否有第三方实测或社区反馈验证该声明？", "付费服务的定价/用量限制是否明确？"]
      expected_outputs: ["raw-S* 中的官方参数记录（标注声明性质）", "知识包断言带 evidence_ranking 提示（官方声称需交叉验证）"]
      strategy_gap: "无"
    - strategy_file: "sources/专业评测.md"
      field_model: ["测试方法和样本是否公开", "测试场景是否符合真实使用", "结论是否可复核", "利益相关/厂商送测/软文倾向", "功能效果是否被量化", "评测结论是否被社区反馈支持"]
      collection_direction: "采集第三方对 deep research 服务的横向评测/benchmark/实测文章（技术博客/评测媒体/独立 benchmark 仓库），优先有方法、可复核数据、横向对比与长期测试者；记录测试方法与样本"
      evidence_questions: ["评测方法和样本是否公开？", "测试场景与真实使用是否一致？", "是否有利益相关或厂商送测倾向？", "性能/效果数据是否被量化且可复核？"]
      expected_outputs: ["raw-S* 评测类采录 → 跨源对比-C*（性能/效果横向差异）", "知识包 benchmark/limitation 断言带测试条件"]
      strategy_gap: "无"
    - strategy_file: "sources/社区反馈.md"
      field_model: ["具体经历/真实需求/情绪表达/营销内容", "用户场景/条件/使用周期", "高频痛点/后悔点/安装雷区/长期使用问题", "多人复现或跨平台共现", "与官方参数/专业评测冲突", "平台偏差/营销/水军/个案"]
      collection_direction: "采集 GitHub Issues/Reddit/X/知乎/公众号/技术社区对 deep research 工具与付费服务的真实使用反馈，重点挖高频痛点、失败场景、官方宣传落差、开源项目 issue 中的能力缺陷；单条不直接定性，须聚类+标注平台偏差"
      evidence_questions: ["这是真实经历还是营销内容？", "高频痛点/后悔点/长期使用问题是什么？", "是否多人复现或跨平台共现？", "与官方参数/专业评测是否冲突？", "抓不到全文时是否已记录线索？"]
      expected_outputs: ["raw-S* 社区反馈采录（标注频次/平台偏差）", "知识包 limitation/risk 断言 + source-leads 线索", "跨源对比-C* 中官方声称 vs 真实口碑对照"]
      strategy_gap: "无"
    - strategy_file: "sources/论文.md"
      field_model: []  # 策略缺口：sources/ 目录无 论文.md 策略文件，回退 types/技术调研.md 的学术引擎规则（arxiv/openalex 取摘要，PDF 用 opendataloader-pdf 提取）
      collection_direction: "对 STORM（arXiv:2402.14207）等有学术出处的方案走 arxiv/openalex 取论文元数据与摘要，作为算法/架构一手证据；论文摘要直接作 raw 内容，需全文时下载 PDF 提取"
      evidence_questions: ["论文描述的架构与真实实现是否一致？", "基准/实验条件是什么？", "论文声称 vs 社区实测差异？"]
      expected_outputs: ["raw-S* 论文类采录 → 架构/算法维度证据", "知识包 architecture 断言带论文来源"]
      strategy_gap: "有：sources/论文.md 策略文件缺失，学术证据分级与引擎规则暂按 types/技术调研.md 执行（arxiv/openalex），待策略库补齐"
  completeness_checks:
    has_type_row: true
    has_scenario_row: true
    source_rows_cover_all_tags: true
    no_empty_cells: true
    field_model_expanded: true
    discover_ready: true
```

> 运行时搜索参数（breadth/depth/threshold/sources/focus_keywords/exclude/round）已移至 `run-state.md`，本文件不再承载。

---

## 关键链接

- **任务规划：** `1-规划/1-任务规划.md`（其"目标"段须与上方 objectives 对齐）
- **知识包设计：** `1-规划/4-知识包设计.md`
- **运行状态：** `run-state.md`（批次进度/keywords/dead_ends/用户阶段性意见）
- **讨论纪要：** `1-规划/2-讨论纪要.md`
- **进度日志：** `progress.md`
- **发现汇总：** `findings.md`
- **采集日志：** `2-执行/01-采集记录/采集日志.md`
- **分析索引：** `2-执行/02-分析提取/分析索引.md`
- **知识提炼日志：** `2-执行/03-知识提炼/知识提炼日志.md`

---

## 知识包 Schema

> 本段由前置准备阶段根据 `1-规划/4-知识包设计.md` 填充。通用模板不预设具体图谱类型，必须按项目目标动态设计。
> **4 个 goals 字段是 PLAN_REVIEW 验收硬门，缺任一判 NEEDS_REVISION（见 check-plan-review-quality.py）：**

```yaml
knowledge_schema:
  purpose: [reporting, conversation, analysis, comparison, extension]
  research_type: "技术调研"
  research_subtype: "生态调研（客观横向观察）"
  strategy_tags: [官方参数, 专业评测, 社区反馈, 论文]
  research_axis:
    primary: "深度调研agent与skill生态能力/架构/工作流/成本/开放度/局限客观横向对比（开源框架/skill + 付费服务）"
    secondary: ["生态方法/技术流派与趋势观察（论文驱动 vs 工程驱动、agent loop 流派等）", "付费服务市场与定价（市场商业维度）"]
  type_notes: "混合任务：研究对象为深度调研服务技术产品生态，主类型技术调研；定位为客观生态观察——如实收集证据、横向对比、观察方法流派，不产出改进方向建议；本平台对比由最终知识分析自然得出，不写入调研任务。"
  domain_schema:
    node_types:
      - "solution（方案/产品：deep-research/OpenDeepResearch/STORM/hyperresearch/各类 research skill/ChatGPT DR/Perplexity DR/Gemini DR/Genspark/Manus/Operator 等）"
      - "solution_category（方案类别：开源框架/开源skill/付费服务/agent框架内置能力）"
      - "capability（能力：多源检索/深度追问/报告生成/证据引用/知识复用等）"
      - "architecture_component（架构组件：agent loop/规划器/检索器/记忆/工具调用/评测循环）"
      - "workflow_stage（工作流阶段：问题拆解/搜索规划/迭代检索/追问/报告组装）"
      - "method_stream（方法/技术流派：论文驱动 vs 工程驱动、agent loop 流派、静态流程流派等，客观观察用）"
      - "output_form（输出形态：Markdown 报告/HTML/带引用长文/幻灯片）"
      - "pricing（定价/成本：订阅价/API 用量/自托管资源成本/代理成本）"
      - "openness（开放程度：API 可用性/自托管/许可证/数据可导出）"
      - "limitation（局限：失败场景/不可靠点/来源质量/深度限制）"
      - "own_platform（本平台：调研管理平台，证据链驱动+状态机+知识底座）——仅作最终知识分析可选锚点，本调研不采集本平台 vs 生态对比内容"
      - "comparison_dimension（对比维度锚点：能力/架构/工作流/成本/开放度/局限）"
      - "evidence（证据/来源：官方文档/GitHub/评测/社区/论文）"
    edge_types:
      - "belongs_to（solution→solution_category）"
      - "has_capability（solution→capability）"
      - "uses_architecture（solution→architecture_component）"
      - "has_workflow（solution→workflow_stage）"
      - "belongs_to_stream（solution→method_stream，流派归类，客观观察用）"
      - "outputs（solution→output_form）"
      - "priced_at（solution→pricing）"
      - "has_openness（solution→openness）"
      - "has_limitation（solution→limitation）"
      - "compared_with（solution→solution，按 comparison_dimension；不采集 solution→own_platform 对比，由最终知识分析派生）"
      - "opposing/coexist（官方声称 vs 社区实测冲突等）"
    required_chains:
      - "竞品差异链：同类方案（开源组/付费组）按全部对比锚点建立横向对比（客观差异陈述）"
      - "能力-架构映射链：能力 → 支撑该能力的架构组件"
      - "方法流派链：方案 → 所属方法/技术流派 → 流派特征（客观观察，不做优劣判断）"
    required_maps:
      - "方案类别覆盖图（开源框架/skill/付费服务/agent框架内置 4 类均覆盖代表方案）"
      - "能力矩阵覆盖图（多源检索/深度追问/报告生成/证据引用/知识复用 × 各方案）"
    completion_checks:
      - "开源方案覆盖 ≥4（deep-research/OpenDeepResearch/STORM/hyperresearch 或同类），付费服务覆盖 ≥4（ChatGPT/Perplexity/Gemini/Genspark/Manus/Operator 中至少 4 个）"
      - "每个方案均有官方参数来源 + 至少 1 类交叉来源（专业评测/社区反馈/论文）"
      - "竞品差异链按全部 6 个对比锚点建立（客观差异陈述，不产出改进/借鉴判断）"
      - "方法流派链建立，流派特征均有证据支撑（客观归类，不做优劣判断）"
      - "核心问题进入 question_index.can_answer"
      - "已知局限/失败场景/成本均有记录且标注证据类型"
      - "本平台（own_platform）对比不进入本调研采集范围，若出现仅作为知识分析锚点占位"
  core_questions:
    - "深度调研生态中开源框架/skill 与付费服务各有哪些代表方案，按产品形态如何归类？"
    - "各方案的能力边界（多源检索/深度追问/报告生成/证据引用/知识复用）与架构（agent loop/规划器/检索器/记忆/工具）、工作流的关键差异是什么？"
    - "各方案的成本结构、输出形态、开放程度（API/自托管/许可证）与已知局限（失败场景/不可靠点）是什么？"
    - "生态内存在哪些方法/技术流派（论文驱动 vs 工程驱动、agent loop vs 静态流程等）？各流派的代表方案、特征与趋势是什么？"
    - "官方声称 vs 独立验证（专业评测/社区反馈/论文）的差异集中在哪些维度？哪些结论可信度高、哪些是证据缺口？"
  conversation_goals:
    - "回答'某两个方案在 X 维度（能力/架构/工作流/成本/开放度/局限）上如何对比、各自适用什么场景'类客观对比问题（可追溯到方案节点与对比边）"
    - "回答'深度调研工具生态的整体格局/产品形态分类/方法流派/趋势'类概述问题"
    - "回答'官方声称与独立验证/社区口碑在哪些方面存在差异'类证据对照问题"
  reporting_goals:
    - "生态横向对比报告（客观观察：开源 vs 付费、能力矩阵、架构/工作流模式、成本/开放度/局限对照、方法流派与趋势）"
    - "生态证据与缺口说明报告（官方声称 vs 独立验证/社区口碑对照、已知局限与证据缺口标注，无改进建议）"
  comparison_anchors:
    - "能力维度（多源检索/深度追问/报告生成/证据引用/知识复用）"
    - "架构维度（agent loop/规划器/检索器/记忆/工具/状态机）"
    - "工作流维度（问题拆解/搜索规划/迭代检索/追问/报告组装）"
    - "成本与开放程度（定价/API 可用性/自托管/许可证）"
    - "证据与知识管理（证据链/可追溯/冲突仲裁/知识沉淀复用）——生态客观维度；本平台对比不作为调研目标，仅作最终知识分析产物锚点之一"
```

---

## ID 注册表

> ID 编码规则：
> - S{3位} = 采集记录（如 S001 = 第1篇采集的来源）
> - A{3位} = 单源分析（如 A001 = 第1篇分析）
> - C{3位} = 跨源对比（如 C001 = 第1份对比分析）
> - 知识包中引用来源用 S{id}，引用分析结论用 A{id} 或 C{id}

```yaml
id_registry:
  sources: {}      # S001: "标题 → 01-采集记录/采集记录-S001-标题.md"
  analyses: {}     # A001: "主题 → 02-分析提取/单源分析/分析-A001-主题.md"
  comparisons: {}  # C001: "对比主题 → 02-分析提取/跨源对比/对比-C001-主题.md"
```

---

## 备注

- **客观观察定位（2026-08-04 用户确认）**：本调研以"看"为主、客观收集生态证据为主，不做改进方向建议；与自有平台（调研管理平台：AGENTS.md 状态机管控、raw→采录→分析→知识包证据链、zhishibao 可持续复用知识底座、冲突仲裁、无付费 API 依赖）的对比**不写入调研任务**，由最终知识分析自然得出。调研阶段不得产出"本平台应借鉴/应避免/改进方向"类判断（属分析员职责）。
- **对比对象锚定**：本平台仅作为最终知识分析产物的可选锚点之一（对应 comparison_anchors"证据与知识管理"维度），不在本调研采集范围内；生态方案之间的六维横向对比是本调研主体。
- **产品形态归类原则**：开源复刻（如 open-source deep-research）与闭源商业服务（如 ChatGPT Deep Research）可能同名或重叠，一律按产品形态归入"开源框架/skill"或"付费服务"，并在断言 boundary 中注明形态。
- **时效性要求**：生态迭代快，采录时须记录来源的版本号/发布时间/访问日期；评测与性能数据必须记录测试条件。
- **面向人类表述**：报告/反馈不得外显内部 ID；跨源对比与知识包断言保留内部 ID（机器资产）。

# 项目配置：[项目名]

> 本项目级的配置文件。Agent 在进入本项目时读取此文件获取上下文。
> 所有路径以本项目目录为基准。
> **本文件只承载静态定义，PLAN_REVIEW 后冻结**——批次进度、keywords、dead_ends、用户阶段性意见一律写入 `run-state.md`，不写本文件。

---

## 元信息

- **项目名：** [项目名]
- **创建日期：** 2026-XX-XX
- **当前 Phase：** [Phase 编号]
- **内存分区标签：** `research:<项目名>`
- **qmd 集合名：** `<项目名>`
- **plan_status：** draft
- **execution_mode：** continuous
- **execution_status：** not_started
- **research_type：** 通用
- **research_subtype：** 待确认
- **strategy_tags：** []
- **research_axis：** { primary: "待确认", secondary: [] }
- **type_notes：** ""

---

## 调研目标（四问，必填，一句话填不下是项目定义不清）

> **禁止循环定义**：objectives 是调研**之前**就定义的起点，不准引用调研产物（CLxxxx/Sxxxx/Axxxx）--那些是调研后才有。场景只写"场景名+一句话说明"，不写证据锚点（证据是调研结果，不是目标）。
> **禁止内部ID**：本段面向人类，必须业务性表述（见根 AGENTS.md "面向人类表述规范"）。

> 目标回答**为什么、给谁、产出什么、服务哪些场景**——不写"工艺"（怎么挖怎么沉淀属下方"调研工艺"段）。

```yaml
objectives:
  problem: "[一句话陈述要回答的核心问题]"
  audience: "[目标读者/服务方，如 agent/决策者/工程师/创作者]"
  deliverables: "[要产出的能力/文档/知识包形态]"
  scenarios:                              # 重点支撑场景，多场景枚举（只写场景名+一句话说明，不引用CL/S/A）
    - name: "[场景名]"
      desc: "[这个场景要解决什么问题，一句话]"
```

示例（"知识与记忆体系调研"项目）：
```yaml
objectives:
  problem: "构建通用的、服务于多种 agent 定位的知识体系--如何把任意领域的业务知识组织成可被 agent 检索、可派生观点、可冲突仲裁、可复用扩展的体系"
  audience: "agent（首要服务对象，多种定位）/ 决策者（次要）/ 知识工作者（远期）"
  deliverables: "知识包（断言层）+ 知识地图视图 + 体系化设计方法论 + 多场景派生路径"
  scenarios:
    - name: "AI运维（重点示例）"
      desc: "agent 在运维场景下获得业务知识--本项目重点深挖的示例场景"
    - name: "知识创作类"
      desc: "agent 辅助写作/内容生产/资料整理所需的知识支撑"
    - name: "技术类"
      desc: "agent 辅助开发/调试/架构/选型所需的技术知识支撑"
```
> 注：scenarios 是"这套知识体系用在哪"（agent 定位/使用领域），不是"要研究什么机制"（研究目标归 core_questions）。

---

## 调研工艺/流程（怎么挖、怎么沉淀）

> 工艺与目标是正交维度。目标回答"为什么/给谁/产出什么"，本段回答"怎么做"——挖掘策略、采录档位、采录模板、关系型/对比导向、合并节奏。

```yaml
process:
  collection_mode: "MapReduce(新协议) | 原批次(旧协议兼容)"
  extraction_levels: ["deep", "light"]      # 采录档位（见 prompts/value-judgment.md）
  merge_cadence: "每5批次 consolidation（知识管理员）"
  relation_orientation: "关系型 为主 + 冲突导向 (opposing 必须仲裁)"
  schema_granularity: "断言=主体+关系+客体+边界+置信度+来源（见 standards/extraction-format.md SPO 表格）"
  saturation_gate: "8条饱和判定（见知识管理员 AGENTS.md Step 5）"
```

```yaml
strategy_mapping:  # 填写规则见下方"策略映射"段
  classification:
    research_type: "通用"
    research_subtype: "待确认"
    strategy_tags: []
    research_axis:
      primary: "待确认"
      secondary: []
    type_notes: ""
    confidence: 0.0
    rationale: ""
    counter_risks: []
    alternatives: []
  rows:
    - strategy_file: "types/通用.md"
      field_model: []
      collection_direction: []
      evidence_questions: []
      expected_outputs: []
      strategy_gap: "待前置准备填充"
  completeness_checks:
    has_type_row: false
    has_scenario_row: false
    source_rows_cover_all_tags: false
    no_empty_cells: false
    field_model_expanded: false
    discover_ready: false
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
  purpose: []              # 知识包未来用途：reporting/conversation/analysis/comparison/extension
  research_type: ""        # 决策支持/技术调研/源码调研/市场商业/文史人文/政策法规/知识创作/舆情用户研究/通用
  research_subtype: ""     # 产品选型/技术选型/供应商选型/竞品分析/需求发现/风险避坑/源码理解等
  strategy_tags: []        # 社区反馈/电商评价/售后投诉/官方参数/专业评测等
  research_axis:           # 混合任务的研究主轴/副轴
    primary: ""
    secondary: []
  type_notes: ""           # 分类说明
  domain_schema:
    node_types: []         # 本项目图谱节点类型
    edge_types: []         # 本项目图谱边类型
    required_chains: []    # 必须建立的链/图
    required_maps: []      # 必须建立的覆盖图/对照图
    completion_checks: []  # 完成/饱和检查项
  core_questions: []       # 知识包完成后必须能回答的问题（验收硬门，≥3）
  conversation_goals: []   # 后续分析员对话要支持的能力（验收硬门，≥2）
  reporting_goals: []      # 可支撑的报告类型（验收硬门，≥1）
  comparison_anchors: []   # 跨项目对比锚点（验收硬门，≥1）
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

[项目特定的注意事项、约束、偏好等]

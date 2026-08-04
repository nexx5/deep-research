# 预设配置库

> 每个 preset 定义一种报告风格：结构模型、叙事组合、色板、组件选配、章节骨架。

---

## overview-md（默认概貌性 Markdown 报告）

```yaml
name: overview-md
label: 概貌性报告
reader: 未额外指定时的默认读者；需要先建立全局理解的人
structure_model: 讲解型总览
narrative:
  opening: 读者基准 + 一句话理解
  argument: 场景化解释
  progression: 从整体到关键机制
  closing: 后续问题
palette_default: blue-orange
palette_options:
  - blue-orange
  - warm-paper
components:
  - concept-card
  - card-comparison
  - gap-box
  - source-tag
```

### 章节骨架模板

```markdown
# {报告标题}

## 读者基准
说明读者已经知道什么、不知道什么、本报告帮助其建立什么理解。

## 一句话理解{主题}
用一段话建立总体心智模型。

## 先看整体图景
用自然叙事说明对象由哪些部分组成，这些部分为什么需要协作。

## 关键机制
按读者理解路径组织，不机械暴露“读者已知/场景/解决之道/效果价值”等方法标签。

## 重要取舍与代价
说明方案为什么这样设计，以及带来的复杂性。

## 读完后可以继续追问的问题
列出后续深挖问题。

## 附录：来源与引用
- 附录只能列外显来源：原始URL、标题、源件路径、源码符号。
- 不得用"知识包/采录/raw/分析/链路资产"作为来源名称。
```

---

## explanatory-overview（讲解型概貌报告）

```yaml
name: explanatory-overview
label: 讲解型概貌报告
reader: 有相关使用经验，但不了解内部流程和技术机制的读者
structure_model: 教学型解释
narrative:
  opening: 读者基准
  argument: 问题驱动解释
  progression: 一次完整流程 → 分层机制 → 设计取舍
  closing: 问题清单
palette_default: blue-orange
palette_options:
  - blue-orange
  - warm-paper
components:
  - concept-card
  - card-comparison
  - gap-box
  - source-tag
```

### 写作规则

- 术语不是少讲，而是必须讲明白。
- 核心术语首次出现时，先讲为什么需要它，再给术语名。
- 场景、问题、解决之道、效果价值可以出现，但不得机械固定为每节小标题。
- 正文和图文输出默认不出现内部编号或内部置信度。
- 附录只能列外显来源：原始URL、标题、源文件路径、源码符号。
- 不得用"知识包/采录/raw/分析/链路资产"作为来源名称。

### 章节骨架模板

```markdown
# {报告标题}

## 读者基准

## 一句话理解{主题}

## 当你发出一次请求时，系统内部发生了什么

## 为什么需要这些内部层次

## 关键机制逐层讲解

## 这些设计带来的价值与代价

## 读完后应该产生的问题

## 附录：来源与引用
```

---

## comparison-report（对比报告）

```yaml
name: comparison-report
label: 对比报告
reader: 需要横向判断差异、取舍和适用边界的读者
structure_model: 维度对比 + 取舍解释
narrative:
  opening: 对比对象与读者目标
  argument: 维度化对比
  progression: 相同点 → 差异点 → 取舍 → 适用场景
  closing: 选择建议或后续问题
palette_default: purple-green
palette_options:
  - purple-green
  - blue-orange
components:
  - card-comparison
  - conflict-view
  - gap-box
  - source-tag
```

### 章节骨架模板

```markdown
# {报告标题}

## 读者基准与对比目标

## 对比对象一句话定位

## 核心维度对比

## 差异背后的设计取舍

## 适用场景

## 尚不能判断的部分

## 附录：来源与引用
```

---

## deep-research（深度调研报告）

```yaml
name: deep-research
label: 深度调研报告
reader: 需要全面理解领域现状、方案优劣、历史脉络的决策者或技术负责人
structure_model: 横纵分析法
narrative:
  opening: SCQA
  argument: CER
  progression: Data Story Arc
  closing: AIDA
palette_default: blue-orange
palette_options:
  - blue-orange
  - warm-paper
components:
  - card-finding
  - card-comparison
  - conflict-view
  - timeline-item
  - gap-box
  - evidence-chain
  - source-tag
  - concept-card
  - card-finding
```

### 读者定位段模板

```markdown
<div class="reader-profile">
  <p>本报告面向 <strong>决策者与技术负责人</strong>，提供对 {领域/主题} 的全景式深度分析。
  报告采用横纵分析法：纵向梳理发展历程与关键转折，横向对比主流方案与竞品，
  交汇处给出推荐与取舍建议，并用自然语言说明证据强弱。</p>
  <p>读者无需具备 {领域} 前置知识——核心概念均以三段式卡片（痛点→是什么→怎么工作）讲解。</p>
</div>
```

### 章节骨架模板

```markdown
# {报告标题}

## 读者定位
{读者定位段}

## 执行摘要
2-3 段，覆盖：核心结论 + 关键发现 + 重大矛盾 + 缺口声明

## 纵向叙事：{领域}历程
### {阶段1标题}
timeline-item × N
### {阶段2标题}
timeline-item × N
### 关键转折点
card-finding × 关键转折

## 横向对比：方案/竞品
### 方案总览
card-comparison × 对比组
### 矛盾与分歧
conflict-view × 矛盾点

## 交汇推荐
### 综合判定
card-finding× 核心结论
### 取舍建议
card-finding × 每个取舍维度

## 矛盾与取舍
conflict-view × 未裁决矛盾
gap-box × 单源/无源结论

## 缺口声明
gap-box × 待补项
concept-card × 需进一步学习的概念

## 来源与引用
source-tag × 全部来源
```

---

## decision-guide（决策指南）

```yaml
name: decision-guide
label: 决策指南
reader: 需要快速拿到结论和行动建议的决策者
structure_model: 倒金字塔
narrative:
  opening: PAS
  argument: 结论先行
  progression: null
  closing: null
palette_default: purple-green
palette_options:
  - purple-green
  - blue-orange
components:
  - card-finding
  - card-finding
  - gap-box
  - kpi-card
  - source-tag
  - conflict-view
```

### 读者定位段模板

```markdown
<div class="reader-profile">
  <p>本指南面向 <strong>需要快速决策的负责人</strong>，采用倒金字塔结构：
  核心结论先行，行动建议紧跟，关键发现与风险在后支撑。
  建议使用自然语言说明依据强弱，缺口显式标出。</p>
  <p>阅读时间约 {N} 分钟。如需完整论证，请参阅对应的深度调研报告。</p>
</div>
```

### 章节骨架模板

```markdown
# {报告标题}

## 读者定位
{读者定位段}

## 核心结论
card-finding × 1-3 条
kpi-card × 关键指标

## 行动建议
### ✅ 建议1
card-finding
### ❌ 建议2
card-finding
### ⚠️ 建议3
card-finding

## 关键发现
card-finding × N
conflict-view × 矛盾点

## 风险
gap-box × 风险项
conflict-view × 待裁决矛盾

## 时间线
timeline-item × 里程碑

## 来源统计
source-tag × 全部来源
kpi-card × 来源数/覆盖领域数
```

---

## action-guide（行动指南）

```yaml
name: action-guide
label: 行动指南
reader: 需要按步骤执行的具体操作人
structure_model: 倒金字塔+步骤式
narrative:
  opening: PAS
  argument: 结论先行
  progression: null
  closing: AIDA
palette_default: purple-green
palette_options:
  - purple-green
  - blue-orange
components:
  - card-finding
  - step-card
  - card-finding
  - gap-box
  - source-tag
  - concept-card
```

### 读者定位段模板

```markdown
<div class="reader-profile">
  <p>本指南面向 <strong>具体执行人</strong>，提供可照着做的分步操作指引。
  每步附检查清单，关键概念以三段式卡片讲解，风险和注意事项前置提醒。</p>
  <p>预计完成时间：{N} 小时/天。需准备：{前置条件}。</p>
</div>
```

### 章节骨架模板

```markdown
# {报告标题}

## 读者定位
{读者定位段}

## 核心结论
card-finding × 1-2 条
concept-card × 需要理解的核心概念

## 行动步骤
### 步骤1：{标题}
step-card（序号+内容+检查清单）
### 步骤2：{标题}
step-card
### 步骤N：{标题}
step-card

## 风险与注意事项
gap-box × 风险项
card-finding × 已知坑点

## 时间表
timeline-item × 各步骤预期时间

## 来源
source-tag × 全部来源
```

---

## technical（技术报告）

```yaml
name: technical
label: 技术报告
reader: 需要复现/评估技术方案的工程师
structure_model: IMRaD
narrative:
  opening: SCQA
  argument: Toulmin
  progression: null
  closing: null
palette_default: blue-orange
palette_options:
  - blue-orange
components:
  - card-finding
  - card-finding
  - evidence-chain
  - gap-box
  - source-tag
  - concept-card
  - card-comparison
```

### 读者定位段模板

```markdown
<div class="reader-profile">
  <p>本报告面向 <strong>工程师</strong>，采用 IMRaD 结构（引言-方法-结果-讨论），
  给出可直接照着干的安装/配置/架构/API/benchmark 信息。
  论证遵循 Toulmin 模型（主张→数据→担保→支撑→反驳→限定），每条结论附带证据链。</p>
  <p>前置知识：{所需基础}。</p>
</div>
```

### 章节骨架模板

```markdown
# {报告标题}

## 读者定位
{读者定位段}

## 摘要
card-finding × 核心结论
kpi-card × 关键指标（可选）

## 背景与动机
concept-card × 核心概念
evidence-chain × 问题链

## 方法
card-comparison × 方案对比
concept-card × 方法核心概念

## 结果
card-finding × 每个关键结果
evidence-chain × 结果证据链

## 讨论
### 局限性
gap-box × 局限项
conflict-view × 争议点
### 建议
card-finding × 建议项

## 来源
source-tag × 全部来源
```

---

---

## knowledge-creation（知识创作/知乎体）

```yaml
name: knowledge-creation
label: 知识创作
reader: 对领域好奇的普通读者/知乎用户
structure_model: 故事化+反常识洞察
narrative:
  opening: Story Spine（故事钩）
  argument: 反常识洞察（先破后立）
  progression: Story Spine（案例叙述）
  closing: AIDA（金句收束）
palette_default: warm-paper
palette_options:
  - warm-paper
  - blue-orange
components:
  - card-finding
  - concept-card
  - conflict-view
  - timeline-item
  - source-tag
```

### 读者定位段模板

```markdown
<div class="reader-profile">
  <p>本文面向 <strong>对{领域}好奇的读者</strong>，用故事化叙事带你理解一个反常识的真相。
  不堆砌术语，先讲"为什么重要"，再讲"是什么"，最后给出"能怎么用"。</p>
  <p>阅读时间约 {N} 分钟。如有疑问，欢迎评论区讨论。</p>
</div>
```

### 章节骨架模板

```markdown
# {标题：结论先行，带悬念或反常识}

## 读者定位
{读者定位段}

## 故事钩
Story Spine 开场：一个具体的场景/事件/人物，引出核心问题。

## 反常识洞察
### 你以为的真相
conflict-view（立场A：常见误解）
### 实际的真相
conflict-view（立场B：调研发现的反常识结论）

## 它是什么
concept-card × 核心概念（痛点→是什么→怎么工作）

## 案例与证据
timeline-item × 关键事件/演变
card-finding × 每个关键发现

## 怎么用
### 对个人的意义
card-finding
### 对行业的意义
card-finding

## 金句收束
一句话总结核心洞察，留有余味。

## 来源
source-tag × 全部来源
```

---

## brief（简明报告）

```yaml
name: brief
label: 简明报告
reader: 需要快速了解结论和可信度的决策者/执行者
structure_model: 一页纸
narrative:
  opening: 结论先行
  argument: 关键发现列表
  progression: null
  closing: 缺口声明
palette_default: blue-orange
palette_options:
  - blue-orange
  - purple-green
components:
  - card-finding
  - card-finding
  - kpi-card
  - gap-box
  - source-tag
```

### 读者定位段模板

```markdown
<div class="reader-profile">
  <p>本报告为 <strong>一页纸简报</strong>，面向时间有限的决策者。
  核心结论、关键发现、依据强弱和主要缺口一目了然。</p>
  <p>如需完整论证，请参阅对应的深度调研报告。</p>
</div>
```

### 章节骨架模板

```markdown
# {报告标题}

## 读者定位
{读者定位段}

## 核心结论
kpi-card × 关键指标/数据
card-finding × 1-3 条核心结论

## 关键发现
card-finding × N（每条一句话结论 + 依据强弱说明）

## 矛盾与争议
conflict-view × 未裁决矛盾（如有）

## 缺口声明
gap-box × 待补项（单源/无源结论）

## 来源
source-tag × 全部来源
```

---

## 色板定义

### blue-orange

```css
:root {
  --color-primary: #3b82f6;
  --color-primary-light: #93c5fd;
  --color-primary-dark: #1e40af;
  --color-accent: #f97316;
  --color-accent-light: #fdba74;
  --color-bg: #ffffff;
  --color-bg-soft: #f8fafc;
  --color-bg-muted: #f1f5f9;
  --color-text: #0f172a;
  --color-text-secondary: #475569;
  --color-text-muted: #94a3b8;
  --color-border: #e2e8f0;
}
```

### warm-paper

```css
:root {
  --color-primary: #92400e;
  --color-primary-light: #fde68a;
  --color-primary-dark: #78350f;
  --color-accent: #b45309;
  --color-accent-light: #fbbf24;
  --color-bg: #fefce8;
  --color-bg-soft: #fef9c3;
  --color-bg-muted: #fef08a;
  --color-text: #1c1917;
  --color-text-secondary: #57534e;
  --color-text-muted: #a8a29e;
  --color-border: #d6d3d1;
}
```

### purple-green

```css
:root {
  --color-primary: #7c3aed;
  --color-primary-light: #c4b5fd;
  --color-primary-dark: #5b21b6;
  --color-accent: #16a34a;
  --color-accent-light: #86efac;
  --color-bg: #ffffff;
  --color-bg-soft: #faf5ff;
  --color-bg-muted: #f3e8ff;
  --color-text: #1e1b4b;
  --color-text-secondary: #4c1d95;
  --color-text-muted: #a78bfa;
  --color-border: #e9d5ff;
}
```

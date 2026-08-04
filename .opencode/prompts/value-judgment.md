# 价值判断模板

> 用途：采录subagent读取文章后，判断提取档位（轻量/深度）
> 模型：弱模型（qwen3.6-27b / deepseek-v4-flash）
> 决策点：在采录subagent内部，读取文章后立即判断

## 输入

- 文章全文内容
- 策略提示（strategy_tags，来自project.config.md）

## 判断规则

| 文章类型 | extraction_level | 判断依据 |
|---|---|---|
| 概念介绍 | light | 讲"什么是X"，定义性内容为主，无深度论证 |
| 新闻资讯 | light | 时效性信息，事实陈述为主 |
| 产品介绍 | light | 官方宣传内容，无独立评测 |
| 论文解读 | deep | 有实验数据、方法论推导、性能对比 |
| 项目拆解 | deep | 有架构分析、代码级细节、设计决策 |
| 对比评测 | deep | 有多方案对比、优劣势分析、场景适用性 |
| 技术深度分析 | deep | 有原理推导、性能基准、工程实践 |
| 社区反馈 | deep | 有真实使用体验、踩坑经验、问题复现 |

## 策略提示影响

- strategy_tags含 `evidence_priority`：强制deep（即使看似light）
- strategy_tags含 `quick_scan`：倾向light（即使看似deep）
- 无策略提示：按上表判断

## 输出格式

```json
{
  "extraction_level": "light | deep",
  "value_judgment": "一句话说明判断理由",
  "article_type": "概念介绍 | 论文解读 | 项目拆解 | 对比评测 | 技术深度分析 | 社区反馈 | 新闻资讯 | 产品介绍",
  "estimated_claims": 3
}
```

estimated_claims：预估可提取的断言数量（light档2-3个概念，deep档2-8条断言）

# 叙事逻辑组合规则

核心原则：一份报告不是只用一种叙事，而是按位置组合。

## 开场段叙事

| 模式   | 结构                                     | 适用                                  |
| ---- | -------------------------------------- | ----------------------------------- |
| SCQA | Situation→Complication→Question→Answer | 通用（deep-research, technical）        |
| BAB  | Before→After→Bridge                    | 变革提案（decision-guide）                |
| PAS  | Problem→Agitate→Solution               | 紧迫性行动（action-guide, decision-guide） |

## 论证段叙事

| 模式      | 结构                                               | 适用                       |
| ------- | ------------------------------------------------ | ------------------------ |
| Toulmin | Claim→Grounds→Warrant→Backing→Qualifier→Rebuttal | 学术/技术评估（technical）       |
| CER     | Claim→Evidence→Reasoning                         | 科学/技术微观段落（deep-research） |
| 辩证法TAS  | Thesis↔Antithesis→Synthesis                      | 矛盾分析                     |

## 推进段叙事

| 模式             | 结构                                              | 适用                   |
| -------------- | ----------------------------------------------- | -------------------- |
| Data Story Arc | Setting→Hook→Rising→Aha→Options                 | 数据密集型（deep-research） |
| Story Spine    | Once→Every day→Until→Because→Finally→Ever since | 案例叙述                 |
| Fichtean曲线     | 连续危机→高潮→回落                                      | 层层追问式                |

## 结论段叙事

| 模式   | 结构                               | 适用                  |
| ---- | -------------------------------- | ------------------- |
| AIDA | Attention→Interest→Desire→Action | 说服型（action-guide）   |
| 结论先行 | 结论→支撑→风险                         | 决策型（decision-guide） |

## 组合示例

| 报告类型           | 开场   | 论证      | 推进             | 结论   |
| -------------- | ---- | ------- | -------------- | ---- |
| deep-research  | SCQA | CER     | Data Story Arc | AIDA |
| decision-guide | PAS  | —       | —              | 结论先行 |
| action-guide   | PAS  | CER     | —              | AIDA |
| technical      | SCQA | Toulmin | —              | 结论先行 |

## 解释型叙事

适用于 `overview-md`、`explanatory-overview` 和技术概貌类报告。

内部组织方法：

```text
读者基准 → 场景/问题/需求 → 调研对象的解决之道 → 运转过程 → 效果/价值 → 代价/问题 → 后续追问
```

注意：这是写作推理骨架，不是最终报告的小标题模板。最终报告应保持自然叙事，不要每节机械写“读者已知/场景/解决之道/效果价值”。其中“读者已知”只应在报告开头的读者基准中总体说明；场景、问题、解决之道、效果价值可以自然出现。

## 写作约束

- 概念三步走：为什么需要→是什么→怎么工作
- 每个技术名词首次出现时必须解释，不让术语裸奔
- 章节标题=结论或明确问题（不说"XX分析"）
- 段落之间有过渡句
- 读者定位段：假设读者知道X、不知道Y、关心Z
- 所有报告默认不暴露内部编号和内部置信度标记

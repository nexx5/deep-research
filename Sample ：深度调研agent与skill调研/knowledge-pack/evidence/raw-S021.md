---
source_id: S021
source_url: https://cognition.ai/blog/dont-build-multi-agents
title: "Don't Build Multi-Agents (Cognition 博客) + Into the Unknown Unknowns (Co-STORM, arXiv:2408.15232)"
author: "Walden Yan (Cognition) / Yucheng Jiang, Yijia Shao, Dekun Ma, Sina J. Semnani, Monica S. Lam (Stanford/Yale)"
date: 2025-06-12 (博客) / 2024-08-27 (论文)
fetched_at: 2026-08-04T09:15:00
content_type: web_page + paper
note: "两源合并存档：源A=Cognition官方博客（观点主张）；源B=Co-STORM论文 arXiv:2408.15232v2（EMNLP 2024 Main，学术声称）。访问日期2026-08-04。"
---

# 源A：Cognition《Don't Build Multi-Agents》

- URL: https://cognition.ai/blog/dont-build-multi-agents
- 作者：Walden Yan（Cognition）
- 日期：06.12.25（2025年6月12日）

## Principles of Context Engineering

We'll work our way up to the following principles:

1.  Share context
2.  Actions carry implicit decisions

**Why think about principles?**

HTML was introduced in 1993. In 2013, Facebook released React to the world. It is now 2025 and React (and its descendants) dominates the way developers build sites and apps. Why? Because React is not just a scaffold for writing code. It is a philosophy. By using React, you embrace building applications with a pattern of reactivity and modularity, which people now accept to be a standard requirement, but this was not always obvious to early web developers.

In the age of LLMs and building AI Agents, it feels like we're still playing with raw HTML & CSS and figuring out how to fit these together to make a good experience. No single approach to building agents has become the standard yet, besides some of the absolute basics.

> In some cases, libraries such as [https://github.com/openai/swarm](https://github.com/openai/swarm) by OpenAI and [https://github.com/microsoft/autogen](https://github.com/microsoft/autogen) by Microsoft actively push concepts which I believe to be the wrong way of building agents. Namely, using multi-agent architectures, and I'll explain why.

That said, if you're new to agent-building, there are lots of resources on how to set up the basic scaffolding [1](https://www.anthropic.com/engineering/building-effective-agents) [2](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf). But when it comes to building serious production applications, it's a different story.

## A Theory of Building Long-running Agents

Let's start with reliability. When agents have to actually be reliable while running for long periods of time and maintain coherent conversations, there are certain things you must do to contain the potential for compounding errors. Otherwise, if you're not careful, things fall apart quickly. At the core of reliability is Context Engineering.

*Context Engineering*

In 2025, the models out there are extremely intelligent. But even the smartest human won't be able to do their job effectively without the context of what they're being asked to do. "Prompt engineering" was coined as a term for the effort needing to write your task in the ideal format for a LLM chatbot. "Context engineering" is the next level of this. It is about doing this automatically in a dynamic system. It takes more nuance and is effectively the #1 job of engineers building AI agents.

Take an example of a common type of agent. This agent

1. breaks its work down into multiple parts
2. starts subagents to work on those parts
3. combines those results in the end

This is a tempting architecture, especially if you work in a domain of tasks with several parallel components to it. However, it is very fragile. The key failure point is this:

> Suppose your **Task** is "build a Flappy Bird clone". This gets divided into **Subtask 1** "build a moving game background with green pipes and hit boxes" and **Subtask 2** "build a bird that you can move up and down".
>
> It turns out subagent 1 actually mistook your subtask and started building a background that looks like Super Mario Bros. Subagent 2 built you a bird, but it doesn't look like a game asset and it moves nothing like the one in Flappy Bird. Now the final agent is left with the undesirable task of combining these two miscommunications.

This may seem contrived, but most real-world tasks have many layers of nuance that all have the potential to be miscommunicated. You might think that a simple solution would be to just copy over the original task as context to the subagents as well. That way, they don't misunderstand their subtask. But remember that in a real production system, the conversation is most likely multi-turn, the agent probably had to make some tool calls to decide how to break down the task, and any number of details could have consequences on the interpretation of the task.

> *Principle 1*
> Share context, and share full agent traces, not just individual messages

Let's take another revision at our agent, this time making sure each agent has the context of the previous agents.

Unfortunately, we aren't quite out of the woods. When you give your agent the same Flappy Bird cloning task, this time, you might end up with a bird and background with completely different visual styles. Subagent 1 and subagent 2 cannot not see what the other was doing and so their work ends up being inconsistent with each other.

The actions subagent 1 took and the actions subagent 2 took were based on conflicting assumptions not prescribed upfront.

> *Principle 2*
> Actions carry implicit decisions, and conflicting decisions carry bad results

I would argue that Principles 1 & 2 are so critical, and so rarely worth violating, that you should by default rule out any agent architectures that don't abide by them. You might think this is constraining, but there is actually a wide space of different architectures you could still explore for your agent.

The simplest way to follow the principles is to just use a single-threaded linear agent:

Here, the context is continuous. However, you might run into issues for very large tasks with so many subparts that context windows start to overflow.

To be honest, the simple architecture will get you very far, but for those who have truly long-duration tasks, and are willing to put in the effort, you can do even better. There are several ways you could solve this, but today I will present just one:

In this world, we introduce a new LLM model whose key purpose is to compress a history of actions & conversation into key details, events, and decisions. This is *hard to get right.* It takes investment into figuring out what ends up being the key information and creating a system that is good at this. Depending on the domain, you might even consider fine-tuning a smaller model (this is in fact something we've done at Cognition).

The benefit you get is an agent that is effective at longer contexts. You will still eventually hit a limit though. For the avid reader, I encourage you to think of better ways to manage arbitrarily long contexts. It ends up being quite a deep rabbit hole!

## Applying the Principles

If you're an agent-builder, ensure your agent's every action is informed by the context of all relevant decisions made by other parts of the system. Ideally, every action would just see everything else. Unfortunately, this is not always possible due to limited context windows and practical tradeoffs, and you may need to decide what level of complexity you are willing to take on for the level of reliability you aim for.

As you think about architecting your agents to avoid conflicting decision-making, here are some real-world examples to ponder:

*Claude Code Subagents*
As of June 2025, Claude Code is an example of an agent that spawns subtasks. However, it never does work in parallel with the subtask agent, and the subtask agent is usually only tasked with answering a question, not writing any code. Why? The subtask agent lacks context from the main agent that would otherwise be needed to do anything beyond answering a well-defined question. And if they were to run multiple parallel subagents, they might give conflicting responses, resulting in the reliability issues we saw with our earlier examples of agents. The benefit of having a subagent in this case is that all the subagent's investigative work does not need to remain in the history of the main agent, allowing for longer traces before running out of context. The designers of Claude Code took a purposefully simple approach.

*Edit Apply Models*
In 2024, many models were really bad at editing code. A common practice among coding agents, IDEs, app builders, etc. (including Devin) was to use an "edit apply model." The key idea was that it was actually more reliable to get a small model to rewrite your entire file, given a markdown explanation of the changes you wanted, than to get a large model to output a properly formatted diff. So, builders had the large models output markdown explanations of code edits and then fed these markdown explanations to small models to actually rewrite the files. However, these systems would still be very faulty. Often times, for example, the small model would misinterpret the instructions of the large model and make an incorrect edit due to the most slight ambiguities in the instructions. Today, the edit decision-making and applying are more often done by a single model in one action.

**Multi-Agents**

If we really want to get parallelism out of our system, you might think to let the decision makers "talk" to each other and work things out.

This is what us humans do when we disagree (in an ideal world). If Engineer A's code causes a merge conflict with Engineer B, the correct protocol is to talk out the differences and reach a consensus. However, agents today are not quite able to engage in this style of long-context proactive discourse with much more reliability than you would get with a single agent. Humans are quite efficient at communicating our most important knowledge to one another, but this efficiency takes nontrivial intelligence.

Since not long after the launch of ChatGPT, people have been exploring the idea of multiple agents interacting with one another to achieve goals [3](https://arxiv.org/abs/2304.03442)[4](https://github.com/FoundationAgents/MetaGPT). While I'm optimistic about the long-term possibilities of agents collaborating with one another, it is evident that in 2025, running multiple agents in collaboration only results in fragile systems. The decision-making ends up being too dispersed and context isn't able to be shared thoroughly enough between the agents. At the moment, I don't see anyone putting a dedicated effort to solving this difficult cross-agent context-passing problem. I personally think it will come for free as we make our single-threaded agents even better at communicating with humans. When this day comes, it will unlock much greater amounts of parallelism and efficiency.

**Toward a More General Theory**

These observations on context engineering are just the start to what we might someday consider the standard principles of building agents. And there are many more challenges and techniques not discussed here. At Cognition, agent building is a key frontier we think about. We build our internal tools and frameworks around these principles we repeatedly find ourselves relearning as a way to enforce these ideas. But our theories are likely not perfect, and we expect things to change as the field advances, so some flexibility and humility is required as well.

We welcome you to try our work at [app.devin.ai](http://app.devin.ai). And if you would enjoy discovering some of these agent-building principles with us, reach out to [walden@cognition.ai](mailto:walden@cognition.ai)

---

# 源B：Co-STORM 论文《Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations》

- arXiv: https://arxiv.org/abs/2408.15232（v2，2024-10-17）
- PDF: https://arxiv.org/pdf/2408.15232v2
- 作者：Yucheng Jiang*, Yijia Shao*（*共同一作，Stanford University）、Dekun Ma（Yale University）、Sina J. Semnani、Monica S. Lam（Stanford University）
- 发表：arXiv 2024-08-27；EMNLP 2024 Main
- 分类：cs.CL / cs.AI / cs.IR
- 开源资源：https://github.com/stanford-oval/storm；在线预览：https://storm.genie.stanford.edu
- 引用数（OpenAlex 2026-08-04 快照）：1

## 摘要（Abstract 原文）

While language model (LM)-powered chatbots and generative search engines excel at answering concrete queries, discovering information in the terrain of unknown unknowns remains challenging for users. To emulate the common educational scenario where children/students learn by listening to and participating in conversations with their parents/teachers, we create Collaborative STORM (Co-STORM). Unlike QA systems that require users to ask all the questions, Co-STORM lets users observe and occasionally steer the discourse among several LM agents. The agents ask questions on the user's behalf, allowing the user to discover unknown unknowns serendipitously. To facilitate user interaction, Co-STORM assists users in tracking the discourse by organizing the uncovered information into a dynamic mind map, ultimately generating a comprehensive report as takeaways. For automatic evaluation, we construct the WildSeek dataset by collecting real information-seeking records with user goals. Co-STORM outperforms baseline methods on both discourse trace and report quality. In a further human evaluation, 70% of participants prefer Co-STORM over a search engine, and 78% favor it over a RAG (Retrieval Augmented Generation) chatbot.

## 引言关键内容（Introduction 摘录）

- 现有聊天机器人与生成式搜索引擎"effectively addressing known unknowns, where users are aware of their information needs"，但复杂信息寻求（学术研究、市场分析、决策制定）中系统应让用户暴露于 unknown unknowns。
- 前序自动写作系统 STORM（Shao et al., 2024）"demonstrates that LMs paired with search engines can automatically generate a high-quality draft of Wikipedia-like articles on arbitrary topics"，但"producing the static report as the final outcome, STORM does not support any user interaction which is crucial in complex information seeking"。
- 传统搜索引擎和 RAG 聊天机器人被动响应用户查询，"often inducing echo chamber effects or high cognition load as users with limited prior knowledge may even struggle to formulate questions"。
- 贡献三条：①提出 Co-STORM（协作话语模拟+人类交互+信息组织）；②构建 WildSeek 数据集；③自动+人工评估显示 Co-STORM 帮助人类发现 unknown unknowns 且"requires less mental effort"。

## 方法（§3 Method）关键内容

### 3.1 Collaborative Discourse Protocol

- 协作话语 D = {u1, ..., un} 由三种角色的 turn-based 文本话语组成：user（§3.3）、具有不同视角的专家 experts with diverse perspectives（§3.4）、引导话语并注入问题的主持人 a moderator guiding the discourse and injecting questions（§3.5）。
- 话语以 N 个专家每人一轮"热身"开始。
- Utterance Intent：每个 agent 话语带意图类型——ORIGINAL QUESTION（发起新问题）、INFORMATION REQUEST（从先前话语寻求更多信息）、POTENTIAL ANSWER（对先前问题的可能回答）、FURTHER DETAILS（对先前回答的补充信息）。
- Initiative Management：Co-STORM 采用混合主动性（mixed-initiative）——用户主动参与时系统基于用户问题/论点继续话语；否则系统自动生成下一轮。用户可随时接管话语。

### 3.2 Tracking the Discourse with a Mind Map

- "To help users track the discourse and reduce their cognition load, Co-STORM uses a tree-structured mind map M to dynamically organize collected information"。
- M = (C, E)：概念 C 的层级组织，有向边 E 表示主题间父子关系；每个概念关联检索信息子集 Ic。
- 通过两个操作动态更新：insert（把信息放到最合适概念下）与 reorganize（概念下信息超过 K 条时触发，生成新子主题名并重新插入）；采用自底向上清理（删除无支撑概念、折叠单子主题概念）。

### 3.3 User Participation / 3.4 Simulating the Roundtable Participant / 3.5 Simulating the Moderator

- 用户注入话语 u 后，Co-STORM 用 u 作为查询检索信息，提示 LM 更新专家列表 P'。
- 模拟专家（perspective-guided）：沿用 STORM 的 perspective-guided question asking，为不同视角个性化模拟专家；专家依次按流程生成话语：①基于话语历史和专家视角选择意图 ai；②若意图是 POTENTIAL ANSWER 或 FURTHER DETAILS，生成搜索查询、检索信息、生成带引用的回答；否则直接基于历史生成问题；③用 LM 润色话语使其更聊天化、更吸引人。
- 模拟主持人：若所有参与者都是专家，话语倾向全是 FURTHER DETAILS（重复与狭窄讨论）。主持人基于"自上轮主持人发言后检索到的未引用来源"生成有依据的新问题；对每条信息按 cos(i, t)^α · (1−cos(i, q))^(1−α) 重排（优先与主题相关但不直接回答原问题的信息），α 为超参数。

## 实现（§4 Co-STORM Implementation）

- LM 组件：DSPy 框架 + gpt-4o-2024-05-13（zero-shot prompting）。
- 检索接地：You.com search API（系统兼容其他搜索引擎/IR 系统）。
- 超参数：N（专家数）=3，K（reorganize 阈值）=10，L（主持人介入阈值）=2，α=0.5；embedding 用 text-embedding-3-small；LM temperature 1.0、top_p 0.9。

## 自动评估（§5 Automatic Evaluation）

### 评估设置

- 数据集：WildSeek（真实用户 topic + goal 对，100 数据点、24 个领域；从开源 STORM 网站收集，规则过滤 + gpt-4o 二分类 + 人工审查 + 下采样）。
- 基线：(1) RAG Chatbot（一问一答范式）；(2) STORM + QA（用 STORM 生成报告后允许用户追问）。
- 模拟用户：gpt-4o-2024-05-13（给定 t, g, 话语历史）；所有方法在 30 次搜索查询后终止。
- 报告评估器：Prometheus 2（7B 评估 LM），5 点 rubric：Relevance、Breadth、Depth、Novelty；另报告 Information Diversity（信息对间平均不相似度）。
- 话语评估：5 点 rubric 逐轮打分；提问类（Novelty、Intent Alignment、No Repetition），回答类（Consistency、Engagement）；报告每轮唯一引用 URL 数。

### 自动评估结果（Table 3，均值；†=与两基线配对t检验 p<0.05）

| 指标 | RAG Chatbot | STORM+QA | Co-STORM | w/o Multi-Expert | w/o Moderator |
|---|---|---|---|---|---|
| Report Relevance | 3.57 | 3.61 | 3.78 | 3.73 | 3.56 |
| Breadth | 3.50 | 3.61 | 3.79 | 3.75 | 3.69 |
| Depth | 3.26 | 3.43 | 3.77† | 3.77 | 3.41 |
| Novelty | 2.44 | 2.50 | 3.05† | 2.93 | 2.89 |
| Info Diversity | 0.595 | 0.592 | 0.602 | 0.589 | 0.577 |
| QA Consistency | 4.37 | 4.34 | 4.40† | 4.40 | 4.39 |
| QA Engagement | 4.13 | 4.11 | 4.33† | 4.32 | 4.28 |
| # Unique URLs | 2.94 | 2.89 | 6.04† | 5.91 | 5.67 |

### Ablation 研究（§5.4）

- 对比 (1) w/o Multi-Expert（1 专家+1 主持人）、(2) w/o Moderator（N 专家+0 主持人）：两消融在所有指标上均差于完整系统；"removing the moderator has a greater negative impact than reducing the number of experts"。
- 单专家+单主持人已提供大部分收益；主持人角色基于未使用信息提问，"represents somebody with a much larger known unknowns, effectively steering the discourse to help users discover more in the space of their unknown unknowns"。

## 人工评估（§6 Human Evaluation）

### 设置

- IRB 批准；招募 20 名志愿者，随机分两组：一组对比 Google Search，另一组对比 RAG Chatbot；每个用户在两个系统上各完成同一领域同一目标的主题（用不同主题缓解主题熟悉度偏差）；5 个领域各 2 人/组；交叉平衡起始系统。
- 评分：4 个维度（Relevance、Breadth、Depth、Novelty/Serendipity），5 点 Likert；完成后提供成对偏好（努力程度、参与度、回音室问题、整体体验）。

### 结果（Table 4）

- Co-STORM vs Search Engine（n=10）：Serendipity 2.70 vs 3.90，Win 70% (Lose 10%)，p=0.030；Breadth Win 50%、Depth Win 60%。
- Co-STORM vs RAG Chatbot（n=9，1 人未留使用记录被剔除）：Breadth Win 67% (p=0.013)、Serendipity Win 67% (p=0.009)；Overall Experience 78% 偏好 Co-STORM。
- 摘要声明：70% 偏好 Co-STORM 胜过搜索引擎，78% 胜过 RAG 聊天机器人。
- 成对偏好（Fig 4 数据）：Less Effort——vs Search Engine 67% 同意、vs RAG 44% 同意；User Engagement——80% / 100%；Addresses Echo Chamber——60% / 56%；Overall Experience——70% / 78%。
- 参与者反馈：mind map 的 80 个快照被评估，"accurately tracked the discourse 71% of the time"；一位参与者评论"Co-STORM is so much less mentally taxing for me to use"。
- 负面反馈：19 名参与者中 4 人指出 RAG Chatbot 对目标明确指令遵循更好，期望 Co-STORM 输出更简洁话语。

## 结论与局限（§8 Conclusion / Limitations）

- 结论："Co-STORM outperforms traditional search engines and RAG chatbots in surfacing unknown unknowns for human learning and reducing users' mental effort"。
- 局限自述：①未针对用户先验知识定制话语；②用户有时想要更多话语控制（管理专家视角、定制话语长度）；③不支持多语言；④相比 RAG Chatbot，Co-STORM 延迟更高（需决定话语意图和更新 mind map）。

## 相关工作（§7 Related Works 摘录）

- 信息寻求支持：多数 NLP 研究聚焦 QA 系统，假设答案在单文档或用户能构造复杂查询——在复杂信息寻求中不成立；长文 QA 与自动写作系统通常忽略人类交互或仅被动回答问题；"We construct a multi-agent system with a human-in-the-loop protocol to support effective user interaction"。
- 多 agent 系统：多 agent 辩论提升事实性与推理（Du et al., 2023；Liang et al., 2023）；协作角色扮演提升编码/数学基准表现（Li et al., 2023；Hong et al., 2023）；Generative Agents（Park et al., 2023）用 25 个 LM agent 研究涌现社会行为；Michael et al. (2023) 显示多 agent 辩论帮助人类监督模型输出。
- 协作话语学习：Nussbaum (2008) 强调批判性讨论中参与者持不同观点的重要性；facilitator 角色（提问与提供补充信息）是流行策略（Onrubia et al., 2022）。

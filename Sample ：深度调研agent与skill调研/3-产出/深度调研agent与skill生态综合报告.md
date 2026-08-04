# 深度调研服务生态综合报告：从"搜索的终点"到"调研的起点"

> **读者定位**：本文假设读者了解大模型与 Agent 的基本概念、熟悉 ChatGPT / Perplexity 等主流 AI 产品；不一定了解深度调研服务的内部架构差异、评测基准的量纲问题与"官方声称 vs 独立验证"的证据落差。本文关心的是：这个生态的整体格局是什么、开源与付费两大阵营各自走到了哪里、方法流派在争什么、我们看到的数字哪些可信。
>
> **诚实边界声明**：本报告基于一次完整的生态调研组装而成（38 个来源采录、5 份跨源对比、914 条知识包断言），已通过结构一致性检查（证据链完整、知识包一致、冲突已仲裁）；但结构检查不保证事实准确性——事实准确性由来源可信度与多源交叉验证共同保障。报告不宣称"已通过质量验证"，只如实说明证据的层级与缺口。文中引用的 Gemini 结构化输出能力，官方资料口径存在不一致（详见正文），引用时已标注。

---

## 一、生态全景：一场关于"调研"的集体爆发

如果只用一个词描述 2025-2026 年的 AI 产品生态，那就是"深度调研"（Deep Research）——把人类分析师"读几十篇资料、交叉验证、写一份带引用的长报告"的过程，压缩进一个自主运行的 Agent。这个物种的公共能力基线已经相当清晰：**多源检索 + 长报告生成 + 证据引用**，几乎每个自称深度调研的产品都声称具备这三项能力（开源方案有源码与文档佐证，付费方案则是官方声称）。

但"是什么"只是故事的开始。真正值得观察的是**它为什么在 2024 年底到 2026 年如此密集地爆发**。把时间轴拉长，可以看到一条清晰的接力线：

- 2024 年 10 月：Anthropic 发布 computer use，浏览器代理流派起步
- 2024 年 12 月：Google 发布 Project Mariner
- 2025 年 1 月：OpenAI 发布 Operator
- 2025 年 2 月：ChatGPT Deep Research 发布，"深度调研"概念引爆
- 2025 年全年：Perplexity、Gemini、Genspark、Manus、hyperresearch、OpenManus 等密集跟进
- 2025 年 12 月：Meta 宣布以约 20 亿美元收购 Manus
- 2026 年：DRB II、DRACO、DeepResearchEval 等评测基准集中出现；Kimi、Claude、Grok、Parallel 等新形态分化

这条时间线说明，深度调研不是单一公司的发明，而是"长上下文模型 + 工具调用 + 强化学习"三股技术力量汇合后的必然产物：ChatGPT Deep Research 官方明示其基于端到端强化学习训练（在浏览器与 Python 工具的真实任务上训练），Gemini 则强调 1M 上下文窗口与 RAG 的结合。技术底座成熟之后，产品形态迅速分化成两大阵营。

**开源阵营**以"可复核"为最大公约数：源码公开、许可证宽松（MIT / Apache-2.0）、自托管、自带 API Key 运行；能力主张可以被任何人验证，但成本与复杂度要自己承担。**付费阵营**以"开箱即用"为卖点：订阅制或积分制、托管运行、黑盒能力；官方声称为主，能力细节大多不公开。两阵营并非平行线——Manus 发布后三天，社区就火速推出了 OpenManus 开源复刻，构成"闭源商业 SaaS vs 社区开源"的直接对冲样本。

---

## 二、开源阵营：四条路线与一套张力

开源阵营内部并非铁板一块，而是存在至少四条方法论路线，它们的差异本身就是生态最有价值的信息。

### 单 agent 极简派：dzhng/deep-research

这条路线主张"最简单即可用"。其目标是提供最简的 deep research agent 实现（代码量目标小于 500 行，官方自述），架构是单一 agent 递归循环：用 depth / breadth 参数控制迭代检索的深度与广度，递归深化后输出带 Sources 引用的 Markdown 报告。没有编排器、没有子代理、没有记忆库，依赖 Firecrawl 单一第三方服务完成搜索抓取。它的方法论主张很鲜明：**单 agent 连续深化足够，简单、可控、成本低**。这是"深度 vs 广度/分工"方法论光谱上最纯粹的一端。

### 多 agent 编排派：OpenDeepResearch

另一端是 LangGraph 图编排的多 agent 方案。其工作流是清晰的三阶段：**Scope（澄清 + 简报）→ Research（supervisor 拆解子主题 → 子 agent 并行检索 → 压缩 findings）→ Write（one-shot 报告）**。这里有一个非常值得注意的"第一手教训"：官方主张研究阶段多 agent 并行有效（隔离上下文、防止膨胀），但写作阶段必须退回单 agent——因为并行写报告会导致章节不连贯。它还通过上下文工程控制 token 膨胀（研究简报压缩对话、子 agent 压缩 findings 后回传 supervisor）。多 agent 不是万能的，它只在一半流程中成立，这是工程实践给出的朴素答案。

### 论文驱动派：STORM / Co-STORM

斯坦福的 STORM 是"论文驱动"路线的代表——方法名就是论文名。它把自动化聚焦在 pre-writing 阶段：视角发现 → 模拟多轮对话 → 信息策展 → 大纲 → 生成带引用全文。技术底座上，STORM 与 Co-STORM 都基于 dspy 高度模块化实现（官方 README 明示，dspy 论文清单也收录了 STORM 论文，三方互证）。Co-STORM 更进一步走向人机协作：用户观察并偶尔引导多个 LM agent 的对话（用户 / 多视角专家 / 主持人三方话语协议），用动态 mind map 追踪话语、降低认知负荷——论文实验声称 70% 用户偏好超过搜索引擎、78% 超过 RAG 聊天机器人（单源自报，人工评估样本 n≈10）。

### 工程驱动商业级：GPT Researcher

作为生态里较早的开源方案，它采用 planner / execution / publisher 三阶段，树状递归探索，官方声称单次成本约 0.4 美元、约 5 分钟完成（特定配置下，未含检索与图片费用）。它最特殊的一点是分发方式：除自托管外，还提供 Claude Skill 分发（`npx skills add`），成为"开源项目 skill 化"的早期样本。

### 通用底座与框架内置

开源生态里还有一批"非专用"参与者：OpenManus（社区开源复刻，MIT，约 5.8 万 stars）以单 agent 循环为主、多 agent 版本自述不稳定；LangChain 提供官方 deep research 构建指南与 deepagents harness，走"官方教程 + harness 能力"路线，而 LlamaIndex 则没有专用深度调研页，走"框架原语 + 自建"路线；CAMEL、MetaGPT、OpenAI Swarm、Microsoft AutoGen 等通用多 agent 框架中，Swarm 已被官方 Agents SDK 取代（29 个 commit 的实验项目）、AutoGen 进入维护模式（由 Microsoft Agent Framework 接替）。框架层快速迭代，与深度调研专用方案处在不同抽象层。

### 开源阵营的共性观察

把四条路线放在一起，三个客观结论浮出水面：其一，**能力可复核**——开源方案的能力主张几乎都能落到源码或官方文档上，这是付费阵营不具备的；其二，**成本披露两极分化**——工程驱动方案给出估算（GPT Researcher 约 0.4 美元/次、OpenDeepResearch 约 46-187 美元/百任务、hyperresearch 约 60-120 美元/查询），论文驱动方案（STORM）则基本不公开成本；其三，**知识复用是普遍缺口**——大多数开源方案没有长期记忆，仅 hyperresearch 提供跨会话的 SQLite vault。

---

## 三、付费阵营：能力、定价与开放度

付费阵营以订阅与积分制为共同特征，但在能力、定价透明度、开放度上差异显著。

| 方案 | 能力要点 | 定价（官方） | 开放度 |
|---|---|---|---|
| ChatGPT Deep Research | agentic 多步研究、数百来源综合、研究分析师级报告、官方承认幻觉与置信度校准弱点 | 订阅配额（Pro 250 次/月，Plus 等 25 次/月，Free 5 次/月），美元价格未披露 | 封闭产品（仅 ChatGPT 内），2026-02 起可连 MCP |
| Perplexity Deep Research | 迭代式研究（搜索 + 编码 + 计划细化），多数任务 <3 分钟，官方称"数百来源" | 免费增值，具体数字未披露 | 托管闭源 |
| Gemini Deep Research | 1M 上下文 RAG、Plan→Search→Read→Iterate→Output 三步工作流、双档（DR / DR Max） | 成本透明：DR 约 1-3 美元/任务、DR Max 约 3-7 美元/任务；订阅 + API 双轨 | API 开放度高（Interactions API / MCP / File Search） |
| Genspark | 多模型聚合（Claude/GPT/Gemini/Grok/DeepSeek 等 8 家） | Team 30 美元/席/月 + 12000 积分/席/月 | 闭源 SaaS，登录墙 |
| Manus | 通用 agent，Wide Research 并行多代理（主代理分配、子代理间不通信） | 积分制：免费 300 积分/日，Pro 20 美元/月 4000 积分起，40 美元/月 8000 积分起 | 开放 API，云端异步 VM 执行 |
| Operator | 浏览器代理（CUA），解读屏幕、点击、输入，官方 OSWorld 38.1% | 订阅制（官方未披露独立定价细节） | 无专用 API，通用界面哲学 |

这个表格背后有几个叙事线索值得展开。

**ChatGPT Deep Research** 是引爆者，也是官方自我批评最坦诚的一个：发布页明确承认可能幻觉事实、错误推断、难以分辨权威信息与谣言、置信度校准弱。它的能力更新节奏（2025-07 视觉浏览器、2026-02 MCP 连接）说明产品仍在快速进化。但它的定价是最不透明的——发布页只给用量配额，美元价格从未披露（定价页 JS 渲染抓取失败，这是生态内"定价公开度下降"的一个样本）。

**Perplexity Deep Research** 的口碑关键词是"快而浅"。官方声称"读取数百来源、多数任务 3 分钟内完成"，社区却普遍反馈"15 个来源太浅"、"升级后反而变差"。这个矛盾值得玩味：官方迭代机制 vs 社区感知的来源数量，是两个不同层面的讨论——但"官方声称深度"与"社区感知浅"的落差是真实存在的。

**Gemini Deep Research** 在付费阵营里是开放度与透明度的异类：唯一给出任务级成本估算（1-7 美元/任务）、唯一开放 API 的旗舰产品。但它的官方资料存在**内部口径不一致**：发布文声称支持 JSON schema 结构化输出，API 文档却在局限清单里明确写"目前不支持结构化输出"——同一家公司的两份官方资料互相矛盾，引用其结构化输出能力时必须标注这一口径冲突。

**Manus** 是通用 agent 的代表，也贡献了生态里最戏剧性的稳定性事件：2025 年 12 月 Meta 宣布以约 20 亿美元收购；2026 年 4 月中国发改委以技术出口管制、外商投资规则与国家安全为由命令撤销收购；2026 年 6 月 Meta 开始执行运营拆分、停止数据共享——而截至采录日（2026-08-04）官网仍标注 Meta 归属，状态并存。此外，Manus 还有积分消耗争议（社区反馈单任务平均消耗约 1500 积分，免费档每日 300 积分难以支撑复杂任务）与"套壳"争议（底层模型来自外部，社区信息）。

**Operator** 代表了"执行侧"路线：CUA（Computer-Using Agent）模型解读屏幕、像人一样操作 GUI。它与深度调研的关系是官方规划中的"异步调研 + 现实执行"组合——付费侧正在出现"调研-执行一体"的趋势（Perplexity 也已把 Deep Research 并入 Computer 宿主）。

**Kimi / Claude / Grok / Parallel 等新形态**则展示付费生态的进一步分化：Kimi Deep Research 是消费者应用内功能（免费层 + token 计费，三阶段工作流：澄清意图→自主执行→多格式产出）；Claude Research 仅限付费订阅；Grok DeepSearch 面向 X Premium+ 用户，同时提供独立的 Web Search API 工具（xAI 文档用 web_search 命名而非 DeepSearch）；Parallel 则直接走"面向 agent 的 API 基础设施"路线（请求计费 + 自研索引）。同一枚"深度调研"标签下，产品形态从消费者功能到开发者基础设施一应俱全。

---

## 四、方法流派：一场关于"该用几个 agent"的争论

如果把生态比作一个学派林立的学术圈，最大的争论就是**多 agent 到底该不该用**。综合跨源对比梳理出的"方法流派三角"把立场分为四派：

**单 agent 递归深化派**（dzhng/deep-research）主张简单、可控、低成本，一个 agent 连续深化足够。**多 agent 编排派**（OpenDeepResearch、GPT Researcher 多 agent 变体）主张研究阶段多 agent 并行有效，用隔离上下文解决上下文膨胀。**反多 agent 派**（Cognition 官方博客《Don't Build Multi-Agents》）则给出最尖锐的批评：多 agent 架构"脆弱"——决策分散、上下文无法充分共享；提出上下文工程两原则（共享完整 agent 轨迹、行动携带隐含决策），主张单线程线性 agent 加上下文压缩模型；点名批评 OpenAI Swarm 与 Microsoft AutoGen。**人机协作派**（Co-STORM）则把用户拉回流程中央：用户不是提问者而是旁听者，观察并偶尔引导多个专家 agent 的对话。

这四派并非纯粹对立，存在一个有意思的"边界共识"：**即使是最坚定的多 agent 支持者（OpenDeepResearch），也承认写作阶段必须单 agent**；而最激烈的反多 agent 者（Cognition）也不排斥 subagent——它只是反对并行协作。争论的真正焦点是"并行协作是否值得"：多 agent 支持者认为研究阶段的上下文隔离是优点，反对者认为决策分散是致命伤。另外，Anthropic《Building Effective Agents》把 orchestrator-workers（多 worker 委派）列为合法模式，与 Cognition 的默认排除形成张力；但 Anthropic 同时反对复杂框架抽象层、建议直连 API，与 dspy 主张编译器引入抽象又构成另一条方法论分界线。这些立场目前都没有被实验一锤定音——Cognition 的博客是无实验支撑的观点主张，Co-STORM 的实验是单源自报。

---

## 五、评测基准家族：同名不同源，量纲割裂

深度调研能力的评测是这个生态最混乱也最关键的角落。混乱的根源是：**没有人真正定义过"什么算深度调研能力"**——是报告质量？引用准确率？事实核查？还是答案正确性？不同基准给出了不同答案，于是出现了基准家族内部的"量纲割裂"。

最典型的陷阱是**同名不同源**：存在两个都叫 DRB（Deep Research Bench）的基准——中国科学技术大学团队的 USTC DRB（100 任务 / 22 领域，RACE 报告质量四维 + FACT 引用准确率，arXiv:2506.11763）与 FutureSearch 的 DRB（89 任务 / 8 类，冻结网页环境的答案 + 轨迹评估，arXiv:2506.06287）。两者任务集、评估方式完全不同，分数不可互比，但常被混用。后续基准继续膨胀：DRB II（132 任务 / 9430 条细粒度 rubric，独立量纲）、LiveResearchBench（动态任务抗污染）、GAIA（真实世界问题，付费官方声称 SOTA 的常用参照物）、DeepResearchEval（persona 驱动任务生成 + 动态维度评估 + 主动事实核查，独立于 DRB 家族）。

这里还有一个必须警惕的类别：**官方附属基准**。Perplexity 与哈佛合作的 DRACO（100 任务 / 10 领域，arXiv:2602.11685）是官方基准——Perplexity Deep Research 在其中自称全领域全轴最高分（约 70.5%），但 judge 虽为第三方模型，基准本身存在利益相关；而第三方 AIMultiple 的 DR-50 评测中 Perplexity 得分约 34%。同是 Perplexity，官方基准 70.5% vs 第三方 34%，差异巨大——这不是矛盾，而是指标、任务集、规模完全不同，只能分别引用、不可互相换算。hyperresearch 的官方附属 harness（自称"领先"DRB 榜单）也是同类样本：官方措辞 "benchmarked internally"（内部基准），并自认"第三方验证待定"。

**独立第三方评测补充的是另一类证据**：USTC DRB 上 Gemini RACE 48.88（DRA 组最高）、OpenAI 46.98、Perplexity 42.25；引用准确率 Perplexity 90.24% 最高、OpenAI 77.96% 最低。而官方自报的 HLE / GAIA / SimpleQA 分数（ChatGPT HLE 26.6%、Perplexity HLE 21.1% / SimpleQA 93.9%、Gemini HLE 46.4%）测的是知识问答类能力，与第三方自建的报告质量 / 引用指标维度不同——**未发现任何第三方对官方自报分数做同基准独立复测**，这是整个生态最普遍的证据缺口。

---

## 六、关键证据对照：官方声称、独立验证与社区口碑

把官方声称、独立验证、社区口碑三方证据并置，是本次调研最有价值的产出。三个对照结论如下。

**其一，引用可靠性是付费侧最大的争议点。** 官方普遍声称"详细引用、减少幻觉"（Gemini 甚至说专门训练减少幻觉），但学术审计给出了相反的量化证据：商业 LLM 与 deep research agent 的引用 URL 存在 **3-13% 的幻觉率**（基于 DRBench 53,090 条 URL 与 ExpertQA 168,021 条 URL 的测量），整体 5-18% 的引用无法解析，且 deep research agents 生成的引用数显著多于搜索增强 LLM、幻觉 URL 比例更高。这条证据已被仲裁为"声称与实测的对照，客观并列"——不是同一边界下的事实矛盾，而是证据层级不同（独立实测 vs 官方自述）。社区侧同样共现"引用质量"痛点，甚至有 Cornell 的 preprint 记录 Reddit 用户发现的引用污染漏洞。

**其二，官方自报分普遍缺乏独立复测，但部分方向被第三方确认。** 一个值得注意的例外是 Perplexity 的引用准确率（第三方量化 90.24%，DRA 组最高）与 Gemini 的 RACE 总分（48.88，DRA 组最高）——这两个方向与官方高排名声称一致，属于"获得第三方确认的官方声称"。另一个反例是 Gemini 的输出质量：Section AI 实测（n=1，样本极小）批评其输出"过于高层级、不可直接使用"，与 RACE 第一形成不同评测场景下的结论分歧。至于"官方声称能力"与"社区感知"的落差，跨服务共现的社区痛点集中在三个词：**引用质量、配额成本、深度不足**。

**其三，开源与付费的引用机制形成开放度对照。** 开源侧引用机制可见可审计（OpenDeepResearch 强制编号引用 + Sources 段、hyperresearch 引用-句子绑定 + 撤稿检测），付费侧多为黑盒（Perplexity 引用机制未披露）。可见性本身不是优点，但它决定了证据链能否被独立核查——这正是开源方案与付费方案在"证据与知识管理"维度上最本质的差异。与此同时，可靠性攻击研究正在成为新兴维度：检索重叠使单页 UGC 污染可操纵引用（该攻击已在 STORM、Co-STORM、OmniThink 三个开源系统上验证成功）、Search-Time Contamination 可让公开基准性能虚增最高 4%、轨迹劫持与误导知识采纳均有量化证据。

---

## 七、局限与风险：繁荣之下的五道阴影

1. **成本与配额**：付费侧普遍以订阅配额或积分制限流（ChatGPT Pro 250 次/月、Manus 免费 300 积分/日而单任务约消耗 1500 积分），真实单次成本不透明；开源侧成本依赖模型 API 与检索服务，GPT Researcher 约 0.4 美元/次的估算不含检索与图片费用。
2. **引用可靠性**：3-13% 的引用幻觉率、5-18% 的引用无法解析，直接动摇"证据引用"这一公共能力基线的地基；领域差异显著（Business 5.4% 至 Theology 11.4%）。
3. **评测污染**：同名不同源的基准、官方附属基准的利益相关、公开基准的搜索时污染——排行榜上的数字需要先问"谁测的、测什么、量纲是什么"。
4. **稳定性事件**：Manus 从收购、被命令撤销到拆分，暴露了付费服务对地缘政治与监管的脆弱性；多 agent 框架层的快速迭代（Swarm 废弃、AutoGen 维护模式）则是开源侧的不确定性。
5. **定价公开度下降**：ChatGPT 与 Perplexity 的美元价格官方均未披露（JS 渲染 / 登录墙），Genspark 个人定价登录墙——付费生态的信息透明度在倒退。

---

## 八、本平台对比：一份客观的知识分析产物

> 本节是最终知识分析产物（分析观点），不是调研采集的断言。依据为本平台的设计定义（状态机管控、证据链、知识底座），用于客观对照生态方案的位置，**不产出改进方向建议**。

把调研管理平台放入生态坐标系，它在四个维度上的位置可以客观陈述如下：

| 维度 | 生态代表方案 | 调研管理平台（分析观点） |
|---|---|---|
| 证据链 | 多数付费方案黑盒、引用机制不可审计；开源方案可见但多为"引用即证据" | 强制 raw → 采录 → 分析 → 知识包四级证据链，引用必须可追溯到来源，冲突必须仲裁 |
| 状态机 | 多数为 agent loop / 流水线，无工程级状态管控 | 状态机管控（规划 → 采集 → 分析 → 知识包 → 报告闸门），批次推进、饱和判定 |
| 知识底座 | 仅 hyperresearch 有跨会话 vault；其余普遍无长期记忆 | 可持续复用的知识底座（断言 + 关系 + 冲突仲裁 + 概念索引），报告只是知识系统的一次消费 |
| 成本 | 付费订阅 / 积分；开源自托管仍需模型与检索 API | 无付费 API 依赖（客观陈述，非优劣判断） |

对照的要点不是"谁更好"，而是**生态方案的取舍在本平台上以另一种方式被回答**：生态用"多 agent 并行"解决上下文膨胀，本平台用状态机 + 分批推进管控复杂度；生态把"引用"当作输出格式，本平台把"可追溯"当作知识单元的内建属性；生态的长期记忆普遍缺失，本平台把"可持续复用、可更新、可反驳的知识单元"写进知识底座原则。这些差异是设计选择的结果，本报告只做客观陈述。

**已知缺口（诚实声明）**：本报告的能力矩阵中，付费方案（除 Gemini 外）的能力证据几乎全部来自官方声称，未经独立复测；Genspark 完全缺失第三方评测；DRB 论文全文细节、DRACO 官方 PDF、各框架对反多 agent 批评的回应、中文社区原生体验帖等仍是待补线索；OpenAI Agents SDK 中 Swarm 的迁移说明尚待官方文档确认。这些缺口意味着：本文对生态的判断是"证据驱动的观察"，不是"定论"。

---

## 附录：来源与引用

（按主题分组，原始标题为主；URL 以知识包反查的 display_citation 为准）

**官方文档与产品页**
- ChatGPT Deep Research 官方发布页（OpenAI，2025-02 发布，含 2025-04/2025-07/2026-02 更新标注）
- Introducing Perplexity Deep Research（Perplexity 官方博客）
- Perplexity 产品页 / 帮助中心 Advanced Deep Research / Changelog（2026-02、2026-06）
- Gemini Deep Research 官方说明合集（专项页 + API 文档 + 发布文 + 帮助中心）
- Kimi Deep Research 官方功能页（Moonshot AI，2026-06）
- Manus 官网 / 帮助中心官方定价与退款政策（2026 现行价目）
- OpenAI Operator System Card（发布前官方安全报告）
- xAI Web Search 工具 API 文档

**开源项目与论文**
- dzhng/deep-research（GitHub）
- OpenDeepResearch（GitHub，LangGraph 生态）
- STORM（stanford-oval/storm，GitHub；论文 arXiv:2402.14207）
- Co-STORM（论文 arXiv:2408.15232，EMNLP 2024）
- GPT Researcher（assafelovic/gpt-researcher，GitHub）
- hyperresearch（GitHub，Claude Code Skill）
- OpenManus（FoundationAgents/OpenManus，GitHub）
- LangChain Deep Agents 官方文档 / LlamaIndex 官方文档
- CAMEL / MetaGPT / OpenAI Swarm / Microsoft AutoGen / Microsoft Agent Framework（GitHub）
- Gemini Fullstack LangGraph Quickstart（Google 官方开源仓库）
- DSPy 论文（arXiv:2310.03714，Stanford）
- Anthropic《Building Effective Agents》/ Cognition《Don't Build Multi-Agents》（博客）
- DeerFlow（字节跳动开源）、WebThinker（arXiv:2504.21776）

**评测基准**
- USTC Deep Research Bench（arXiv:2506.11763）/ FutureSearch DRB（arXiv:2506.06287）/ DRB II（arXiv:2601.08536）
- DRACO（Perplexity + Harvard，arXiv:2602.11685）/ DeepResearchEval（arXiv:2601.09688）
- LiveResearchBench（arXiv:2510.14240）/ GAIA（arXiv:2311.12983）/ OSWorld（arXiv:2404.07972）/ WebArena（arXiv:2307.13854）
- hyperresearch 官方附属评测 harness（"benchmarked internally"，官方自认第三方验证待定）

**独立评测与学术审计**
- DRB 第三方评测（RACE / FACT 指标，DRA 组横向）
- Section AI 实测（Gemini DR 输出质量，n=1）
- AIMultiple DR-50 / DR-2T 评测（含 agent CLI 类对照，商业 B2B 机构，方法论公开）
- DRBench / ExpertQA 引用幻觉学术审计（53,090 / 168,021 条 URL，含 urlhealth 工具）
- UGC 污染攻击研究（arXiv:2605.24245）/ FORGE 轨迹劫持（arXiv:2607.04718）/ MisKnow-Agent（arXiv:2607.20891）/ Search-Time Contamination（arXiv:2606.05241）

**媒体与社区反馈**
- Reddit r/perplexity_ai、r/ChatGPTPro、r/Bard 等社区聚合反馈（8 平台 20+ URL）
- Reuters / TechCrunch / Bloomberg / The Guardian / BBC（Meta-Manus 收购、撤销、拆分报道）
- 澎湃新闻 / 证券时报 / 硅谷101 / 钛媒体（Manus 评测与用户反馈）

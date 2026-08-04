# raw-S032：OpenAI《Computer-Using Agent》技术博客

- source_id: S032
- source_url: https://openai.com/index/computer-using-agent/
- 标题: Computer-Using Agent
- 发布: 2025-01-23（January 23, 2025）
- 发布方: OpenAI（Research / Release 栏目）
- 访问日期: 2026-08-04
- 抓取方式: 多源搜索 skill —— Tavily（确认 URL）+ webfetch（渠道1，正文全文）
- 内容性质: 官方技术博客（OpenAI 立场，官方声称），本文件为原文存档，供采录溯源
- 抓取说明: 表格原为 HTML 表格，markdown 转换后列对应存在错位风险；表格数字以正文文字陈述为准，表格链接按原文保留

---

## 正文存档（去除页面导航/页脚）

### 导语

Today we introduced a research preview of Operator, an agent that can go to the web to perform tasks for you. Powering Operator is Computer-Using Agent (CUA), a model that combines GPT‑4o's vision capabilities with advanced reasoning through reinforcement learning. CUA is trained to interact with graphical user interfaces (GUIs)—the buttons, menus, and text fields people see on a screen—just as humans do. This gives it the flexibility to perform digital tasks without using OS-or web-specific APIs.

CUA builds off of years of foundational research at the intersection of multimodal understanding and reasoning. By combining advanced GUI perception with structured problem-solving, it can break tasks into multi-step plans and adaptively self-correct when challenges arise. This capability marks the next step in AI development, allowing models to use the same tools humans rely on daily and opening the door to a vast range of new applications.

While CUA is still early and has limitations, it sets new state-of-the-art benchmark results, achieving a 38.1% success rate on OSWorld for full computer use tasks, and 58.1% on WebArena and 87% on WebVoyager for web-based tasks. These results highlight CUA's ability to navigate and operate across diverse environments using a single general action space.

We've developed CUA with safety as a top priority to address the challenges posed by an agent having access to the digital world, as detailed in our Operator System Card. In line with our iterative deployment strategy, we are releasing CUA through a research preview of Operator at operator.chatgpt.com for Pro Tier users in the U.S. to start. By gathering real-world feedback, we can refine safety measures and continuously improve as we prepare for a future with increasing use of digital agents.

### How it works

CUA processes raw pixel data to understand what's happening on the screen and uses a virtual mouse and keyboard to complete actions. It can navigate multi-step tasks, handle errors, and adapt to unexpected changes. This enables CUA to act in a wide range of digital environments, performing tasks like filling out forms and navigating websites without needing specialized APIs.

Given a user's instruction, CUA operates through an iterative loop that integrates perception, reasoning, and action:

- **Perception**: Screenshots from the computer are added to the model's context, providing a visual snapshot of the computer's current state.
- **Reasoning**: CUA reasons through the next steps using chain-of-thought, taking into consideration current and past screenshots and actions. This inner monologue improves task performance by enabling the model to evaluate its observations, track intermediate steps, and adapt dynamically.
- **Action**: It performs the actions—clicking, scrolling, or typing—until it decides that the task is completed or user input is needed. While it handles most steps automatically, CUA seeks user confirmation for sensitive actions, such as entering login details or responding to CAPTCHA forms.

### Evaluations

CUA establishes a new state-of-the-art in both computer use and browser use benchmarks by using the same universal interface of screen, mouse, and keyboard.

#### 评测基准表（原文表格，markdown 转换后记录）

表头（转换后）：Benchmark type | Benchmark | Computer use (universal interface) | Web browsing agents | Human | OpenAI CUA | Previous SOTA | Previous SOTA

| Benchmark type | Benchmark | OpenAI CUA | Previous SOTA | Previous SOTA | Human |
|---|---|---|---|---|---|
| Computer use | OSWorld | 38.1% | 22.0%（链接指向 Anthropic computer use 公告） | - | 72.4%（链接指向 OSWorld 论文 arxiv.org/abs/2404.07972） |
| Browser use | WebArena | 58.1% | 36.2%（链接指向 ServiceNow browsergym leaderboard） | 57.1%（链接指向 Kura spreadsheet，docs.google.com） | 78.2%（链接指向 WebArena 论文 arxiv.org/abs/2307.13854） |
| Browser use | WebVoyager | 87.0% | 56.0%（链接指向 trykura.com/benchmarks） | 87.0%（链接指向 trykura.com/benchmarks） | - |

> 注：原始表格为 6 列多链接结构，markdown 转换列对应关系按链接归属推断，存在错位风险；以下正文文字陈述为权威数字。

Evaluation details are described here（https://cdn.openai.com/cua/CUA_eval_extra_information.pdf）

#### Browser use

WebArena and WebVoyager are designed to evaluate the performance of web browsing agents in completing real-world tasks using browsers. WebArena utilizes self-hosted open-source websites offline to imitate real-world scenarios in e-commerce, online store content management (CMS), social forum platforms, and more. WebVoyager tests the model's performance on online live websites like Amazon, GitHub, and Google Maps.

In these benchmarks, CUA sets a new standard using the same universal interface that perceives the browser screen as pixels and takes action through mouse and keyboard. CUA achieved a 58.1% success rate on WebArena and an 87% success rate on WebVoyager for web-based tasks. While CUA achieves a high success rate on WebVoyager, where most tasks are relatively simple, CUA still needs more improvements to close the gap with human performance on more complex benchmarks like WebArena.

（此处原文含一个 WebVoyager 交互轨迹示例：Cambridge Dictionary Plus 语法测验任务，包含 152 步 Perception/Reasoning/Action 标注过程，用户指令为 "Go to the Plus section of Cambridge Dictionary, finish a recommended Grammar quiz without login and tell me your final score."）

#### Computer use

OSWorld is a benchmark that evaluates models' ability to control full operating systems like Ubuntu, Windows, and macOS. In this benchmark, CUA achieves 38.1% success rate. We observed test-time scaling, meaning CUA's performance improves when more steps are allowed. The figure below compares CUA's performance with previous state-of-the-arts with varying maximum allowed steps. Human performance on this benchmark is 72.4%, so there is still significant room for improvement.

（原文此处含 OSWorld 折线图：success rates (%) vs max steps allowed on a logarithmic scale，蓝色线 OpenAI CUA，橙色点 Claude 3.5 Sonnet - Computer use，并附多个 OSWorld 任务可视化示例：下载讲义、合并 PDF、压缩图片、计算价格、导出图片；其中"下载每周讲义 PDF"示例任务含 267 步轨迹标注，任务提示含 sudo 密码、thunderbird 账户密码等测试环境信息）

### CUA in Operator

We're making CUA available through a research preview of Operator, an agent that can go to the web to perform tasks for you. Operator is available to Pro users in the U.S. at operator.chatgpt.com. This research preview is an opportunity to learn from our users and the broader ecosystem, refining and improving Operator iteratively. As with any early-stage technology, we don't expect CUA to perform reliably in all scenarios just yet. However, it has already proven useful in a variety of cases, and we aim to extend that reliability across a wider range of tasks.

In the table below, we present CUA's performance in Operator on a handful of trials given a prompt to illustrate its known strengths and weaknesses.

| Category | Prompt（概要） | Success / attempts | Note |
|---|---|---|---|
| Interacting with various UI components to accomplish tasks | Britannica 地图任务（两轮：搜索熊栖息地地图 + 查看黑/棕/北极熊链接并总结特征、保存链接） | 10 / 10 | CUA can interact with various UI components to search, sort, and filter results to find the information that users want. Reliability varies for different websites and UIs. |
| Interacting with various UI components | Target 折扣商品任务（poppi 益生菌汽水、西瓜味 12fl oz 罐装、是否无麸质） | 9 / 10 | 同上 |
| Interacting with various UI components | Redfin 找房任务（西雅图、≥3 卧 2 卫、节能设计如太阳能/LEED、预算 $600k-$800k、约 1500 sq ft） | 3 / 10 | 同上 |
| Tasks that can be accomplished through repeated simple UI interactions | Todoist 创建项目+购物清单（香蕉 6 根、牛油果 2 个等 8 项） | 10 / 10 | CUA can reliably repeat simple UI interaction multiple times to automate simple, but tedious tasks from users. |
| Tasks through repeated simple UI interactions | Spotify 搜索美国 1990s 最流行歌曲并创建 ≥10 首歌曲单 | 10 / 10 | 同上 |
| Tasks where CUA shows a high success rate only if prompts include detailed hints on how to use the website | tagvenue.com 找音乐厅任务（伦敦、150 人、2025-02-22 全天 9am-12am、<£90/小时、含停车+轮椅无障碍，带"check the filters section"提示） | 8 / 10 | Even for the same task, CUA's reliability might change depending on how we are prompting the task. In this case, we can improve the reliability by providing specifics of date and by providing hints on which UI should be used. |
| 同上（无 UI 提示版） | 同上任务但提示更模糊（"entire day from 9 am"、无 filters 提示） | 3 / 10 | 同上 |
| Struggling to use unfamiliar UI and text editing | html5editor 文本编辑任务（输入给定文本并按指令应用 header/red/bold/italic/右对齐等格式） | 4 / 10 | When CUA has to interact with UIs that it hasn't interacted much with during training, it struggles to figure out how to use the provided UI appropriately. It often results in lots of trial and errors, and inefficient actions. CUA is not precise at text editing. It often makes lots of mistakes in the process or provides output with error. |

### Safety

Because CUA is one of our first agentic products with an ability to directly take actions in a browser, it brings new risks and challenges to address. As we prepared for deployment of Operator, we did extensive safety testing and implemented mitigations across three major classes of safety risks: misuse, model mistakes, and frontier risks. We believe it is important to take a layered approach to safety, so we implemented safeguards across the whole deployment context: the CUA model itself, the Operator system, and post-deployment processes. The aim is to have mitigations that stack, with each layer incrementally reducing the risk profile.

The first category of risk is **misuse**. In addition to requiring users to comply with our Usage Policies, we have designed the following mitigations to reduce Operator's risk of harm due to misuse, building off our safety work for GPT‑4o:

- **Refusals**: The CUA model is trained to refuse many harmful tasks and illegal or regulated activities.
- **Blocklist:** Operator cannot access websites that we've preemptively blocked, such as many gambling sites, adult entertainment, and drug or gun retailers.
- **Moderation**: User interactions are reviewed in real-time by automated safety checkers that are designed to ensure compliance with Usage Policies and have the ability to issue warnings or blocks for prohibited activities.
- **Offline detection:** We've also developed automated detection and human review pipelines to identify prohibited usage in priority policy areas, including child safety and deceptive activities, allowing us to enforce our Usage Policies.

The second category of risk is **model mistakes**, where the CUA model accidentally takes an action that the user didn't intend, which in turn causes harm to the user or others. Hypothetical mistakes can range in severity, from a typo in an email, to purchasing the wrong item, to permanently deleting an important document. To minimize potential harm, we've developed the following mitigations:

- **User confirmations:** The CUA model is trained to ask for user confirmation before finalizing tasks with external side effects, for example before submitting an order, sending an email, etc., so that the user can double-check the model's work before it becomes permanent.
- **Limitations on tasks:** For now, the CUA model will decline to help with certain higher-risk tasks, like banking transactions and tasks that require sensitive decision-making.
- **Watch mode:** On particularly sensitive websites, such as email, Operator requires active user supervision, ensuring users can directly catch and address any potential mistakes the model might make.

One particularly important category of model mistakes is **adversarial attacks on websites** that cause the CUA model to take unintended actions, through prompt injections, jailbreaks, and phishing attempts. In addition to the aforementioned mitigations against model mistakes, we developed several additional layers of defense to protect against these risks:

- **Cautious navigation:** The CUA model is designed to identify and ignore prompt injections on websites, recognizing all but one case from an early internal red-teaming session.
- **Monitoring:** In Operator, we've implemented an additional model to monitor and pause execution if it detects suspicious content on the screen.
- **Detection pipeline:** We're applying both automated detection and human review pipelines to identify suspicious access patterns that can be flagged and rapidly added to the monitor (in a matter of hours).

Finally, we evaluated the CUA model against **frontier risks** outlined in our Preparedness Framework, including scenarios involving autonomous replication and biorisk tooling. These assessments showed no incremental risk on top of GPT‑4o.

For those interested in exploring the evaluations and safeguards in more detail, we encourage you to review the Operator System Card, a living document that provides transparency into our safety approach and ongoing improvements.

As many of Operator's capabilities are new, so are the risks and mitigation approaches we've implemented. While we have aimed for state-of-the-art, diverse and complementary mitigations, we expect these risks and our approach to evolve as we learn more.

### Conclusion

CUA builds on years of research advancements in multimodality, reasoning and safety. We have made significant progress in deep reasoning through the o-model series, vision capabilities through GPT‑4o, and new techniques to improve robustness through reinforcement learning and instruction hierarchy. The next challenge space we plan to explore is expanding the action space of agents. The flexibility offered by a universal interface addresses this challenge, enabling an agent that can navigate any software tool designed for humans. By moving beyond specialized agent-friendly APIs, CUA can adapt to whatever computer environment is available—truly addressing the "long tail" of digital use cases that remain out of reach for most AI models.

We're also working to make CUA available in the API, so developers can use it to build their own computer-using agents. As we continue to iterate on CUA, we look forward to seeing the different use cases the community will discover.

### Authors

OpenAI

### References

- Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku（Anthropic，https://www.anthropic.com/news/3-5-models-and-computer-use）
- Model Card Addendum: Claude 3.5 Haiku and Upgraded Claude 3.5 Sonnet（Anthropic PDF）
- Kura WebVoyager benchmark（https://www.trykura.com/benchmarks）
- Google project mariner（https://deepmind.google/technologies/project-mariner/）
- OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments（https://os-world.github.io/）
- WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models（arxiv.org/abs/2401.13919）
- WebArena: A Realistic Web Environment for Building Autonomous Agents（https://webarena.dev/）

### Citations

Please cite OpenAI and use the following BibTeX for citation: http://cdn.openai.com/cua/cua2025.bib

---

## 抓取渠道记录

- Tavily 搜索词: "OpenAI computer using agent CUA blog"（确认 URL = openai.com/index/computer-using-agent，发布日期 2025-01-23，含摘要级内容片段）
- 正文渠道: webfetch（opencode 内置，自动走系统代理），format=markdown，成功获取全文
- 备选渠道结果（记录）：CloakBrowser networkidle 超时 → domcontentloaded 渲染成功但 defuddle 提取失败（页面 HTML 11,263 字符为动态壳）；web-fetch.cmd 403 Forbidden

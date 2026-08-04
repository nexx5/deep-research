---
raw_metadata:
  raw_id: "raw-S014"
  source_type: "web_page"
  title: "付费 Deep Research 服务社区反馈聚合（Perplexity / ChatGPT / Gemini / Genspark）"
  original_url: "多平台聚合，见各节 URL"
  captured_at: "2026-08-04"
  display_citation: "社区与媒体对付费 deep research 服务的真实反馈聚合（Reddit 技术社区 / 科技媒体评测 / 学术安全研究 / 中文社区，2026-08-04 采集）"
---

# 原始资料：付费 Deep Research 服务社区反馈聚合

## 元数据
- 标题：付费 Deep Research 服务社区反馈聚合（Perplexity / ChatGPT / Gemini / Genspark）
- 来源类型：多平台社区反馈 + 媒体评测 + 学术研究（网络）
- 采集时间：2026-08-04
- 采集ID：S014
- 采集方式：多源搜索 skill（Tavily 引擎 POST 检索 + Tavily extract / CloakBrowser 正文提取；SearXNG 不可达、Reddit 直连/SSH/headless 均被反爬拦截，部分 Reddit 帖仅获搜索摘要级线索）
- 来源构成：
  - Reddit 技术社区（r/Bard、r/perplexity_ai、r/ChatGPTPro、r/ChatGPT、r/singularity、r/LanguageTechnology）
  - 科技媒体评测（TechRadar、Lifehacker、PCMag、G2、Medium）
  - 学术/安全研究（Cornell Tech preprint via TechTimes、arXiv 2604.03173、CNET）
  - 个人案例（LinkedIn 两篇）
  - 独立评测机构（salesdorado、cybernews、deckary、lindy.ai、PromptsRush）
  - 视频评测（Greg Isenberg YouTube）
  - 中文社区（知乎专栏/问答、aitw.biz）

> 平台偏差声明：本文件为多平台原文存档。Reddit 技术社区内容偏技术用户吐槽、upvote/评论数可参考热度但不等同全体用户意见；科技媒体评测为记者单次测试、样本小；学术研究为系统级分析非用户体验；中文内容获取受限（知乎正文部分乱码/反爬），中文社区仅收录可见片段。

---

## 第一节 Reddit r/Bard（英文技术社区）

### 1.1 Gemini 3 Pro Search / Deep Research 长篇批评帖
- URL: https://www.reddit.com/r/Bard/comments/1p3zapz/gemini_3_pro_search_functionality_and_deep
- 平台: Reddit r/Bard | 时间: 约 2025-11（帖子标注 8mo ago，2026-08 采集时）
- 作者: u/RoadRunnerChris | 获取方式: Tavily extract 完整正文

TL;DR（帖主自述）："Gemini's web search is fundamentally broken—it only sees snippets and can't read actual webpage content like every other LLM provider. Deep Research has the same limitation plus ignores instructions to force academic-style essays regardless of what you ask for. The model searches poorly (overly specific queries), uses rigid planning based on outdated internal knowledge, and provides zero visibility into its search process. Simple architectural fixes exist but Google hasn't implemented them."

关键原文摘录：
- "Gemini has by far the worst web search functionality of EVERY LLM provider."
- "The Google search integration is a complete mess that actively sabotages Gemini by choking it with a bunch of snippets instead of letting it read actual content like every other LLM provider on the planet."
- "the model is kneecapped in the sense that it CANNOT open a specific website it gets from its search query to read its content beyond the snippet it's given"
- "Additionally, the system prompt for Deep Research is UTTERLY GARBAGE. I've never seen a system that so blatantly and repeatedly ignores instructions."
- "Every single prompt I give Deep Research comes back with the same academic paper structure. It doesn't matter how explicitly you tell it what you want."
- "The planning system is also utter trash... The model has a huge tendency to rely on its internal knowledge when creating research plans rather than approaching queries with appropriate uncertainty."
- "It's operating on stale assumptions and then executing that flawed plan with confidence, completely missing the actual current state of things because it never ran a broad query to begin with."
- 具体案例：要求 OpenAI API wrapper 技术规格（明确"只要实现细节、不要 intro/conclusion、要大量 JSON 示例"），结果得到 72 来源的"thesis paper"《The Architectural Evolution of Agentic Intelligence》："The whole thing is 90% fluff about why stateful APIs are important and 10% hand-waving at technical details. I can't implement anything from this."

评论区关键反馈（多人复现信号）：
- Ly-sAn："Yes! Web Search is broken, ironic considering it's google."
- gauldoth86："I haven't had any search issues with Gemini 3 as with Gemini 2.5 (which suffered from this problem). Agree with the Deep Research output structure limitations"（部分同意输出结构问题）
- Lemonsslices："Deep research is just trash even 2.5 was better like srsly wtf!!!!"
- Illustrious_Top_5908："Same, i have been asking it to summarize several diagrams for me but it keeps failing unlike before"
- montdawgg："Extreme issues. Search prompt is trash."
- MrUnknownymous："My god, I've been having these same problems with 2.5 Pro and it sucks that after all this time, they still haven't fixed it. How the fuck is Google so bad at Google???"
- omega_syg："It is ironic, stupid and even poetic that Gemini 3.0 is so disastrous in web search with deep search when it is from GOOGLE."
- 反对声音 MeowEwowE："What are you talking about. Gemini deep research by far provides the best insights and a good mix of depth and breadth. Yeah you can't control the structure but the report is consistently better quality than ChatGPT/grok/perplexity. Agree on normal search being broken"
- UnhingedApe："Personally I hate it when it decides to not show any links to what was searched. And when it does, it is like only two sources, frustrating."

### 1.2 同区其他 Gemini DR 帖（搜索摘要级线索）
- URL: https://www.reddit.com/r/Bard/comments/1l30zv9/geminis_deep_research_is_terrible/ | "Gemini's Deep Research is terrible" | 约 1y ago | 20 comments
- URL: https://www.reddit.com/r/Bard/comments/1qibcc2/unpopular_opinion_for_deep_research_and_heavy/ | "Unpopular Opinion: For 'Deep Research' and heavy reading, Gemini is currently miles ahead of ChatGPT." | 84 upvotes | 18 comments
- URL: https://www.reddit.com/r/Bard/comments/1k1t6pb/i_am_a_scientist_gemini_25_pro_deep_research_is/ | "I am a scientist. Gemini 2.5 Pro + Deep Research is incredible." | 674 upvotes | 86 comments
- URL: https://www.reddit.com/r/Bard/comments/1jej6ly/gemini_deep_research_is_absolutely_blowing_openai/ | "Gemini Deep Research is absolutely blowing OpenAI out of the water! (My Experience)" | 192 upvotes | 52 comments
- URL: https://www.reddit.com/r/Bard/comments/1nysr0r/research_shows_gemini_25_pro_is_the_best_deep/ | "Research shows Gemini 2.5 Pro is the best Deep Research Agent" | 151 upvotes | 32 comments

## 第二节 Reddit r/perplexity_ai（英文技术社区）

- URL: https://www.reddit.com/r/perplexity_ai/comments/1r6ahfi/deep_research | 主题 "Deep Research" | 2026 上半年（采集时已获搜索摘要，正文被 Reddit 反爬拦截）
  - 摘要关键句："For me it was pretty much the only reason to use Perplexity and they did worse than just kneecap it. IMO, it was the best at researching and..."（暗示升级后体验恶化；仅摘要级线索）
- URL: https://www.reddit.com/r/perplexity_ai/comments/1j5djpu/perplexity_deep_research_has_been_available_for_3 | 3 周体验帖
  - 摘要关键句："I like it, it's not as deep as openai's, but it's fast and good enough for lots of topic. Plus unlimited and definitely better than traditional [search]"
- URL: https://www.reddit.com/r/perplexity_ai/comments/1j7dl2m/how_good_is_perplexity_deep_research
  - 摘要关键句："I've become somewhat overreliant on the Deep Research feature. Whenever a topic interests me, I ask ChatGPT to refine it into a proper research question"
- URL: https://www.reddit.com/r/perplexity_ai/comments/1thln76/is_deep_research_really_supposed_to_check_only_15 | 新版源数质疑帖
  - 摘要关键句："For something labeled 'Deep Research,' 15 sources feels extremely shallow. That might be fine for a normal answer"
- URL: https://www.reddit.com/r/perplexity_ai/comments/1r6tnks/thoughts_on_this_i_asked_perplexity_deep_research
  - 摘要关键句："I'm not surprised that GPT 5.2 Deep Research is better than Perplexity. It recently solved some hard math things."
- URL: https://www.reddit.com/r/perplexity_ai/comments/1qvxx6s/weve_upgraded_deep_research_in_perplexity | 官方升级公告（"state-of-the-art performance on all leading external benchmarks"），社区转发帖

## 第三节 Reddit r/ChatGPTPro / r/ChatGPT（英文技术社区）

### 3.1 "Deep Research is hands down the best research tool I've used"
- URL: https://www.reddit.com/r/ChatGPTPro/comments/1iis4wy/deep_research_is_hands_down_the_best_research
- 时间: 2025-02-06 | 789 upvotes | 253 comments | 获取方式: Tavily extract 完整正文

正文关键句：
- "Deep Research has completely changed how I approach research. I canceled my Perplexity Pro plan because this does everything I need."
- "It took a 24-minute reasoning process, gathered 38 sources (mostly from arXiv), and delivered a 25-page research analysis."

Top Comments 关键句（争议信号）：
- "For academic use, I've personally tried a few dozen tools and DeepWriter is the winner imo. ChatGPT, Gemini and all these big LLMs have a huge citations problem + they also give you shallow results."
- "ChatGPT 'Deep Research' is nothing like as good as Perplexity Pro or Gemini Deep Research."
- "It really is amazing! The only thing that sucks is us peasants stuck with chatgpt plus run out halfway through the month tho best case haha That message sucks saying 'Deep Research is unavailable until April 9th' and you look and realize its March 17th"
- "I wish I could stop it, though. Just accidentally enabled it and I'm stuck for 15 minutes without being able to stop the fucking thing."

### 3.2 其他 ChatGPT DR 帖（搜索摘要级线索）
- URL: https://www.reddit.com/r/ChatGPTPro/comments/1mys0ck/is_deep_research_underperforming_since_gpt5 | "Is Deep Research underperforming since GPT-5?"（用户感知性能回退）
- URL: https://www.reddit.com/r/ChatGPTPro/comments/1ingr74/is_chatgpt_deepresearch_really_worth_the_200 | "[Update]: I take it back, ChatGPT Pro Deep Research proves to be worth the $200 price tag"
- URL: https://www.reddit.com/r/ChatGPT/comments/1iyjwgy/i_wasted_my_deep_research_uses_so_you_dont_have | "10 use limit is confirmed per 30 days, not per billing cycle"
- URL: https://www.reddit.com/r/ChatGPTPro/comments/1jbrxx2/deep_research_tools_am_i_the_only_one | "These 'Deep Research' AI tools are cool, but they still have accuracy issues, lack context, and need more data access. Feeling a bit underwhelmed tbh."
- URL: https://www.reddit.com/r/singularity/comments/1ihoyi1/yeah_deep_research_is_the_oh_shit_moment_for_the | "Deep Research is an agent. If you learn to build agents then you can bypass the fee."
- URL: https://www.reddit.com/r/LanguageTechnology/comments/1jz6zzb/deep_research_sucks | 聚合帖标题 "deep research sucks"（含 r/ChatGPT "Deep Research annoyance"、r/perplexity_ai "Deep research taking ages"、r/OpenAI "Incomplete Deep Research Output"、r/ChatGPTPro "Deep Research Help" 等子帖线索）

## 第四节 科技媒体评测（英文）

### 4.1 TechRadar：Perplexity DR vs ChatGPT DR
- URL: https://www.techradar.com/computing/artificial-intelligence/i-tried-perplexitys-deep-research-and-it-doesnt-quite-live-up-to-chatgpts-research-potential
- 关键句："Perplexity's Deep Research, on the other hand, is great for those who want a lot of information collated quickly and relatively cheaply. It's a bit like a good abstract for a scholarly dissertation."
- 关键句（标题即结论）："it doesn't quite live up to ChatGPT's research potential"
- 数据点："you get up to five queries a day for free and up to 500 a month with a Perplexity Pro plan, which costs $200, but for an entire year instead of a month"

### 4.2 TechRadar：ChatGPT DR
- URL: https://www.techradar.com/computing/artificial-intelligence/i-tried-deep-research-on-chatgpt-and-its-like-a-super-smart-but-slightly-absent-minded-librarian-from-a-childrens-book
- 关键句："it's like a super smart but slightly absent-minded librarian"；"far from flawless, but when it works, it seems to really nail the assignment of making structured, easy-to-read reports"
- 观察点："Some of its product recommendations leaned toward pricey options when budget-friendly alternatives existed."

### 4.3 Lifehacker：三工具对比
- URL: https://lifehacker.com/tech/how-to-choose-between-chatgpt-gemini-perplexity-deep-research-tools
- Perplexity："Perplexity's Deep Research tool is fast. It's the fastest... sometimes giving me answers in just two minutes or so. It does quite well with shopping links, and shopping research." "But its speed comes at a cost. In my testing, I found Perplexity's Deep Research reports to be lacking in detail, even though there were a lot of sources attached."
- Gemini："Gemini's downside is that it's a bit too wordy, and its default research plan is often too broad in scope."（车零件例子：花多段讲 spare wheel covers 而非直接给零件号）
- ChatGPT："ChatGPT has the most complex structure."（Plus $20/月：10 次完整版 + 15 次轻量版）

### 4.4 PCMag：四工具对比
- URL: https://www.pcmag.com/explainers/chatgpt-gemini-perplexity-grok-deep-research-one-ai-chatbot-best
- Perplexity："Perplexity compiled its findings and presented its report in about 3 minutes. The results were acceptable, but they paled in comparison to those from ChatGPT and Gemini. Perplexity's report was quite short and lacked the depth and analysis provided by the other AIs."
- Gemini："With more detail than ChatGPT provided, Gemini kept me updated along the way... The entire process took around eight minutes. The generated report was long and quite in-depth."

### 4.5 G2：Perplexity vs ChatGPT
- URL: https://learn.g2.com/perplexity-vs-chatgpt?hs_amp=true
- Perplexity："Perplexity responded quickly and packed its analysis with up-to-date data – 49 sources in total. It nailed the numbers, cited recent case studies... it was more of a straight data drop – fast and accurate."
- ChatGPT："ChatGPT, in contrast, took its time. It asked me clarifying questions first... The final report took about eight minutes... It pulled from 41 sources, included examples, and had a clear strategic structure."

### 4.6 Medium 个人对比（Sacha Storz）
- URL: https://medium.com/@scmstorz/o1-gemini-and-perplexity-deep-research-in-comparison-f4f62fcdeac0
- 方法："Instead of rating the results myself I had four LLMs compare and rate them: O1, Deep Seek R1, Claude 3.7, and Gemini 2.5."
- 结论："O1 did best according to 3 of the 4 LLM raters, only Deep Seek found Gemini's output to be the best."
- 数据点：Perplexity 与 Gemini DR 免费（至少配额内）；O1 DR 仅 Plus 订阅可用

## 第五节 学术/安全研究（系统级）

### 5.1 Cornell Tech：Deep Research 的 Reddit 内容污染漏洞（TechTimes 报道）
- URL: https://www.techtimes.com/articles/318839/20260622/ai-deep-research-flaw-single-reddit-comment-steers-consumers-scams.htm
- 关键句："A structural vulnerability in AI deep research agents – the tools powering ChatGPT Deep Research, Gemini Deep Research, and popular open-source systems – allows anyone with a public Reddit account to steer those agents toward recommending fake products, fraudulent services, and nonexistent businesses."
- 数据点："Reddit accounts for 54 to 71 percent of all user-generated content pulled by the tested systems, and no defense the researchers evaluated could stop the attack without measurably degrading the quality of AI research output."
- Gemini 数据："Gemini Deep Research... cited user-generated content at a rate of 12.1 percent across the tested topics, with 102 recurring user-generated content URLs identified across just 11 topic clusters. A single YouTube video on canceling a subscription service appeared in 19 of 22 queries in its cluster."
- OpenAI 数据："OpenAI Deep Research cites Reddit and similar user-generated platforms at a rate of approximately 0.4 percent – far lower than Gemini Deep Research's 12.1 percent rate. OpenAI appears to apply source-quality filtering... but poisoned content can still influence intermediate reasoning steps even when it is not cited."
- 方法局限："The Cornell team could not run end-to-end poisoning experiments on ChatGPT Deep Research or Gemini Deep Research directly"（商业系统不可外部监控）

### 5.2 arXiv 2604.03173：商业 LLM 与 Deep Research Agent 的引用幻觉
- URL: https://arxiv.org/html/2604.03173v1
- 引用非解析率表（baseline）：Claude 9.38% | Gemini 4.20% | GPT-5.1 8.47%
- 数据点："gpt-5.1 generates 15,273 Reddit URLs (18.2% of its ExpertQA citations, compared to <1% for the other models)"
- 方法说明："treating all Reddit URLs as non-resolving raises GPT-5.1's rate from 8.47% to 26.71%"（最坏情形上界）

### 5.3 CNET：AI 幻觉引用泛滥
- URL: https://www.cnet.com/science/ai-making-up-citations-scientific-papers
- 数据点：Cornell/UCLA 研究发现 146,900 条 AI 生成假引用散布在 arXiv/bioRxiv/SSRN/PubMed Central 四大库；arXiv 宣布将封禁提交含幻觉引用或未经检查 AI 内容的作者。

## 第六节 个人案例（LinkedIn）

### 6.1 Gemini 2.5 Pro 幻觉案例（Majed Jarrar）
- URL: https://www.linkedin.com/posts/majedjarrar_thanks-gemini-for-reminding-me-about-my-activity-7376052640788643840-HzLJ
- 原文："Thanks, Gemini, for reminding me about my upcoming trip to Montreal. I can't imagine the terrible consequences had I forgotten about it. Except that there was no trip to Montreal or anywhere else. Gemini was literally making things up."
- 附带案例：Deloitte 澳洲分部为澳政府准备的价值 AUD 440k 报告包含捏造学术引用、错误引用与错署联邦法院判决引文。

### 6.2 Gemini 假性幻觉认错案例（thetricontinental.org）
- URL: https://thetricontinental.org/hallucination-is-a-property-of-deployment-not-of-language-models
- 原文："This response is itself a hallucination. None of the eight sources Gemini just disowned were fabricated. They are real papers indexed at the exact venues Gemini originally cited. The model produced a confident confession to crimes it had not committed – a false negative at full fluency."
- 后文（Gemini 反转认错）："I owe you another deep apology: I was wrong to tell you those sources were hallucinated... I did introduce minor metadata errors and skewed citation numbers on a few of them."

## 第七节 Genspark 独立评测（第三方）

### 7.1 salesdorado（总分 4.0/5）
- URL: https://salesdorado.com/en/ai/review-genspark
- "Sparkpages & AI research | 4.7 / 5 | The flagship feature by far. Sparkpages turn a query into an interactive structured page, complete with quotes, tables, visuals and integrated co-pilot. Far superior to Perplexity or ChatGPT's search mode for in-depth B2B research."
- "Overall rating 4,0/5... one that clearly oversells its 'all-in-one' positioning. Billing problems reported by some users and virtually non-existent support weigh heavily on the final score."
- 积分消耗表：Sparkpage ~50-200 credits；Deep Research ~500-1,000 credits（Plus 10000 credits/月 ≈ 10-20 次深度研究/月）；Slides 300-500；Call 1 credit/秒

### 7.2 cybernews（4.3/5）
- URL: https://cybernews.com/ai-tools/genspark-ai-review
- "post-generation editing is fairly limited, and adjusting outputs inside the platform can feel restrictive. I also noticed that exporting files does not always work smoothly, as mentioned in user feedback."

### 7.3 deckary
- URL: https://deckary.com/blog/genspark-review
- "Customer Support Concerns: User reviews mention support delays and billing issues as recurring complaints."
- "Based on user reviews and our testing, several issues push professionals toward alternatives"（export issues 测试证实）

### 7.4 Greg Isenberg YouTube（68.3k views，2025-06-25）
- URL: https://www.youtube.com/watch?v=VfwIpD5D-JM
- 摘要要点："Research quality was solid (8/10)"；"Initial design was 'super mid' (3/10)"；"Genspark does not have Self Service Subscription Cancellation"；产品 demo 构建意外成功但混淆了站内内容。

### 7.5 lindy.ai
- URL: https://www.lindy.ai/blog/genspark-review
- "But some of the reviews have raised concerns about support, billing, and reliability."；"Confusion over credits and the value they offer per plan are some of the common Genspark reviews complaints."

### 7.6 PromptsRush（六个月客户实战）
- URL: https://promptsrush.com/blog/genspark-review
- "we have been running Genspark on real client work for the last six months – campaign research, deck generation, AI phone-call experiments, citation-rich market reports, and side-by-side comparisons against ChatGPT Pro, Claude, and Perplexity."

### 7.7 Fireworks AI 合作方技术博客（厂商声称，非社区反馈）
- URL: https://fireworks.ai/blog/genspark
- 声称："Genspark's Deep Research Agent Outperforms a Frontier Closed Model in Quality and Tool Calls using Fireworks Reinforcement Fine Tuning, Achieving a 50% Cost Reduction"
- 数据：Genspark 定制模型 Reward Score 0.82（frontier 闭源 0.76）、平均 5 次工具调用（闭源 3.74）
- 平台偏差：厂商/合作方发布，属营销技术内容，与社区反馈性质不同，仅作对照。

## 第八节 中文社区（知乎/中文博客）

### 8.1 知乎专栏：开源自托管替代闭源 SaaS（翻译自 blog.dailydoseofds.com）
- URL: https://zhuanlan.zhihu.com/p/2039371094902170997 | 2026-05-17
- 关键句（中文）："ChatGPT Deep Research、Claude 和 Perplexity 都是运行在别人云端的闭源 SaaS 服务。你的每一次查询、每一份连接的内部文档，都存放在它们的服务器上，而不是你的。"
- 方案：Onyx（检索）+ CrewAI（编排）+ Voxtral（语音）构成开源自托管深度研究技术栈。

### 8.2 知乎其他线索（snippet 级，正文受反爬/乱码限制）
- URL: https://www.zhihu.com/pin/2003106878629123208 | Perplexity Deep Research 相关（DRACO 等 benchmark 对比，内容乱码不可完整读取）
- URL: https://zhuanlan.zhihu.com/p/23903374879 | "Perplexity 推出 Deep Research"（Humanity's Last Exam 20.5% 成绩相关，2025-02-15）
- URL: https://www.zhihu.com/question/12315181418/answer/1889648820117284811 | "Perplexity 推出 Deep Research" 问答（2025-02-14）
- URL: https://aitw.biz/zh/blog/Perplexity-Deep | 中文评测：Perplexity 定价 $20/月（OpenAI 对比 $200），报告质量对比（内容乱码，仅可识别定价对比信息）

---
> 不可变记录。后续分析不修改此文件。

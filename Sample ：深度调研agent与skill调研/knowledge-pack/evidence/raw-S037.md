---
source_id: S037
source_url: https://github.com/FoundationAgents/OpenManus
title: "OpenManus: An open-source framework for building general AI agents (GitHub 仓库)"
author: MetaGPT 团队（核心作者 Xinbin Liang @mannaandpoem, Jinyu Xiang @XiangJinyu）
date: 2025-03（原型发布）；2026-02-11（访问时最后更新）
fetched_at: 2026-08-04T18:00:00
content_type: github_repo
---

# 原文存档说明

> 主来源为 GitHub 仓库页面抓取。任务给定的 `ShilongLee/OpenManus` 经 GitHub 仓库搜索（`q=OpenManus&type=repositories`，474 结果）确认不存在；按任务指示定位真实主流仓库 `FoundationAgents/OpenManus`（57.9k stars）。原社区仓库 `mannaandpoem/OpenManus` 已重定向至本仓库并归档（mannaandpoem/OpenManus_Archive）。
> 以下内容为 2026-08-04 抓取的仓库主页（README.md + README_zh.md + app 目录结构）原文关键部分。

# 仓库元数据（2026-08-04 抓取）

- 仓库：github.com/FoundationAgents/OpenManus
- Stars: 57.9k | Forks: 10.1k | Watchers: 417 | Commits: 526
- Issues: 294 | Pull requests: 195
- License: MIT
- 官网：https://openmanus.github.io/
- 搜索页显示最后更新：Feb 11（2026，当年不显示年份）
- 原仓库 mannaandpoem/OpenManus：614 stars，仅 1 commit，页面仅含迁移声明
- 相关项目：OpenManus-RL（github.com/OpenManus/OpenManus-RL，4.1k stars，590 forks，Apache-2.0，328 commits，更新于 May 5 2026）

# README.md（英文）核心原文

## 定位声明

"Manus is incredible, but OpenManus can achieve any idea without an *Invite Code* 🛫!"

"Our team members @Xinbin Liang and @Jinyu Xiang (core authors), along with @Zhaoyang Yu, @Jiayi Zhang, and @Sirui Hong, we are from @MetaGPT. The prototype is launched within 3 hours and we are keeping building!"

"It's a simple implementation, so we welcome any suggestions, contributions, and feedback!"

"We're also excited to introduce OpenManus-RL, an open-source project dedicated to reinforcement learning (RL)-based (such as GRPO) tuning methods for LLM agents, developed collaboratively by researchers from UIUC and OpenManus."

## 安装

- 方式一 conda：`conda create -n open_manus python=3.12` → `git clone https://github.com/FoundationAgents/OpenManus.git` → `pip install -r requirements.txt`
- 方式二 uv（推荐）：`uv venv --python 3.12` → `uv pip install -r requirements.txt`
- 浏览器自动化（可选）：`playwright install`

## 配置

"OpenManus requires configuration for the LLM APIs it uses."
- 创建 `config/config.toml`（从 config.example.toml 复制）
- 默认配置：`[llm] model = "gpt-4o", base_url = "https://api.openai.com/v1", api_key = "sk-...", max_tokens = 4096, temperature = 0.0`
- 可选 `[llm.vision]` 独立视觉模型配置

## 快速启动

- `python main.py` → "Then input your idea via terminal!"
- "For MCP tool version, you can run: `python run_mcp.py`"
- "For unstable multi-agent version, you also can run: `python run_flow.py`"

## 自定义多智能体

"Currently, besides the general OpenManus Agent, we have also integrated the DataAnalysis Agent, which is suitable for data analysis and data visualization tasks."
- config.toml `[runflow] use_data_analysis_agent = true`（默认关闭）
- 依赖：app/tool/chart_visualization/README.md 安装指南

## 致谢（基础依赖）

"Thanks to anthropic-computer-use, browser-use and crawl4ai for providing basic support for this project!"
"Additionally, we are grateful to AAAJ, MetaGPT, OpenHands and SWE-agent."
"We also thank stepfun(阶跃星辰) for supporting our Hugging Face demo space."

## 赞助

"Thanks to PPIO for computing source support."

## 引用（Zenodo）

@misc{openmanus2025, author = {Xinbin Liang and Jinyu Xiang and Zhaoyang Yu and Jiayi Zhang and Sirui Hong and Sheng Fan and Xiao Tang and Bang Liu and Yuyu Luo and Chenglin Wu}, title = {OpenManus: An open-source framework for building general AI agents}, year = {2025}, publisher = {Zenodo}, doi = {10.5281/zenodo.15186407} }

# README_zh.md（中文）核心原文

- "Manus 非常棒，但 OpenManus 无需邀请码即可实现任何创意 🛫！"
- "我们的团队成员 Xinbin Liang 和 Jinyu Xiang（核心作者），以及 Zhaoyang Yu、Jiayi Zhang 和 Sirui Hong，来自 MetaGPT 团队。我们在 3 小时内完成了开发并持续迭代中！"
- "这是一个简洁的实现方案，欢迎任何建议、贡献和反馈！"
- "我们也非常高兴地向大家介绍 OpenManus-RL，这是一个专注于基于强化学习（RL，例如 GRPO）的方法来优化大语言模型（LLM）智能体的开源项目，由来自 UIUC 和 OpenManus 的研究人员合作开发。"
- 安装/配置/启动与英文版一致（python main.py 终端输入创意；run_mcp.py MCP 工具版本；run_flow.py 不稳定的多智能体版本）
- "目前除了通用的 OpenManus Agent, 我们还内置了 DataAnalysis Agent，适用于数据分析和数据可视化任务"
- "感谢 PPIO 提供的算力支持。PPIO派欧云：一键调用高性价比的开源模型API和GPU容器"
- "特别感谢 anthropic-computer-use 和 browser-use 为本项目提供的基础支持！此外，我们感谢 AAAJ，MetaGPT，OpenHands 和 SWE-agent. 我们也感谢阶跃星辰 (stepfun) 提供的 Hugging Face 演示空间支持。"

# 仓库文件结构（2026-08-04 抓取）

## 根目录
- main.py（单 agent 入口）、run_flow.py（多 agent 入口）、run_mcp.py（MCP 客户端入口）、run_mcp_server.py（MCP 服务端）、sandbox_main.py（沙箱入口）、setup.py、requirements.txt
- config/（config.example.toml）、app/、examples/、protocol/a2a/、tests/sandbox/、workspace/、Dockerfile
- README.md / README_zh.md / README_ko.md / README_ja.md、LICENSE（MIT）、CODE_OF_CONDUCT.md

## app/ 目录
- agent/：base.py, react.py, toolcall.py, manus.py, browser.py, data_analysis.py, swe.py, mcp.py, sandbox_agent.py
- flow/（多 agent 流程）、mcp/、prompt/、sandbox/、tool/、daytona/（Daytona 云沙箱集成）、utils/
- bedrock.py（AWS Bedrock 支持）、config.py、llm.py、schema.py、logger.py、exceptions.py

## app/tool/ 工具集
- ask_human.py（人工询问）、base.py、bash.py（shell 执行）、browser_use_tool.py（browser-use 浏览器操作）、computer_use_tool.py（anthropic-computer-use 计算机操作）、crawl4ai.py（crawl4ai 网页爬取）、create_chat_completion.py（LLM 子调用）、file_operators.py（文件操作）、mcp.py（MCP 工具）、planning.py（规划）、python_execute.py（Python 执行）、str_replace_editor.py（字符串替换编辑）、terminate.py（终止）、tool_collection.py（工具集合）、web_search.py（网络搜索）
- chart_visualization/（图表可视化，DataAnalysis Agent 依赖）、search/、sandbox/

# 原仓库迁移声明（mannaandpoem/OpenManus 页面）

"The OpenManus project has moved. For the latest source code and information, please visit its new official repository: https://github.com/FoundationAgents/OpenManus. An archived version of the project is also available here: https://github.com/mannaandpoem/OpenManus_Archive"

# 搜索定位记录

- 引擎：Bing 国内版 + GitHub 仓库搜索，2026-08-04
- 搜索词："OpenManus github Manus open source replication" / "OpenManus"
- 候选结果：FoundationAgents/OpenManus（57.9k）、mannaandpoem/OpenManus（614，已迁移）、henryalps/OpenManus（921，独立复刻）、OpenManus/OpenManus-RL（4.1k）、iszmxw/OpenManus-Docker（32）、Shybert-AI/OpenManus-WebUI（222）
- 另有 openmanus.github.io 官网、知乎/CSDN 部署文章、aiho.net 深度评测（2026-07-04，抓取时证书错误未成功）

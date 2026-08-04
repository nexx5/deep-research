# raw-S019 — hyperresearchbench 仓库原文存档

## 抓取元信息

| 字段 | 值 |
|---|---|
| source_id | S019 |
| 仓库 | jordan-gibbs/hyperresearchbench |
| 主 URL | https://github.com/jordan-gibbs/hyperresearchbench |
| 访问日期 | 2026-08-04 |
| 抓取通道 | GitHub API（api.github.com，webfetch/Invoke-RestMethod）+ raw.githubusercontent.com + Tavily API（socks5://127.0.0.1:4040） |
| 采集档位 | deep |
| 利益相关声明 | 本仓库为 hyperresearch（jordan-gibbs/hyperresearch）官方附属基准 harness，作者同属 jordan-gibbs；非第三方独立验证来源 |

## 一、仓库元数据（GitHub API，2026-08-04 抓取）

- full_name: jordan-gibbs/hyperresearchbench
- description: "DeepResearch-Bench runner for Claude Code agents. Agent-agnostic harness for testing any Claude Code research workflow against the 100-query DRB benchmark."
- created_at: 2026-05-04T15:09:28Z
- updated_at: 2026-05-14T01:55:33Z
- pushed_at: 2026-05-04T15:20:24Z（与创建同日，无后续提交）
- stargazers_count: 0
- forks_count: 1
- open_issues_count: 0
- size: 17（KB）
- language: Python
- license: MIT
- default_branch: main
- topics: 空
- 目录树（main，GitHub API git/trees/main?recursive=1）：
  - .gitignore
  - LICENSE
  - README.md
  - DeepResearch-Bench/grade.sh
  - DeepResearch-Bench/harness.py
  - DeepResearch-Bench/results/.gitkeep
  - DeepResearch-Bench/setup.sh

## 二、README.md 全文（GitHub API readme endpoint 抓取并解码，2026-08-04）

```markdown
# hyperresearchbench

**Reproduction harness for hyperresearch's [DeepResearch-Bench](https://github.com/Ayanami0730/deep_research_bench) score.**

Runs the 100-query DRB benchmark against [hyperresearch](https://github.com/jordan-gibbs/hyperresearch) on Claude Code, full tier (16-step pipeline with adversarial review), Opus 4.7. Outputs a JSONL file ready for the upstream RACE + FACT evaluator.

## Stack

| Layer | Model | Role |
|---|---|---|
| Orchestrator | Opus 4.7 | Tier classification, pipeline routing, synthesis planning |
| Critics (4×) | Opus 4.7 | Dialectic, depth, width, instruction adversarial review |
| Synthesizer | Opus 4.7 | Two-pass write from 3 angle-specific drafts |
| Patcher + polish auditor | Opus 4.7 | Tool-locked `[Read, Edit]` → surgical hunks only |
| Loci-analysts, depth-investigators, draft sub-orchestrators, source-analyst | Sonnet 4.6 | Parallel reading + position-committing |
| Fetchers | Haiku 4.5 | URL fetching via crawl4ai, 8–12 in parallel per wave |

Per-query wall-clock: **~1.5–2.5 hours** for full tier. Per-query cost: **~$60–120**.

## Reproduce

```bash
git clone https://github.com/jordan-gibbs/hyperresearchbench
cd hyperresearchbench/DeepResearch-Bench

# 1. One-command setup. Installs hyperresearch globally, clones upstream
#    DRB, installs Gemini eval deps, downloads the 100 queries.
bash setup.sh

# 2. Smoke test — one query end-to-end (~1.5-2.5 hours, ~$60-120)
python harness.py --query 67          # English, "RL exploration → trajectory planning"
export GEMINI_API_KEY=<your-key>      # Get one at https://aistudio.google.com/apikey
bash grade.sh --limit 1

# 3. Full run (resume-safe; checkpoints to results/claude-research.jsonl)
python harness.py                     # ~6-10 days wall-clock for 100 queries
bash grade.sh                         # RACE + FACT
```

Reproduction expectations:

- **`hyperresearch --version`** must report `0.8.5` or later
- **`claude --version`** must work and be authenticated
- **Python 3.11, 3.12, or 3.13** (3.14 unsupported pending upstream Crawl4AI fix; setup.sh refuses to run on 3.14)
- A Gemini API key (Gemini-2.5-Pro for RACE, Gemini-2.5-Flash for FACT)

## What the harness does per query

1. Mirrors your project's `.claude/` and `CLAUDE.md` into a fresh `runs/query_<id>/` subdir
2. Runs `claude -p "Use the /hyperresearch skill on the FULL tier..."` with the benchmark prompt
3. The agent in that subdir auto-bootstraps a hyperresearch vault (step 0), then walks the 16-step pipeline:

   ```
   1. decompose                    9.  evidence digest
   2. width sweep (40-100 sources) 10. triple-draft (3 parallel)
   3. contradiction graph          11. synthesize (Opus, two-pass)
   4. loci analysis                12. 4 adversarial critics (parallel)
   5. depth investigation (K par.) 13. gap-fetch
   6. cross-locus reconcile        14. patcher (Read+Edit only)
   7. source tensions              15. polish (Read+Edit only)
   8. corpus critic                16. readability audit
   ```

4. Reads the resulting `research/notes/final_report_<vault_tag>.md`
5. Appends one JSON record per query to `results/claude-research.jsonl`

## Output JSONL schema

```json
{
  "id": 67,
  "language": "en",
  "prompt": "Summarize recent research progress in reinforcement learning...",
  "article": "<the full final_report.md content>",
  "model": "opus",
  "prompt_tokens": 8423,
  "completion_tokens": 12017,
  "duration_seconds": 9182.4,
  "timestamp": "2026-04-29T19:32:45Z"
}
```

The schema matches the upstream DRB evaluator's expected format. `grade.sh` copies the file into `deep_research_bench/data/results/` and invokes `python -m race.eval` and `python -m fact.eval` (FACT scrapes citation URLs to verify them).

## Single-query smoke test details

```bash
python harness.py --query 67 --timeout 10800
```

`--query 67` is the canonical English query for smoke-testing — it's the one we used as our public sample report at https://github.com/jordan-gibbs/hyperresearch/blob/main/example-reports/rl-exploration-trajectory-planning.md (graded 58.3/100 in the V8.3 stratified pilot). Anyone reproducing should expect to land within ±2 points of that score.

`--timeout 10800` is 3 hours — defensive, since full tier on a research-heavy query can run long when fetcher waves hit slow sources.

After the run, `runs/query_67/research/notes/final_report_*.md` is the deliverable. `results/claude-research.jsonl` has the JSONL entry.

## Resuming after interruption

The harness is resume-safe via `--resume`. Reads `results/claude-research.jsonl`, builds a set of completed query IDs, skips them on the next run.

```bash
python harness.py --resume
```

Worth knowing:

- **API rate limits / quotas** — if Anthropic billing pauses mid-run, fix the billing, then `python harness.py --resume`. Already-completed queries are not re-run.
- **Timeouts** — if a query hits `--timeout`, it's NOT recorded as completed. The next `--resume` will retry it. Bump `--timeout` if certain queries consistently hit the cap.
- **Manual recovery** — every per-query subdir at `runs/query_<id>/` is a complete hyperresearch project (vault, sources, scaffold, drafts, critic findings). If a query crashed mid-pipeline (e.g., during step 15), you can `cd` in and inspect / manually finish.

## CLI reference

```
python harness.py --setup                # Download benchmark queries
python harness.py                        # Run all 100 queries
python harness.py --limit N              # Run only the first N
python harness.py --query <id>           # Run a specific query (1-100)
python harness.py --lang en | --lang zh  # Filter by language (50 each)
python harness.py --resume               # Skip queries already in JSONL
python harness.py --model opus           # Default; can also pass sonnet or haiku
python harness.py --timeout 10800        # Per-query timeout in seconds (default 3600)
python harness.py --output run-name      # Write to results/run-name.jsonl

bash grade.sh                            # RACE + FACT on results/claude-research.jsonl
bash grade.sh my-run                     # Grade results/my-run.jsonl
bash grade.sh --skip-fact                # RACE only (no citation web-scraping)
bash grade.sh --limit 5                  # Grade first 5 entries only
```

## Hyperresearch's published score

V8.3 stratified pilot (n = 9 queries, full reference-strength distribution): **57.77 average overall**, beating xiaoyi (DRB #1 on the public leaderboard at the time) by 0.77 points.

Full 100-query reproduction is what this harness exists to enable.

## License

MIT. The upstream [DeepResearch-Bench](https://github.com/Ayanami0730/deep_research_bench) repo (cloned by `setup.sh` into `DeepResearch-Bench/deep_research_bench/`) is licensed separately by its authors.
```

## 三、harness.py 全文（raw.githubusercontent.com 抓取，2026-08-04）

```python
#!/usr/bin/env python3
"""DeepResearch-Bench harness for hyperresearch on Claude Code.

Runs the 100 benchmark queries through `claude -p` invoking the
`/hyperresearch` skill on its full tier (16-step pipeline with
adversarial review), captures the resulting research reports, and
writes JSONL ready for RACE/FACT evaluation.

This is the canonical reproduction harness for hyperresearch's
DeepResearch-Bench leaderboard score. To reproduce: run
`bash setup.sh` then `python harness.py` (or `bash run.sh` which
wraps both). Each query runs on Opus 4.7 (orchestrator + critics +
synthesizer + patcher), Sonnet 4.6 (loci-analysts, depth-investigators,
draft sub-orchestrators, source-analyst), and Haiku 4.5 (fetchers).
"""
# [实现细节节选，全文见下方关键常量与函数]

QUERY_URL = (
    "https://raw.githubusercontent.com/Ayanami0730/deep_research_bench/main/"
    "data/prompt_data/query.jsonl"
)

RESEARCH_PROMPT = """\
Use the `/hyperresearch` skill on the FULL tier (the 16-step pipeline with adversarial review) to research this topic and write a comprehensive report with inline citations:

{prompt}

When step 1 (decompose) classifies the query, override `pipeline_tier` to `"full"` regardless of the query length — this is a benchmark run that requires the full pipeline.

Save your final report to `research/notes/final_report_<vault_tag>.md` (relative to the current working directory). The harness reads the most-recently-modified file matching `research/notes/final_report*.md`.
"""
```

harness.py 关键实现逻辑（抓取全文摘要）：
- `download_queries()`：从上游 USTC DRB 仓库拉取 query.jsonl（"100 PhD-level prompts, 50 zh + 50 en"）
- `_setup_run_dir()`：将父项目的 `.claude/` 和 `CLAUDE.md` 镜像进每个 run 子目录（"the subdir needs to inherit whatever Claude Code skills + agents + hooks the parent project has installed — that's what determines the research workflow under test"）
- `run_query()`：执行 `claude -p <prompt> --model opus --dangerously-skip-permissions --no-session-persistence --output-format stream-json --verbose`；timeout 默认 3600；超时后仍尝试读报告
- `_read_report()`：读取 `research/notes/final_report*.md` 中最新的文件（"Save path is the v0.8.5+ vault_tag-suffixed form"）
- token 统计：从 stream-json 输出行中 `usage.input_tokens` / `usage.output_tokens` 累加
- JSONL 输出字段：id, language, prompt, article, model, prompt_tokens, completion_tokens, duration_seconds, timestamp
- `--resume`：读取输出 JSONL 中的已完成 id，跳过不重跑

## 四、grade.sh 全文（raw.githubusercontent.com 抓取，2026-08-04）

```bash
#!/bin/bash
# Run RACE + FACT evaluation on harness output JSONL using the upstream
# DeepResearch-Bench evaluator.
#
# Prerequisites:
#   1. bash setup.sh   (clones upstream DRB + installs deps)
#   2. python harness.py --limit N   (generates results/<output>.jsonl)
#   3. export GEMINI_API_KEY=<your-key>   (Gemini-2.5-Pro for RACE, 2.5-Flash for FACT)
```

grade.sh 关键逻辑：
- 前置校验：需已克隆上游 DRB（`deep_research_bench/` 目录存在）、存在结果 JSONL、设置 `GEMINI_API_KEY` 或 `GOOGLE_API_KEY`
- 步骤1 RACE：`python -m race.eval --target <RESULTS_NAME>.jsonl`——"RACE — report quality (comprehensiveness, insight, instruction-following, readability)"，"Gemini-2.5-Pro pairwise judge"
- 步骤2 FACT：`python -m fact.eval --target <RESULTS_NAME>.jsonl`——"FACT — citation accuracy (effective citations / total citations)"，"Gemini-2.5-Flash citation grader, web-scrapes URLs"；`--skip-fact` 可跳过
- 将结果 JSONL 复制到 `deep_research_bench/data/results/`，评分后把 `_score.json` 拉回本地 results 目录
- score 输出字段：overall, comprehensiveness, insight, instruction_following, readability

## 五、setup.sh 全文（GitHub API contents endpoint 抓取并解码，2026-08-04）

```bash
#!/bin/bash
# One-command setup: install hyperresearch globally, clone the upstream
# DeepResearch-Bench repo (for the RACE evaluator), install Gemini eval
# deps, and download the 100 benchmark queries.
#
# Prerequisites:
#   - Python 3.11, 3.12, or 3.13 (NOT 3.14 — Crawl4AI's lxml pin)
#   - Claude Code CLI installed and authenticated (`claude --version`)

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
DRB_REPO="$HERE/deep_research_bench"
DRB_URL="https://github.com/Ayanami0730/deep_research_bench.git"

# Step 0: Verify Python version
PY_MAJ=$(python -c "import sys; print(sys.version_info.major)")
PY_MIN=$(python -c "import sys; print(sys.version_info.minor)")
if [ "$PY_MAJ" -ne 3 ] || [ "$PY_MIN" -lt 11 ] || [ "$PY_MIN" -ge 14 ]; then
    echo "[ERROR] Python ${PY_MAJ}.${PY_MIN} not supported. Use 3.11, 3.12, or 3.13."
    echo "        (Crawl4AI's lxml~=5.3 pin has no cp314 wheels yet.)"
    exit 1
fi

# Step 1: Install hyperresearch + run global install (skill + agents → ~/.claude/)
python -m pip install --upgrade hyperresearch
hyperresearch install --global

# Step 2: Clone upstream DRB if not present (RACE evaluator + reference data)
git clone --depth 1 "$DRB_URL" "$DRB_REPO"

# Step 3: Install Gemini eval deps
python -m pip install --upgrade \
    google-generativeai \
    requests \
    tqdm \
    beautifulsoup4 \
    lxml

# Step 4: Download benchmark queries
python "$HERE/harness.py" --setup
```

## 六、Tavily 搜索结果片段（hyperresearch 主仓库 README 关键声明，2026-08-04 抓取）

来源：https://github.com/jordan-gibbs/hyperresearch（S004 已采录主仓库；此处为 Tavily content 字段提取的关键片段，用于核实"领先"声称的官方措辞）

> "Hyperresearch turns Claude Code into a deep research agent: one that currently leads the DeepResearch-Bench RACE leaderboard (benchmarked internally). A tier-adaptive 16-step pipeline takes one prompt and produces an adversarially-audited report with full source provenance."

> "DeepResearch-Bench top-5 hyperresearch leads the chart ahead of Grep Deep Research, Cellcog Max, nvidia-aiq, Gemini Deep Research, and OpenAI Deep Research"

> "Forward-looking projection from a stratified pilot against the DeepResearch-Bench leaderboard snapshot (). Third party validation is pending."

（注：Tavily 搜索结果还返回了 arXiv 2510.14240 LiveResearchBench——"A Live Benchmark for User-Centric Deep Research in the Wild"，100 个专家任务 + DeepEval 评估套件，与本基准生态相关，见线索清单。）

## 七、价值判断记录

- extraction_level: deep（评测 harness/项目拆解类：有架构拆解、评估器调用链、成本数据、官方声称分层）
- article_type: 项目拆解/基准 harness 文档
- 关键观察（如实记录，不评判）：
  1. 本仓库是 hyperresearch 官方附属的"复现 harness"，README 自定位为 "Reproduction harness for hyperresearch's DeepResearch-Bench score"
  2. 任务集与评估器全部来自第三方基准 USTC DeepResearch-Bench（Ayanami0730/deep_research_bench）
  3. 官方公布的 57.77 分为 V8.3 stratified pilot（n=9）结果，官方 README 同时声明完整 100-query 复现正是本 harness 存在的目的
  4. hyperresearch 主仓库 README 官方措辞：领先声称标注 "benchmarked internally"，且自述 "Third party validation is pending"
  5. 仓库 0 stars / 1 fork / 无后续提交（2026-05-04 创建即最后推送）

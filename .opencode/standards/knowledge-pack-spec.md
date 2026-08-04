# 知识包目录结构标准

> 版本：1.0
> 日期：2026-07-06
> 定位：所有知识包的统一目录结构标准，保证可移植性

## 目录结构

```
<project>/knowledge-pack/
  manifest.json              # 知识包清单（元数据+统计）
  claims.jsonl               # 断言（流式，每行一条JSON）
  debates.jsonl              # 争议议题
  schools.jsonl              # 流派
  concepts.jsonl             # 概念
  relations.jsonl            # 关系
  source-leads.jsonl         # 线索池
  evidence/                  # 证据文件（真相源）
    raw-S*.md                # 原始捕获
    采录-S*.md               # 采录（断言+证据链）
    分析-A*.md               # 单源分析
  index/                     # 索引层（影子，可重建）
    knowledge.db             # SQLite索引（FTS5+关系表）
    qmd-index/               # qmd语义索引（可重建）
  views/                     # 视图层（从索引派生）
    L0-知识概貌.md           # L0知识概貌
    L1-*.md                  # L1专题视图
  batch-state.json           # 检查点（可中断恢复）
```

## 分层原则

| 层 | 目录 | 性质 | 可重建 |
|---|---|---|---|
| 真相源 | evidence/ + *.jsonl | 只增不改 | ❌ 不可重建 |
| 索引层 | index/ | 影子，可重建 | ✅ 从真相源重建 |
| 视图层 | views/ | 派生，可重建 | ✅ 从索引层重建 |
| 状态层 | batch-state.json | 运行时状态 | ❌ 不可重建（但可从文件推断） |

## 可移植性规则

1. 拷贝 `knowledge-pack/` 目录到任何位置即可用
2. `index/knowledge.db` 和 `index/qmd-index/` 丢失不致命，可从 `evidence/` + `*.jsonl` 重建
3. `views/` 丢失不致命，可从 `index/` 重建
4. `batch-state.json` 丢失需手动恢复（从jsonl行数推断进度）

## 文件命名规范

| 文件 | 命名规则 | 示例 |
|---|---|---|
| raw | raw-S{四位序号}.md | raw-S0001.md |
| 采录 | 采录-S{四位序号}.md | 采录-S0001.md |
| 分析 | 分析-A{四位序号}.md | 分析-A0001.md |
| claim_id | CL{五位序号} | CL00001 |
| debate_id | DB{四位序号} | DB0001 |
| school_id | SC{三位序号} | SC001 |
| lead_id | LD{六位序号} | LD000001 |

## manifest.json 字段

```json
{
  "pack_version": "1.0",
  "schema_version": "1.0",
  "project": "项目名",
  "domain": "领域标签",
  "created": "ISO日期",
  "updated": "ISO日期",
  "stats": {
    "sources": 0,
    "claims": 0,
    "debates": 0,
    "schools": 0,
    "concepts": 0
  },
  "index_layers": {
    "sqlite_fts5": true,
    "qmd": false,
    "graph": true
  },
  "retrieval_interface": "kb-retriever@1.0"
}
```

## JSONL 格式约定

- 每行一条 JSON 对象，UTF-8 无 BOM
- 换行符 `\n`（LF）
- 追加写入，不修改已有行
- 字段顺序不保证，解析时按 key 取值
- Schema 定义在 `.opencode/standards/jsonl-schemas/` 下

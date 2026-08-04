# 搜索适配器接口标准

> 版本：1.0
> 日期：2026-07-06
> 定位：搜索能力可插拔接口，调度器按策略选择引擎组合

## 适配器定义格式

每个适配器是一个YAML配置块，注册到 `.opencode/standards/search-adapters/` 目录：

```yaml
# .opencode/standards/search-adapters/baidu.yaml
adapter:
  name: baidu
  type: mcp              # mcp | http | local | browser
  capabilities:          # 能力标签
    - keyword
    - general
  rate_limit:
    requests_per_min: 30
    adaptive: false
  config:
    mcp_server: search-engine-mcp
    proxy: http://127.0.0.1:4040
  enabled: true
```

## 能力标签

| 标签 | 含义 | 适用场景 |
|---|---|---|
| keyword | 关键词搜索 | 通用搜索 |
| general | 通用信息 | 大多数调研 |
| academic | 学术文献 | 论文溯源、学术调研 |
| fulltext | 全文检索 | 本地文档 |
| semantic | 语义检索 | 模糊匹配 |
| community | 社区反馈 | 用户评价、社区讨论 |
| screenshot | 截图/可视化 | UI调研 |
| dynamic | 动态页面 | SPA/反爬站点 |

## 已有适配器

| 适配器 | 类型 | 能力 | 状态 |
|---|---|---|---|
| baidu | mcp | keyword, general | ✅ |
| bing | mcp | keyword, general | ✅ |
| google | mcp | keyword, general | ✅ |
| duckduckgo | mcp | keyword, general | ✅ |
| searxng | http | keyword, general | ✅ |
| tavily | http | keyword, general | ✅ |
| qmd | local | fulltext, semantic | ✅ |
| arxiv | http | keyword, academic | ✅ |
| openalex | http | keyword, academic | ✅ |
| semantic_scholar | http | keyword, academic | ✅ |

## 待加适配器

| 适配器 | 类型 | 能力 | 批次 |
|---|---|---|---|
| pubmed | http | keyword, academic | 后续 |
| browser-act | local | dynamic, screenshot | 批次4 |
| redfox | local | community | 批次4 |

## 调度器选择规则

调度器（强模型）根据 `strategy_tags` 和上一轮发现内容选择适配器组合：

```yaml
# 选择策略示例
strategy_tags:
  academic_research:        # 学术调研
    primary: [arxiv, openalex, semantic_scholar, google]
    fallback: [bing, searxng]
  
  community_feedback:       # 社区反馈
    primary: [redfox, browser-act, baidu]
    fallback: [google]
  
  general_research:         # 通用调研
    primary: [baidu, bing, duckduckgo]
    fallback: [searxng, tavily]
  
  local_search:             # 本地知识包检索
    primary: [qmd]
    fallback: []
```

## STORM agentic 诊断五类（叠加到四象限收敛上）

调度器在每轮搜索后诊断结果质量，调整下一轮引擎组合：

| 诊断类型 | 症状 | 调整 |
|---|---|---|
| 结果不足 | 返回<3条相关结果 | 换引擎或扩展关键词 |
| 结果冗余 | 多引擎返回相同结果 | 减少并行引擎数 |
| 质量不足 | 结果相关度低 | 切换到学术/专用引擎 |
| 时效不足 | 结果过旧 | 加时间过滤，优先最新 |
| 视角不足 | 结果单一视角 | STORM多视角补搜 |

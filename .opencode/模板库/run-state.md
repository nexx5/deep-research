# 运行状态：[项目名]

> 运行时累积状态。随批次更新，与 `project.config.md`（静态定义，PLAN_REVIEW 后冻结）分离。
> 机器读 `knowledge-pack/batch-state.json`，本文件供 agent/人类读 + 采录员做去重 + 调研员关键词追加。
> **本文件不替代 batch-state.json**——还原点以 batch-state.json 为准，本文件是人类/agent 可读镜像。

---

## 执行参数

```yaml
execution:
  parallel_discover_limit: 8
  failure_fallback_limit: 3
  mode: continuous
```

---

## 搜索参数（每轮可变）

```
当前轮参数 = {
  round: 0              本轮轮次（agent 每轮自动 +1）
  breadth: 3-10         本轮搜索宽度
  depth: 1-5            递归深度
  threshold: 0.3        当前轮采集阈值（动态变化）
  sources: [bing, searxng, baidu]   本轮启用搜索源（学术加 arxiv, openalex）
  exclude: []           排除关键词
  user_notes: ""        用户补充说明
}
```

---

## 批次进度

- **当前批次：** batch [编号]
- **已有采录：** [N 篇]
- **模型配比：** [如 deepseek-v4-flash x8 并发；合并用 glm-5.2]
- **上批次结论摘要：** [一句话]

---

## focus_keywords / explore_keywords（按批次累加，调研员追加，不写回 project.config）

> 调研员每批次从分析线索中追加关键词到本段（累加不覆盖）。去重时与已采列表+id_registry 比对。

### [batch 编号]新增
- 关键词1
- 关键词2

---

## dead_ends（已穷尽路径，留作饱和判定参考）

| 代号 | 线索/方向 | 处理 |
|---|---|---|
| DE001 | [搜索词/URL] | unreachable: [原因] / abandoned: [理由] / captured: [说明] |

---

## 用户阶段性意见（运行期注入的临时定义/售前定义/阶段性成果，不写 project.config）

- [日期] [意见/定义摘要]
> 例如："用户采纳售前定义：知识=不确定性最低的稳定描述"

---

## 备注

[运行时其他需要沉淀但不属于 project.config 静态定义的事项]
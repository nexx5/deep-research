# Task Queue

> 调研员的核心驱动。主 agent 循环：读队列 → 派发 sub-agent → 收摘要 → 更新队列。
> 任务类型：PLAN_REVIEW（方案确认）、DISCOVER（搜索抓取）、EXTRACT（提取标注）、SYNTHESIZE（聚类对撞合成）。

---

## 状态摘要

| 指标 | 值 |
|------|-----|
| 运行模式 | plan_review |
| 总任务数 | 2 |
| pending | 1 |
| pending_approval | 1 |
| in_progress | 0 |
| completed | 0 |
| failed | 0 |
| blocked | 0 |
| 未分析采录数 | 0 |

---

## 任务队列

| ID | 类型 | Source | 描述 | 优先级 | 状态 | 依赖 |
|----|------|--------|------|--------|------|------|
| P001 | PLAN_REVIEW | project | 生成调研方案草案并等待用户确认 | H | pending | - |
| D001 | DISCOVER | project | 用户确认方案后执行初始采集 | H | pending_approval | P001 |

---

## 线索生成任务

| ID | 类型 | 描述 | 来源 | 优先级 | 状态 |
|----|------|------|------|--------|------|
| | | | | | |

---

## 已完成任务

| ID | 类型 | Source | 描述 | 完成时间 | 产出 |
|----|------|--------|------|----------|------|
| | | | | | |

---

## 队列运行规则

1. `plan_status != approved` 时，只允许执行 PLAN_REVIEW，不得执行 DISCOVER/EXTRACT/SYNTHESIZE。
2. 用户确认方案后，将 `plan_status` 改为 `approved`，并将 D001 从 `pending_approval` 改为 `pending`。
3. 选任务：H > M > L。同优先级内按 ID 顺序。
4. DISCOVER 完成后自动生成对应 EXTRACT 任务。
5. EXTRACT 完成条件：采录检查点通过。
6. SYNTHESIZE 触发：未分析采录 >= 5 或采集暂歇。
7. 线索处理：sub-agent 返回线索 → 主 agent 去重 → 生成 DISCOVER 任务入队。
8. 去重：同名/同址/同关键词的线索不重复添加。
9. 饱和判定：队列空 + 无缺口 + 无新线索 + 子问题全覆盖。
10. 每次队列变更后更新本文件。

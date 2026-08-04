# 深度档采录模板

> 用途：对论文解读/项目拆解/对比评测类文章做深度断言提取
> 模型：弱模型（qwen3.6-27b / deepseek-v4-flash）
> 约束：详细提取模板，减少自由发挥

## 输入

- 文章全文内容
- 文章元数据（title, author, date, url）

## 提取要求

从文章中提取原子化断言，每条断言必须包含完整证据链。

### 断言提取规范

1. 每篇A*通常产出2-8条断言，不要过度提取
2. 每条断言必须包含：
   - statement：简洁的概念关系，不是完整句子
   - boundary：在什么条件下成立（必填，不允许空）
   - characteristics：特点标签（必填，用于跨源关联）
   - evidence：原文摘录+定位（必填，证据链不能空）
   - confidence：0-1（多源支撑+边界明确→高；单源/边界模糊→低）
   - possible_relations：基于本文推断的可能关联

3. 断言的statement格式：{主体} {关系} {客体}
   - 例：向量检索 适用于 语义模糊匹配场景
   - 例：纯文件方案 弱于 向量检索 在语义匹配上

### boundary填写规范

- boundary是"在什么条件下成立"，不是结论本身
- 好的boundary："语义模糊匹配场景"、"小规模知识库(<1万文档)"、"零依赖部署环境"
- 坏的boundary："在某些情况下"、"视具体需求而定"（太模糊）

### characteristics标注规范

只标注文章明确涉及的技术/方案特点：
- 存储介质：向量库 / 纯文件 / 知识图谱 / 模型参数 / 混合
- 检索方式：语义匹配 / 精确匹配 / 图遍历 / grep
- 依赖：需embedding / 零依赖 / 需数据库 / 需GPU
- 规模：小规模适用 / 大规模适用 / 可扩展

### possible_relations推断规范

基于本文内容推断，不读全局知识包：
- "与{纯文件方案}可能{对立}，因为本文主张向量检索的语义优势"
- "与{知识图谱方案}可能{互补}，因为图谱擅长关系推理而向量擅长语义匹配"
- 不确定时标注"可能"，不要绝对化

## 输出格式

按采录-S*.md格式输出。**key_claims 必须用 SPO 表格格式，唯一权威见 standards/extraction-format.md，禁止 bullet 前缀、禁止 CL 预占位。** 完整包含 key_claims(SPO表格) + evidence + characteristics + possible_relations + discovered_leads 段。

### key_claims 段格式（深量档必填，2-8 条）

```markdown
## key_claims

| # | subject | predicate | object | boundary | confidence | sources | characteristics |
|---|---|---|---|---|---|---|---|
| 1 | 知识图谱 | 优于 | 纯向量检索 | 需要跨步追踪信息变化的多跳推理 | H | S0048 | 知识图谱,多跳推理 |
| 2 | 向量检索 | 适用于 | 语义模糊匹配 | 语义模糊匹配场景，不需精确ID匹配 | M | S0048 | 向量检索,语义匹配 |
```

字段约定：
- `#`：表内序号，不是 claim_id（claim_id 由知识管理员 ingest 时统一分配）
- `subject/predicate/object`：简洁概念/关系/客体，**不是完整句子**
- `boundary`：在什么条件下成立（必填，缺失时写"未明确"也比空好）
- `confidence`：H=多源交叉 / M=单源可信 / L=推测二手（或 0.0-1.0）
- `sources`：来源 S-id，来自本文件 frontmatter source_id
- `characteristics`：特点标签逗号分隔（跨源关联依赖，必填）

### 断言提取规范

1. 每篇A*通常产出2-8条断言，不要过度提取
2. 每条断言必须包含完整证据链（evidence 段详写）
3. statement 格式 = subject+predicate+object 拆三原子列（不是一句话）
4. boundary 是"在什么条件下成立"，不是结论本身
5. characteristics 只标文章明确涉及的特点（存储介质/检索方式/依赖/规模等）

boundary 好示例："语义模糊匹配场景"、"小规模知识库(<1万文档)"、"零依赖部署环境"
boundary 坏示例："在某些情况下"、"视具体需求而定"（太模糊）

characteristics 标注：
- 存储介质：向量库 / 纯文件 / 知识图谱 / 模型参数 / 混合
- 检索方式：语义匹配 / 精确匹配 / 图遍历 / grep
- 依赖：需embedding / 零依赖 / 需数据库 / 需GPU
- 规模：小规模适用 / 大规模适用 / 可扩展

possible_relations：基于本文内容推断，不读全局知识包——section 另行展开（不混入表格）。

## 禁止行为

- 不要用 bullet + `**CL{id}**` 前缀格式（已废弃，v2.0 统一 SPO 表格）
- 不要在表格里预占 CL 编号（CL id 由知识管理员 ingest 分配）
- 不要提取文章未明确陈述的断言（不推理不补充）
- 不要遗漏 boundary（裸观点丢弃）
- 不要遗漏 characteristics（跨源关联依赖这个）
- 不要过度提取（超过8条断言说明你在拆碎观点，不是提取知识）

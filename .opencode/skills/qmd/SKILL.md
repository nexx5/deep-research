---
name: qmd
description: QMD 本地文档搜索引擎技能。适用于需要索引、搜索和检索 Markdown 文档、知识库、会议记录等文件的场景。当用户需要搜索文档内容、管理文档集合、生成向量嵌入、或使用混合搜索（BM25+向量）时触发。
---

# QMD - Query Markup Documents

QMD 是一个本地文档搜索引擎，结合 BM25 全文搜索和向量语义搜索，所有模型本地运行。

## 基础使用

```bash
# 1. 添加文档集合
qmd collection add <路径> --name <集合名>

# 2. 添加上下文描述（重要！提升搜索质量）
qmd context add qmd://<集合名> "描述信息"

# 3. 生成向量嵌入
qmd embed

# 4. 搜索文档
qmd search "关键词"           # BM25 快速搜索
qmd vsearch "语义查询"        # 向量语义搜索
qmd query "混合查询"          # 混合搜索（慢速重排序需加 --rerank）
```

## 核心工作流

### 集合管理

```bash
# 创建集合
qmd collection add . --name myproject
qmd collection add ~/Documents/notes --name notes --mask "**/*.md"

# 查看/移除/重命名集合
qmd collection list
qmd collection remove <集合名>
qmd collection rename <旧名> <新名>

# 列出集合中的文件
qmd ls <集合名>
qmd ls <集合名>/子目录
```

### 上下文管理

上下文是 QMD 的核心功能，为文档添加描述性元数据以改善搜索结果。

```bash
# 为集合添加上下文
qmd context add qmd://notes "个人笔记和想法"
qmd context add qmd://docs/api "API 文档"

# 添加全局上下文
qmd context add / "项目知识库"

# 查看/移除上下文
qmd context list
qmd context rm qmd://notes/旧路径
```

### 搜索命令

| 命令 | 类型 | 适用场景 |
|------|------|----------|
| `search` | BM25 全文搜索 | 快速关键词匹配 |
| `vsearch` | 向量语义搜索 | 自然语言语义匹配 |
| `query` | 混合搜索 | BM25+向量，需重排序时加 `--rerank` |

```bash
# 基础搜索
qmd search "关键词"
qmd query "复杂查询"

# 限制集合
qmd search "API" -c notes

# 控制结果数量和质量
qmd query -n 10 --min-score 0.3 "查询内容"

# 获取所有匹配
qmd search "关键词" --all --min-score 0.4
```

### 文档检索

```bash
# 按路径获取文档
qmd get "docs/file.md"
qmd get "docs/file.md:50" -l 100  # 从第50行开始，最多100行

# 按 docid 获取（搜索结果中显示）
qmd get "#abc123"

# 批量获取
qmd multi-get "journals/2025-05*.md"
qmd multi-get "doc1.md, doc2.md, #abc123"
```

### 输出格式

为 AI Agent 工作流设计的输出格式：

```bash
# JSON 输出
qmd search "关键词" --json -n 10

# 文件列表输出
qmd query "错误处理" --all --files --min-score 0.4

# Markdown 输出
qmd search --md --full "错误处理"
```

## 高级配置

### 向量嵌入

```bash
# 基础嵌入
qmd embed

# 强制重新嵌入
qmd embed -f

# AST 感知分块（代码文件）
qmd embed --chunk-strategy auto
```

### 多语言支持

对于中文等 CJK 语言，使用 Qwen3-Embedding 模型：

```bash
# Windows PowerShell
$env:QMD_EMBED_MODEL="hf:Qwen/Qwen3-Embedding-0.6B-GGUF/Qwen3-Embedding-0.6B-Q8_0.gguf"

# 重新嵌入
qmd embed -f
```

### GPU 加速

```bash
# 指定 GPU 后端
$env:QMD_LLAMA_GPU="vulkan"  # 或 metal, cuda, false
```

### MCP 服务器

```bash
# 启动 MCP 服务器
qmd mcp

# HTTP 模式
qmd mcp --http                    # localhost:8181
qmd mcp --http --daemon           # 后台运行
qmd mcp stop                      # 停止服务
```

## 索引维护

```bash
# 查看状态
qmd status

# 重新索引
qmd update
qmd update --pull  # 先 git pull 再索引

# 清理缓存
qmd cleanup
```

## 性能提示

- **`qmd query` 默认不启用重排序**，如需更高质量结果请加 `--rerank` 参数
- **重排序耗时**：`--rerank` 需加载重排序模型，首次较慢，后续会使用缓存
- **GPU 加速**：确保 `QMD_LLAMA_GPU` 设置正确

## 评分解读

| 分数 | 相关性 |
|------|--------|
| 0.8 - 1.0 | 高度相关 |
| 0.5 - 0.8 | 中等相关 |
| 0.2 - 0.5 | 部分相关 |
| 0.0 - 0.2 | 低相关性 |

## 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `QMD_LLAMA_GPU` | auto | GPU 后端配置 |
| `QMD_FORCE_CPU` | unset | 强制 CPU 模式 |
| `QMD_EMBED_MODEL` | embeddinggemma | 自定义嵌入模型 |
| `QMD_EDITOR_URI` | vscode | 编辑器链接模板 |

## 数据存储

索引存储在 `~/.cache/qmd/index.sqlite`，使用 SQLite 数据库包含集合配置、文档内容、FTS5 全文索引、向量嵌入、LLM 缓存。

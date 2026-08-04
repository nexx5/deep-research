-- 知识体系索引层 Schema (V2 - 新协议)
-- 文件: knowledge-schema-v2.sql
-- 用途: 定义新协议（MapReduce模式）的知识体系SQLite索引层结构
-- 设计原则: 文件是真相源（claims.jsonl），SQLite是影子索引
-- 与旧schema区别:
--   claims用statement(一句话)替代subject+predicate+object(三元组)
--   claims用source_id(单值)替代sources(JSON数组)
--   claims用characteristics替代concepts
--   claims用confidence(REAL 0-1)替代confidence(TEXT H/M/L)
--   无comparisons/questions/sync_log/claims_fts表

PRAGMA journal_mode=WAL;

-- ============================================================
-- claims 表：断言（知识体系的原子单元）
-- 每条断言 = statement + boundary + source + lifecycle
-- ============================================================
CREATE TABLE IF NOT EXISTS claims (
    id              TEXT PRIMARY KEY,        -- CL00001, CL00002...
    statement       TEXT NOT NULL,            -- 断言陈述（一句话）
    boundary        TEXT,                     -- 边界条件（在什么条件下成立）
    source_id       TEXT,                     -- 来源ID（S001, S002...）
    source_title    TEXT,                     -- 来源标题（冗余，方便展示）
    source_type     TEXT,                     -- 来源类型
    characteristics TEXT,                     -- JSON array，特点标签
    confidence      REAL DEFAULT 0.5,         -- 置信度 0.0-1.0
    school          TEXT,                     -- 学派标签
    extraction_level TEXT,                    -- light/deep
    status          TEXT NOT NULL DEFAULT 'active',  -- active/contested/merged/irrelevant
    opposing        TEXT,                     -- JSON array，对立断言ID列表
    possible_relations TEXT,                  -- JSON array，可能关系（文本描述）
    created         TEXT NOT NULL,            -- ISO date
    updated         TEXT,                     -- ISO date
    -- 向量嵌入（断言级语义检索）
    embedding       TEXT,                     -- JSON array，断言向量
    embedding_model TEXT,                     -- 嵌入模型名
    embedding_at    TEXT                      -- 嵌入时间 ISO格式
);

-- ============================================================
-- sources 表：来源元数据
-- ============================================================
CREATE TABLE IF NOT EXISTS sources (
    id              TEXT PRIMARY KEY,         -- S001, S002...
    title           TEXT NOT NULL,
    source_type     TEXT,                     -- web_page/github_repo/official_doc...
    url             TEXT,
    raw_path        TEXT,                     -- raw-S*.md 相对路径
    extract_path    TEXT,                     -- 采录-S*.md 相对路径
    analysis_path   TEXT,                     -- 分析-A*.md 相对路径
    created         TEXT NOT NULL
);

-- ============================================================
-- concepts 表：概念索引（概念→断言/来源映射）
-- ============================================================
CREATE TABLE IF NOT EXISTS concepts (
    concept         TEXT NOT NULL,
    claim_ids       TEXT,                     -- JSON array of claim_id
    source_ids      TEXT,                     -- JSON array of S{id}
    PRIMARY KEY (concept)
);

-- ============================================================
-- relations 表：断言间关系
-- ============================================================
CREATE TABLE IF NOT EXISTS relations (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_a         TEXT NOT NULL,
    claim_b         TEXT NOT NULL,
    relation_type   TEXT NOT NULL,            -- coexist/opposing/extends/same_source/shares_concept...
    context         TEXT,                     -- 关系成立的上下文说明
    strength        TEXT DEFAULT 'strong',    -- strong(人工/LLM) / weak(算法自动)
    created         TEXT NOT NULL,
    FOREIGN KEY (claim_a) REFERENCES claims(id),
    FOREIGN KEY (claim_b) REFERENCES claims(id)
);

CREATE INDEX IF NOT EXISTS idx_relations_a ON relations(claim_a);
CREATE INDEX IF NOT EXISTS idx_relations_b ON relations(claim_b);
CREATE INDEX IF NOT EXISTS idx_relations_type ON relations(relation_type);
CREATE INDEX IF NOT EXISTS idx_claims_source ON claims(source_id);
CREATE INDEX IF NOT EXISTS idx_claims_status ON claims(status);

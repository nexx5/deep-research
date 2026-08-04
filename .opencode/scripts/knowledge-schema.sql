-- 知识体系索引层 Schema
-- 文件: knowledge-schema.sql
-- 用途: 定义知识体系的 SQLite 索引层结构，从存储层文件派生，可随时重建
-- 设计原则: 文件是真相源，SQLite 是影子索引

PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

-- ============================================================
-- claims 表：断言（知识体系的原子单元）
-- 每条断言 = subject + predicate + object + boundary + lifecycle
-- ============================================================
CREATE TABLE IF NOT EXISTS claims (
    id              TEXT PRIMARY KEY,        -- CL001, CL002...
    subject         TEXT NOT NULL,            -- 主体概念（任何实体：平台/工具/人物/事件/概念）
    predicate       TEXT NOT NULL,            -- 关系/属性（提供/限制/优于/导致...）
    object          TEXT NOT NULL,            -- 客体（任何概念或值）
    boundary        TEXT,                     -- 边界条件（在什么条件下成立）
    status          TEXT NOT NULL DEFAULT 'active',  -- active/contested/superseded/stale
    confidence      TEXT DEFAULT 'M',         -- H/M/L
    sources         TEXT,                     -- JSON array of S{id}
    concepts        TEXT,                     -- JSON array of concept tags
    created         TEXT NOT NULL,            -- ISO date
    updated         TEXT,                     -- ISO date
    supersedes      TEXT,                     -- JSON array of claim_id（本断言取代了哪些）
    superseded_by   TEXT,                     -- JSON array of claim_id（本断言被哪些取代）
    superseded_reason TEXT,                   -- 取代原因
    extracted_from  TEXT,                     -- JSON array of A{id}/C{id}
    extraction_method TEXT DEFAULT 'key_claims',  -- key_claims/llm/migrated
    notes           TEXT,                     -- 自由备注
    embedding       TEXT,                     -- JSON array, 断言向量（subject+predicate+object+boundary拼接后嵌入）
    embedding_model TEXT,                     -- 嵌入模型名
    embedding_at    TEXT                      -- 嵌入时间 ISO格式
);

-- ============================================================
-- sources 表：来源元数据
-- ============================================================
CREATE TABLE IF NOT EXISTS sources (
    id              TEXT PRIMARY KEY,         -- S001, S002...
    title           TEXT NOT NULL,
    key_findings    TEXT,                     -- 一句话关键发现摘要
    url             TEXT,
    source_type     TEXT,                     -- web_page/github_repo/official_doc...
    created         TEXT NOT NULL,            -- ISO date
    raw_path        TEXT,
    extract_path    TEXT,
    analysis_ids    TEXT                      -- JSON array of A{id}
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
-- relations 表：断言间关系（开放关系类型）
-- ============================================================
CREATE TABLE IF NOT EXISTS relations (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_a         TEXT NOT NULL,
    claim_b         TEXT NOT NULL,
    relation_type   TEXT NOT NULL,            -- supports/contradicts/extends/supersedes/
                                              -- alternative_to/causes/part_of/depends_on/
                                              -- shares_concept/same_source (weak自动关系)
    context         TEXT,                     -- 关系成立的上下文说明
    strength        TEXT DEFAULT 'strong',    -- strong(人工/LLM判断) / weak(算法自动构建)
    created         TEXT NOT NULL,
    FOREIGN KEY (claim_a) REFERENCES claims(id),
    FOREIGN KEY (claim_b) REFERENCES claims(id)
);

CREATE INDEX IF NOT EXISTS idx_relations_a ON relations(claim_a);
CREATE INDEX IF NOT EXISTS idx_relations_b ON relations(claim_b);
CREATE INDEX IF NOT EXISTS idx_relations_type ON relations(relation_type);

-- ============================================================
-- comparisons 表：对比文档生命周期
-- ============================================================
CREATE TABLE IF NOT EXISTS comparisons (
    id              TEXT PRIMARY KEY,         -- C001, C002...
    topic           TEXT NOT NULL,
    status          TEXT DEFAULT 'active',    -- active/stale/superseded
    version         INTEGER DEFAULT 1,
    last_updated    TEXT,                     -- ISO date
    superseded_by   TEXT,                     -- C{id} or NULL
    file_path       TEXT,
    source_count    INTEGER DEFAULT 0,        -- 影响此对比的来源数
    latest_source_date TEXT                   -- 最新来源日期，用于过期检测
);

-- ============================================================
-- questions 表：问题索引（可回答/待回答/深度问题）
-- ============================================================
CREATE TABLE IF NOT EXISTS questions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    question        TEXT NOT NULL,
    category        TEXT NOT NULL,            -- can_answer/cannot_answer_yet/deep_question
    related_claims  TEXT,                     -- JSON array of claim_id
    created         TEXT NOT NULL
);

-- ============================================================
-- sync_log 表：同步日志（知识管理员的操作记录）
-- ============================================================
CREATE TABLE IF NOT EXISTS sync_log (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    action          TEXT NOT NULL,            -- rebuild/incremental/conflict_detect/status_change/view_generate
    details         TEXT,                     -- JSON: 操作详情
    claims_added    INTEGER DEFAULT 0,
    claims_updated  INTEGER DEFAULT 0,
    conflicts_found INTEGER DEFAULT 0,
    status_changes  INTEGER DEFAULT 0,
    timestamp       TEXT NOT NULL
);

-- ============================================================
-- FTS5 全文索引（对断言内容做中文全文检索）
-- 使用 unicode61 tokenizer，对中文按字符分词
-- 手动管理（不用外部内容表，避免列名映射问题）
-- ============================================================
CREATE VIRTUAL TABLE IF NOT EXISTS claims_fts USING fts5(
    claim_id UNINDEXED,
    subject,
    predicate,
    object,
    boundary,
    tokenize='unicode61'
);

-- 注意：FTS 数据由 rebuild-knowledge-index.py 手动插入，不用触发器

-- ============================================================
-- 便捷视图
-- ============================================================

-- active 断言视图（分析员/报告员常用）
CREATE VIEW IF NOT EXISTS v_active_claims AS
    SELECT id, subject, predicate, object, boundary, confidence, sources, concepts, created
    FROM claims
    WHERE status = 'active'
    ORDER BY created DESC;

-- contested 断言视图（知识管理员仲裁用）
CREATE VIEW IF NOT EXISTS v_contested_claims AS
    SELECT c1.id, c1.subject, c1.predicate, c1.object, c1.boundary,
           c1.superseded_by, c1.superseded_reason
    FROM claims c1
    WHERE c1.status = 'contested'
    ORDER BY c1.updated DESC;

-- stale 对比文档视图（过期检测用）
CREATE VIEW IF NOT EXISTS v_stale_comparisons AS
    SELECT id, topic, last_updated, latest_source_date, file_path
    FROM comparisons
    WHERE status = 'stale'
    ORDER BY last_updated DESC;

-- 断言关系视图（带关系类型标签）
CREATE VIEW IF NOT EXISTS v_claim_relations AS
    SELECT r.claim_a, r.claim_b, r.relation_type, r.context,
           c1.subject AS a_subject, c1.predicate AS a_predicate, c1.object AS a_object,
           c2.subject AS b_subject, c2.predicate AS b_predicate, c2.object AS b_object
    FROM relations r
    JOIN claims c1 ON r.claim_a = c1.id
    JOIN claims c2 ON r.claim_b = c2.id;

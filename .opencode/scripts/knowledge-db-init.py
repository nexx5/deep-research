#!/usr/bin/env python3
"""
知识包SQLite索引初始化 - knowledge-db-init.py
功能：创建知识包索引层SQLite数据库，包含FTS5全文索引（修复历史缺失问题）
使用：python knowledge-db-init.py --project-path "<项目路径>"
设计：文件是真相源，SQLite是影子索引，可从JSONL+md重建
"""

import sqlite3
import argparse
import os
from pathlib import Path

import sys
# Windows PowerShell GBK编码修复：强制stdout用UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA foreign_keys=ON;

-- ============================================================
-- claims 表：断言（知识原子单元）
-- ============================================================
CREATE TABLE IF NOT EXISTS claims (
    id              TEXT PRIMARY KEY,
    statement       TEXT NOT NULL,
    boundary        TEXT NOT NULL,
    source_id       TEXT,
    source_title    TEXT,
    source_type     TEXT,
    characteristics TEXT,          -- JSON array
    confidence      REAL DEFAULT 0.5,
    school          TEXT,
    extraction_level TEXT,         -- light/deep
    status          TEXT NOT NULL DEFAULT 'active',
    opposing        TEXT,          -- JSON array of claim_id
    possible_relations TEXT,       -- JSON array
    created         TEXT NOT NULL,
    updated         TEXT,
    FOREIGN KEY (source_id) REFERENCES sources(id)
);

-- ============================================================
-- sources 表：来源元数据
-- ============================================================
CREATE TABLE IF NOT EXISTS sources (
    id              TEXT PRIMARY KEY,
    title           TEXT NOT NULL,
    source_type     TEXT,
    url             TEXT,
    raw_path        TEXT,
    extract_path    TEXT,
    analysis_path   TEXT,
    created         TEXT NOT NULL
);

-- ============================================================
-- debates 表：争议议题
-- ============================================================
CREATE TABLE IF NOT EXISTS debates (
    id              TEXT PRIMARY KEY,
    topic           TEXT NOT NULL,
    positions       TEXT,          -- JSON
    status          TEXT DEFAULT 'coexist',
    resolution      TEXT,
    created         TEXT NOT NULL
);

-- ============================================================
-- schools 表：流派
-- ============================================================
CREATE TABLE IF NOT EXISTS schools (
    id              TEXT PRIMARY KEY,
    name            TEXT NOT NULL,
    core_claims     TEXT,          -- JSON array
    representatives TEXT,          -- JSON array
    boundaries      TEXT,
    characteristics TEXT,          -- JSON array
    evolution_path  TEXT,
    opposing_schools TEXT,         -- JSON array
    created         TEXT NOT NULL
);

-- ============================================================
-- concepts 表：概念索引
-- ============================================================
CREATE TABLE IF NOT EXISTS concepts (
    concept         TEXT PRIMARY KEY,
    claim_ids       TEXT,          -- JSON array
    source_ids      TEXT           -- JSON array
);

-- ============================================================
-- relations 表：断言间关系
-- ============================================================
CREATE TABLE IF NOT EXISTS relations (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    claim_a         TEXT NOT NULL,
    claim_b         TEXT NOT NULL,
    relation_type   TEXT NOT NULL,  -- supports/contradicts/extends/supersedes/alternative_to
    context         TEXT,
    created         TEXT NOT NULL,
    FOREIGN KEY (claim_a) REFERENCES claims(id),
    FOREIGN KEY (claim_b) REFERENCES claims(id)
);

CREATE INDEX IF NOT EXISTS idx_relations_a ON relations(claim_a);
CREATE INDEX IF NOT EXISTS idx_relations_b ON relations(claim_b);
CREATE INDEX IF NOT EXISTS idx_relations_type ON relations(relation_type);

-- ============================================================
-- source_leads 表：线索池
-- ============================================================
CREATE TABLE IF NOT EXISTS source_leads (
    id              TEXT PRIMARY KEY,
    trigger_type    TEXT NOT NULL,
    target_type     TEXT NOT NULL,
    target          TEXT NOT NULL,
    context         TEXT,
    source_article  TEXT,
    priority        TEXT DEFAULT 'P1',
    reference_count INTEGER DEFAULT 1,
    related_outline_node TEXT,
    status          TEXT DEFAULT 'pending',
    created         TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_leads_priority ON source_leads(priority, status);
CREATE INDEX IF NOT EXISTS idx_leads_target ON source_leads(target);

-- ============================================================
-- sync_log 表：同步日志
-- ============================================================
CREATE TABLE IF NOT EXISTS sync_log (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    action          TEXT NOT NULL,
    details         TEXT,
    claims_added    INTEGER DEFAULT 0,
    claims_updated  INTEGER DEFAULT 0,
    conflicts_found INTEGER DEFAULT 0,
    status_changes  INTEGER DEFAULT 0,
    timestamp       TEXT NOT NULL
);

-- ============================================================
-- FTS5 全文索引（关键修复：确保虚拟表正确创建）
-- 使用 unicode61 tokenizer 对中文按字符分词
-- ============================================================
CREATE VIRTUAL TABLE IF NOT EXISTS claims_fts USING fts5(
    claim_id UNINDEXED,
    statement,
    boundary,
    characteristics,
    source_title,
    tokenize='unicode61'
);

-- ============================================================
-- 便捷视图
-- ============================================================
CREATE VIEW IF NOT EXISTS v_active_claims AS
    SELECT id, statement, boundary, source_id, characteristics, confidence, school, created
    FROM claims
    WHERE status = 'active'
    ORDER BY created DESC;

CREATE VIEW IF NOT EXISTS v_contested_claims AS
    SELECT id, statement, boundary, opposing
    FROM claims
    WHERE status = 'contested'
    ORDER BY created DESC;

CREATE VIEW IF NOT EXISTS v_pending_leads AS
    SELECT id, trigger_type, target_type, target, priority, reference_count
    FROM source_leads
    WHERE status = 'pending' AND priority IN ('P0', 'P1')
    ORDER BY
        CASE priority WHEN 'P0' THEN 0 WHEN 'P1' THEN 1 ELSE 2 END,
        reference_count DESC;

CREATE VIEW IF NOT EXISTS v_coexist_debates AS
    SELECT id, topic, positions, resolution
    FROM debates
    WHERE status = 'coexist';

CREATE VIEW IF NOT EXISTS v_unresolved_debates AS
    SELECT id, topic, positions
    FROM debates
    WHERE status = 'unresolved';
"""

def init_database(db_path):
    """初始化数据库"""
    # 确保目录存在
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # 如果数据库已存在，先备份
    if os.path.exists(db_path):
        backup_path = db_path + f".bak"
        os.rename(db_path, backup_path)
        print(f"  已有数据库备份到: {backup_path}")

    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA_SQL)

    # 验证FTS5表创建成功
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='claims_fts'")
    fts_exists = cursor.fetchone()
    if fts_exists:
        print(f"  FTS5表 claims_fts 创建成功")
    else:
        print(f"  警告：FTS5表创建失败！检查SQLite版本是否支持FTS5")
        # 尝试不带FTS5的降级方案
        conn.execute("""
            CREATE TABLE IF NOT EXISTS claims_fts_fallback (
                claim_id TEXT,
                statement TEXT,
                boundary TEXT,
                characteristics TEXT,
                source_title TEXT
            )
        """)
        print(f"  已创建降级表 claims_fts_fallback")

    # 写入sync_log
    from datetime import datetime, timezone
    conn.execute("""
        INSERT INTO sync_log (action, details, timestamp)
        VALUES ('init', '数据库初始化', ?)
    """, (datetime.now(timezone.utc).isoformat(),))

    conn.commit()
    conn.close()
    print(f"  数据库初始化完成: {db_path}")

def main():
    parser = argparse.ArgumentParser(description='知识包SQLite索引初始化')
    parser.add_argument('--project-path', required=True, help='项目路径（含knowledge-pack/目录）')
    args = parser.parse_args()

    db_path = Path(args.project_path) / 'knowledge-pack' / 'index' / 'knowledge.db'
    print(f"初始化知识包数据库: {db_path}")
    init_database(str(db_path))

if __name__ == '__main__':
    main()

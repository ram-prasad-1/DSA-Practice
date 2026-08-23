-- 02. PRAGMAs — introspection, integrity, maintenance
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- what's attached, what's in it
PRAGMA database_list;                       -- main / temp / ATTACHed files
PRAGMA table_list;                          -- (3.37+) tables+views with types
SELECT * FROM pragma_table_list WHERE schema = 'main' AND name = 'products';



-- per-object detail (also available as pragma_* functions — section 13)
PRAGMA table_info(customers);
PRAGMA index_list(products);
PRAGMA foreign_key_list(order_items);



-- build info
PRAGMA compile_options;                     -- what this binary includes
SELECT sqlite_version();



-- health checks: full vs quick
PRAGMA integrity_check;                     -- 'ok' or a list of problems
PRAGMA quick_check;                         -- faster, skips some index checks
PRAGMA foreign_key_check;                   -- FK orphans (empty = clean)



-- planner statistics: ANALYZE fills sqlite_stat1; optimize runs what's needed
ANALYZE;
SELECT * FROM sqlite_stat1 LIMIT 5;
PRAGMA optimize;                            -- ⭐ run on connection close



-- user_version: a free 32-bit int in the header — the classic
-- lightweight migration tracker
PRAGMA user_version;
PRAGMA user_version = 3;                    -- "schema is at migration 3"
PRAGMA user_version;

-- application_id: mark the file format as YOURS (file(1) can identify it)
PRAGMA application_id;



-- space accounting & reclamation
PRAGMA freelist_count;                      -- pages freed by deletes, unreclaimed
PRAGMA auto_vacuum;                         -- 0=none 1=full 2=incremental
-- VACUUM rebuilds the file compactly (see section 19)



-- schema_version: bumped internally on every DDL change (read-only signal)
PRAGMA schema_version;



-- Practice
-- Q1. Write the "unindexed foreign keys" audit using only pragma_*
--     functions (hint: section 13 Q4) — the single most useful pragma query.
-- Q2. Use user_version to gate a fake migration: read it, apply DDL
--     only if < 4, set it to 4.
-- Q3. Delete half of events (if you added them), check freelist_count,
--     VACUUM, check again.
-- Q4. Diff PRAGMA compile_options between your CLI and PyCharm's
--     bundled driver — which features differ?

-- 02. Backup, VACUUM, ATTACH — keeping the single file healthy
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- ⚠ plain file copy of a LIVE db is unsafe: a write mid-copy corrupts
-- the copy, and WAL content may be missing. Safe options below.



-- VACUUM INTO (3.27+): a consistent snapshot to a NEW file, pure SQL ⭐
-- one-shot by design: it ERRORS if the target exists ('output file
-- already exists') — delete the old backup first. Uncomment to run:
-- VACUUM INTO '/tmp/play-backup.db';



-- VACUUM (no INTO) rebuilds THIS file: reclaims free pages, defragments
PRAGMA freelist_count;
VACUUM;
PRAGMA freelist_count;                       -- 0 after



-- CLI alternatives (terminal only):
--   .backup backup.db          online backup API — safe while live,
--                              and unlike VACUUM INTO it overwrites
--   .dump > dump.sql           logical backup: portable SQL text
--   sqlite3 new.db ".read dump.sql"    restore from it
-- offline (nothing writing + WAL checkpointed): plain cp works too



-- integrity: verify backups (and originals) actually open clean
PRAGMA integrity_check;



-- ATTACH: query ACROSS database files — schema.table names.
-- attaching a missing file CREATES it (re-runnable, unlike VACUUM INTO)
ATTACH DATABASE '/tmp/play-archive.db' AS archive;
PRAGMA database_list;

-- cross-database copy: the archive pattern
DROP TABLE IF EXISTS archive.cancelled_orders;
CREATE TABLE archive.cancelled_orders AS
SELECT * FROM main.orders WHERE status = 'cancelled';

SELECT (SELECT count(*) FROM main.orders)             AS live_orders,
       (SELECT count(*) FROM archive.cancelled_orders) AS archived;

-- a transaction spanning both files is still atomic (one COMMIT)
DETACH DATABASE archive;



-- in-memory databases: ':memory:' vanishes on close — perfect scratch space
ATTACH DATABASE ':memory:' AS scratch;
CREATE TABLE scratch.tmp_calc AS
SELECT category_id, avg(price) AS avg_price FROM products GROUP BY category_id;
SELECT * FROM scratch.tmp_calc;
DETACH DATABASE scratch;



-- engine limits — the SQLITE_MAX_* family (defaults: 2000 columns,
-- 10 attached dbs, ~281TB max db) — see sqlite.org/limits.html
PRAGMA main.page_size;
PRAGMA main.max_page_count;



-- Practice
-- Q1. Run the VACUUM INTO line twice — read the error, then make it
--     succeed again (delete the file, or use a new name).
-- Q2. Archive job: move (copy + delete) cancelled orders into
--     /tmp/play-archive.db inside ONE transaction; re-run 00_schema after.
-- Q3. In the CLI: .backup vs VACUUM INTO vs .dump — compare file sizes
--     and try restoring each.
-- Q4. ATTACH two extra dbs at once and list them via PRAGMA database_list.

-- 02. Locking, WAL & SQLITE_BUSY — how SQLite handles concurrency
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (some behavior here only shows with TWO connections — notes inline)



-- SQLite's model: ONE writer at a time, database-level locking,
-- SERIALIZABLE isolation. No row locks, no SELECT ... FOR UPDATE.



-- journal mode: how atomic commit is implemented
PRAGMA journal_mode;               -- 'delete' = rollback journal (default)
PRAGMA journal_mode = WAL;         -- ⭐ write-ahead log: readers don't block
                                   -- the writer, writer doesn't block readers
PRAGMA journal_mode;               -- persists in the FILE, not the connection



-- BEGIN flavors decide WHEN the write lock is taken:
--   DEFERRED  (default) at the first write — can fail LATE with BUSY
--   IMMEDIATE at BEGIN — ⭐ use for write transactions
--   EXCLUSIVE at BEGIN, blocks new readers too (non-WAL)
BEGIN IMMEDIATE;
UPDATE products SET in_stock = in_stock WHERE id = 1;
COMMIT;



-- busy handling: without a timeout a locked db errors instantly with
-- SQLITE_BUSY ('database is locked'); with one, SQLite retries quietly
PRAGMA busy_timeout;               -- 0 by default
PRAGMA busy_timeout = 5000;        -- ⭐ 5s — set on EVERY connection



-- durability dial (per connection): how hard COMMIT syncs to disk
PRAGMA synchronous;                -- 2 = FULL (default)
PRAGMA synchronous = NORMAL;       -- ⭐ recommended with WAL: fast, safe



-- WAL housekeeping: the -wal file grows until a checkpoint copies it
-- back into the main db (automatic every ~1000 pages, or manual)
PRAGMA wal_autocheckpoint;
PRAGMA wal_checkpoint(TRUNCATE);   -- returns busy|log_pages|checkpointed



-- TRY IT with two terminals (connection A and B on the same play.db):
--   A: BEGIN IMMEDIATE; UPDATE products SET price = price WHERE id = 1;
--   B: UPDATE products SET price = price WHERE id = 2;
--      → B waits up to busy_timeout, then 'database is locked'
--   B (WAL): SELECT count(*) FROM products;
--      → works instantly — readers are never blocked in WAL
--   A: COMMIT;   → B's queued write can now proceed



-- the ⭐ app-startup block this section justifies:
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA busy_timeout = 5000;



-- Practice
-- Q1. Open two sqlite3 terminals on play.db and reproduce the BUSY
--     scenario above, with and without busy_timeout.
-- Q2. Switch journal_mode back to DELETE and show readers now block
--     during a write transaction.
-- Q3. Check the -wal and -shm files on disk while a transaction is
--     open; run wal_checkpoint(TRUNCATE) and check again.
-- Q4. Why does BEGIN IMMEDIATE beat BEGIN DEFERRED for write
--     transactions in app code? (think: where does BUSY strike?)

-- 01. PRAGMAs — behavior & performance configuration
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (a PRAGMA without '=' READS the setting; with '=' it WRITES it)



-- ⭐ the startup block every SQLite app should run per connection:
PRAGMA foreign_keys = ON;         -- FK enforcement is OFF by default!
PRAGMA journal_mode = WAL;        -- concurrent readers + writer (sticks to the file)
PRAGMA synchronous = NORMAL;      -- durable-enough + fast with WAL
PRAGMA busy_timeout = 5000;       -- wait 5s on locks instead of erroring



-- proof that foreign_keys matters: with it OFF this orphan INSERT works
PRAGMA foreign_keys = OFF;
INSERT INTO orders (id, customer_id, placed_at, status)
VALUES (9601, 999, '2024-09-21', 'pending');            -- customer 999 doesn't exist!
PRAGMA foreign_keys = ON;
-- INSERT ... VALUES (9602, 999, ...);   -- uncomment → FOREIGN KEY constraint failed
PRAGMA foreign_key_check;                -- finds the orphan we snuck in
DELETE FROM orders WHERE id = 9601;



-- connection-scoped vs file-scoped: journal_mode lives in the FILE;
-- foreign_keys, busy_timeout, synchronous reset on every new connection
PRAGMA journal_mode;



-- performance dials (session-scoped)
PRAGMA cache_size;                -- negative = KiB; -2000 ≈ 2MB default
PRAGMA cache_size = -20000;       -- give hot databases more page cache
PRAGMA mmap_size = 268435456;     -- memory-map up to 256MB of the file
PRAGMA temp_store = MEMORY;       -- temp tables/sorts in RAM



-- behavior switches worth knowing
PRAGMA recursive_triggers;        -- triggers firing triggers (off by default)
PRAGMA defer_foreign_keys;        -- FK checks at COMMIT for this txn
PRAGMA secure_delete;             -- zero out deleted content (privacy, slower)



-- sizing & stats
PRAGMA page_size;                 -- bytes per page (set before creation/VACUUM)
PRAGMA page_count;
SELECT (SELECT page_count FROM pragma_page_count) *
       (SELECT page_size  FROM pragma_page_size) AS db_bytes;



-- Practice
-- Q1. Show that busy_timeout resets to 0 on a fresh connection
--     (two sqlite3 sessions).
-- Q2. Turn foreign_keys OFF, delete a customer with orders, then run
--     PRAGMA foreign_key_check. Repair and re-run 00_schema.
-- Q3. Compare .timer results for a big query with cache_size default
--     vs -50000.
-- Q4. What does PRAGMA journal_mode = DELETE print, and why might a
--     -wal file still exist afterward?

-- 02. Query plans & the optimizer — reading EQP, ANALYZE, planner traps
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (run 01_create_indexes.sql first for its indexes, or re-create below)

DROP INDEX IF EXISTS idx_events_customer_kind;
CREATE INDEX idx_events_customer_kind ON events(customer_id, kind);
DROP INDEX IF EXISTS idx_events_at;
CREATE INDEX idx_events_at ON events(at);



-- read plans on joins: which table is outer, which index serves the inner
EXPLAIN QUERY PLAN
SELECT c.name, count(*)
FROM customers c
JOIN events e ON e.customer_id = c.id
GROUP BY c.id;



-- trap 1: a function on the indexed COLUMN disables the index...
EXPLAIN QUERY PLAN SELECT * FROM events WHERE date(at) = '2024-06-01';
-- ...rewrite as a range on the raw column (sargable)
EXPLAIN QUERY PLAN
SELECT * FROM events WHERE at >= '2024-06-01' AND at < '2024-06-02';



-- trap 2: leading-wildcard LIKE cannot use an ordinary index
EXPLAIN QUERY PLAN SELECT * FROM events WHERE at LIKE '%06-01%';   -- SCAN
EXPLAIN QUERY PLAN SELECT * FROM events WHERE at LIKE '2024-06%';  -- SEARCH (text col)



-- trap 3: OR across different columns often scans — UNION of two
-- indexed queries can be faster
EXPLAIN QUERY PLAN
SELECT * FROM events WHERE customer_id = 3 OR at >= '2024-08-01';



-- ANALYZE gathers row statistics so the planner picks better indexes;
-- PRAGMA optimize runs it as needed (⭐ call on connection close)
ANALYZE;
SELECT * FROM sqlite_stat1 WHERE tbl = 'events';
PRAGMA optimize;



-- ORDER BY can be free if an index already delivers the order
EXPLAIN QUERY PLAN SELECT * FROM events ORDER BY at LIMIT 10;        -- index walk
EXPLAIN QUERY PLAN SELECT * FROM events ORDER BY kind LIMIT 10;      -- sort (TEMP B-TREE)



-- forcing / forbidding (diagnostics, not production tools)
EXPLAIN QUERY PLAN SELECT * FROM events NOT INDEXED WHERE customer_id = 3;
EXPLAIN QUERY PLAN
SELECT * FROM events INDEXED BY idx_events_customer_kind WHERE customer_id = 3;



-- timing at the CLI: .timer on   (then run a query twice — cache warm-up)



-- Practice
-- Q1. Make the 'checkout events per month' report sargable and indexed:
--     compare plans before and after.
-- Q2. Find one query in earlier sections that would hit trap 1, and fix it.
-- Q3. Delete the events indexes, ANALYZE, and watch the join plan change.
-- Q4. Use .timer on in the CLI to measure trap 2's two LIKE variants.

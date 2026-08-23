-- 01. Transactions & savepoints — BEGIN, COMMIT, ROLLBACK, SAVEPOINT
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- autocommit: every bare statement is its own transaction.
-- BEGIN...COMMIT groups statements into ONE atomic unit
BEGIN;
UPDATE products SET in_stock = in_stock - 1 WHERE id = 1;
INSERT INTO orders (id, customer_id, placed_at, status)
VALUES (9501, 1, '2024-09-20', 'pending');
INSERT INTO order_items VALUES (9501, 1, 1, 129.00);
COMMIT;
SELECT id, status FROM orders WHERE id = 9501;



-- ROLLBACK undoes everything since BEGIN
BEGIN;
DELETE FROM order_items;
DELETE FROM orders;
SELECT count(*) AS inside_txn FROM orders;      -- 0 inside the transaction...
ROLLBACK;
SELECT count(*) AS after_rollback FROM orders;  -- ...all back afterwards



-- a failed statement does NOT auto-rollback the transaction —
-- your app decides (this is why drivers wrap statements for you)



-- SAVEPOINT: named nested checkpoints inside a transaction
BEGIN;
UPDATE products SET price = price * 2 WHERE id = 11;

SAVEPOINT risky;
UPDATE products SET price = 0.01 WHERE category_id = 5;
ROLLBACK TO risky;                 -- undo only the savepoint's changes
RELEASE risky;                     -- discard the savepoint marker

COMMIT;                            -- the ×2 on id 11 survives
SELECT id, price FROM products WHERE category_id = 5;

UPDATE products SET price = price / 2 WHERE id = 11;   -- restore the demo



-- transactions are also SQLite's bulk-write accelerator: one fsync per
-- COMMIT instead of per statement — wrap bulk INSERT loops in BEGIN/COMMIT
DROP TABLE IF EXISTS bulk_demo;
CREATE TABLE bulk_demo (x INTEGER PRIMARY KEY, at TEXT NOT NULL);
BEGIN;
WITH RECURSIVE n(x) AS (SELECT 1 UNION ALL SELECT x+1 FROM n WHERE x < 1000)
INSERT INTO bulk_demo (x, at)
SELECT x, datetime('2024-09-01', '+' || x || ' minutes') FROM n;
COMMIT;
SELECT count(*) FROM bulk_demo;
DROP TABLE bulk_demo;

DELETE FROM order_items WHERE order_id = 9501;   -- clean up the demo order
DELETE FROM orders WHERE id = 9501;



-- Practice
-- Q1. Transfer stock: move 5 units of product 4 to product 5 in one
--     transaction; ROLLBACK if either update would go negative.
-- Q2. Nest two savepoints, roll back the inner, commit — what survives?
-- Q3. Time inserting 5000 events with and without a wrapping
--     transaction (.timer on in the CLI).

-- 01. Indexes — CREATE INDEX, composite, partial, expression, covering
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (this section's schema adds 'events': 5000 rows to make plans visible)



-- EXPLAIN QUERY PLAN shows how a query runs: SCAN = read everything,
-- SEARCH = jump via an index. Without an index: full scan
EXPLAIN QUERY PLAN SELECT * FROM events WHERE customer_id = 3;



-- CREATE INDEX turns that into a SEARCH
DROP INDEX IF EXISTS idx_events_customer;
CREATE INDEX idx_events_customer ON events(customer_id);
EXPLAIN QUERY PLAN SELECT * FROM events WHERE customer_id = 3;



-- composite index: column ORDER matters — leftmost prefix rule.
-- (customer_id, kind) serves customer_id alone, and customer_id+kind,
-- but NOT kind alone
DROP INDEX IF EXISTS idx_events_customer_kind;
CREATE INDEX idx_events_customer_kind ON events(customer_id, kind);
EXPLAIN QUERY PLAN SELECT * FROM events WHERE customer_id = 3 AND kind = 'checkout';
EXPLAIN QUERY PLAN SELECT * FROM events WHERE kind = 'checkout';   -- still a SCAN



-- UNIQUE index: constraint + index in one
DROP INDEX IF EXISTS idx_customers_email;
CREATE UNIQUE INDEX idx_customers_email ON customers(email);



-- partial index: index only the rows you query — smaller, faster writes
DROP INDEX IF EXISTS idx_events_checkouts;
CREATE INDEX idx_events_checkouts ON events(at) WHERE kind = 'checkout';
EXPLAIN QUERY PLAN
SELECT * FROM events WHERE kind = 'checkout' AND at >= '2024-06-01';



-- expression index: makes function-wrapped lookups indexable
DROP INDEX IF EXISTS idx_customers_email_lower;
CREATE INDEX idx_customers_email_lower ON customers(lower(email));
EXPLAIN QUERY PLAN SELECT * FROM customers WHERE lower(email) = 'ada@example.com';



-- covering index: when the index holds every needed column the table
-- is never touched — the plan says COVERING INDEX
EXPLAIN QUERY PLAN
SELECT customer_id, kind FROM events WHERE customer_id = 5;



-- what exists, and what it costs: every index is duplicated data
-- maintained on each write — index deliberately, not defensively
SELECT name FROM sqlite_schema WHERE type = 'index' AND tbl_name = 'events';



-- Practice
-- Q1. ⭐ Index every FK in the store schema (orders.customer_id,
--     order_items.order_id, order_items.product_id, products.category_id
--     — SQLite never auto-indexes FKs) and re-plan a customer→orders join.
-- Q2. A partial index on orders WHERE status = 'pending' — check it is
--     used for the "open orders" query and NOT for delivered ones.
-- Q3. Compare plans: WHERE at LIKE '2024-06%' vs
--     WHERE at >= '2024-06-01' AND at < '2024-07-01' on an at-index.

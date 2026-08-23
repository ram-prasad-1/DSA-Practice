-- 04. LIMIT & paging — LIMIT, OFFSET, top-N, keyset pagination
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- LIMIT n caps the row count; OFFSET m skips m rows first.
-- Always pair with ORDER BY — otherwise the "first n rows" are arbitrary.
SELECT id, placed_at, status FROM orders ORDER BY placed_at LIMIT 5;



-- top-N pattern: ORDER BY + LIMIT
SELECT name, price FROM products ORDER BY price DESC LIMIT 3;



-- top 3 orders by value, via the order_totals view from the schema
SELECT order_id, placed_at, total FROM order_totals ORDER BY total DESC LIMIT 3;



-- OFFSET paging: LIMIT n OFFSET m = page (m/n)+1
-- ('LIMIT m, n' means the same but the order flips — MySQL style)
SELECT id, placed_at FROM orders ORDER BY id LIMIT 4 OFFSET 0;   -- page 1
SELECT id, placed_at FROM orders ORDER BY id LIMIT 4 OFFSET 4;   -- page 2
SELECT id, placed_at FROM orders ORDER BY id LIMIT 4 OFFSET 8;   -- page 3



-- Nth-highest: skip N-1, take 1 (3rd most expensive product)
SELECT name, price FROM products ORDER BY price DESC LIMIT 1 OFFSET 2;



-- OFFSET pitfall: the engine still walks every skipped row (slow on deep
-- pages) and inserts between page loads shift results.
-- Keyset pagination instead: remember the last seen key, continue after it.
SELECT id, placed_at FROM orders ORDER BY id LIMIT 4;                 -- page 1
SELECT id, placed_at FROM orders WHERE id > 1004 ORDER BY id LIMIT 4; -- page 2



-- keyset on a non-unique column needs a tiebreaker key
SELECT id, placed_at
FROM orders
WHERE (placed_at, id) > ('2024-05-02', 1005)
ORDER BY placed_at, id
LIMIT 4;



-- Practice
-- Q1. The 5 most recent orders (by placed_at).
-- Q2. Page 2 of products by price ascending, 5 per page (LIMIT/OFFSET).
-- Q3. The same page 2 via keyset pagination (price needs id as tiebreaker).
-- Q4. The 2nd cheapest product.
-- Q5. The order with the 3rd highest total (use order_totals).

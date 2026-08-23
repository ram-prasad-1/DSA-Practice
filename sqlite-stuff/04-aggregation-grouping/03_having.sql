-- 03. HAVING — filtering groups (vs WHERE filtering rows)
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- WHERE runs BEFORE grouping (per row); HAVING runs AFTER (per group)
SELECT customer_id, count(*) AS orders
FROM orders
GROUP BY customer_id
HAVING count(*) >= 2;



-- HAVING can use any aggregate, not just the selected one
SELECT category_id, count(*) AS products
FROM products
GROUP BY category_id
HAVING max(price) > 200;



-- WHERE + HAVING together: filter rows first, then filter the groups
SELECT customer_id, count(*) AS delivered_orders
FROM orders
WHERE status = 'delivered'
GROUP BY customer_id
HAVING count(*) >= 2;



-- putting a row condition in HAVING instead of WHERE is wasteful
-- (groups everything first) and often wrong — compare:
SELECT status, count(*) FROM orders WHERE placed_at >= '2024-05-01' GROUP BY status;
SELECT status, count(*) FROM orders GROUP BY status HAVING placed_at >= '2024-05-01';
-- the HAVING version tests an arbitrary row's placed_at per group (bare column!)



-- the full pipeline, in logical execution order:
-- FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
SELECT category_id, count(*) AS n, round(avg(price), 2) AS avg_price
FROM products
WHERE in_stock > 0                 -- rows: only stocked products
GROUP BY category_id               -- groups: per category
HAVING count(*) >= 2               -- groups: at least 2 stocked products
ORDER BY avg_price DESC            -- sort the surviving groups
LIMIT 3;                           -- top 3



-- Practice
-- Q1. Countries with more than one customer.
-- Q2. Products (from order_items, by product_id) ordered more than once
--     — i.e. appearing in 2+ distinct orders.
-- Q3. Months with 2+ orders, using only non-cancelled orders.
-- Q4. Rewrite Q3 with the date filter wrongly in HAVING and explain
--     why the result can differ.

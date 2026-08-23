-- 01. Window basics — OVER, PARTITION BY: aggregates without collapsing rows
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- an aggregate + OVER () computes across the whole result set
-- while KEEPING every row (GROUP BY would collapse them)
SELECT name, price,
       round(avg(price) OVER (), 2) AS avg_all,
       round(price - avg(price) OVER (), 2) AS vs_avg
FROM products;



-- PARTITION BY: a separate window per group — per-category stats
-- next to each product
SELECT name, category_id, price,
       round(avg(price) OVER (PARTITION BY category_id), 2) AS category_avg,
       max(price)       OVER (PARTITION BY category_id)     AS category_max,
       count(*)         OVER (PARTITION BY category_id)     AS category_size
FROM products;



-- compare with GROUP BY: one row per category, detail rows gone
SELECT category_id, round(avg(price), 2) AS category_avg
FROM products
GROUP BY category_id;



-- windows are computed AFTER WHERE/GROUP BY/HAVING — you cannot filter
-- on a window function directly; wrap it in a subquery or CTE
WITH priced AS (
  SELECT name, category_id, price,
         avg(price) OVER (PARTITION BY category_id) AS category_avg
  FROM products
)
SELECT name, price, round(category_avg, 2) AS category_avg
FROM priced
WHERE price > category_avg;          -- above their category's average



-- share-of-group in one pass (no correlated subquery needed)
SELECT o.customer_id, t.order_id, t.total,
       round(100.0 * t.total / sum(t.total) OVER (PARTITION BY o.customer_id), 1)
         AS pct_of_customer_spend
FROM order_totals t
JOIN orders o ON o.id = t.order_id;



-- Practice
-- Q1. Each order with the count of orders its customer has placed.
-- Q2. Each product's price as a % of its category's max.
-- Q3. Orders whose total is above their month's average total
--     (window in a CTE, filter outside).

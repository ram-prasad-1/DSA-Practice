-- 03. Date reporting — grouping by period, ranges, gaps, durations
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- group by month / quarter / week via strftime
SELECT strftime('%Y-%m', placed_at) AS month, count(*) AS orders
FROM orders GROUP BY month;

SELECT strftime('%Y', placed_at) || '-Q' ||
       ((strftime('%m', placed_at) + 2) / 3) AS quarter,
       count(*) AS orders
FROM orders GROUP BY quarter;

SELECT strftime('%Y-W%W', placed_at) AS week, count(*) AS orders
FROM orders GROUP BY week;



-- date-range filtering: half-open ranges [start, next-start) are safest —
-- BETWEEN '2024-03-01' AND '2024-03-31' would miss '2024-03-31 10:00'
-- the moment timestamps appear
SELECT count(*) AS march_orders
FROM orders
WHERE placed_at >= '2024-03-01' AND placed_at < '2024-04-01';



-- durations: customer tenure and order recency at a reference date
SELECT name, signed_up,
       CAST((julianday('2024-12-31') - julianday(signed_up)) / 30.44 AS INTEGER)
         AS months_as_customer
FROM customers;



-- gaps: days between consecutive orders (window recap)
SELECT id, placed_at,
       julianday(placed_at) - julianday(lag(placed_at) OVER (ORDER BY placed_at))
         AS gap_days
FROM orders;



-- filling missing periods with a recursive calendar (section 06 recap):
-- months with ZERO orders still appear
WITH RECURSIVE months(m) AS (
  SELECT '2024-01'
  UNION ALL
  SELECT strftime('%Y-%m', m || '-01', '+1 month') FROM months WHERE m < '2024-12'
)
SELECT m AS month, count(o.id) AS orders
FROM months
LEFT JOIN orders o ON strftime('%Y-%m', o.placed_at) = m
GROUP BY m;



-- cohorting: customers bucketed by signup month, with their order counts
SELECT strftime('%Y-%m', c.signed_up) AS cohort,
       count(DISTINCT c.id) AS customers,
       count(o.id) AS orders
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY cohort;



-- Practice
-- Q1. Revenue per quarter using order_totals.
-- Q2. Average days from signup to FIRST order per cohort month.
-- Q3. The longest gap between any two consecutive orders (wrap the
--     lag query, take max).
-- Q4. A full 2024 weekly calendar (recursive) with order counts,
--     zeros included.

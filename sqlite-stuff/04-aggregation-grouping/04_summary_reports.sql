-- 04. Summary reports — monthly revenue, subtotals, ROLLUP emulation
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (order_totals is the view from 00_schema.sql: one row per order with its total)



-- revenue per month
SELECT strftime('%Y-%m', placed_at) AS month,
       count(*)                     AS orders,
       round(sum(total), 2)         AS revenue
FROM order_totals
GROUP BY month
ORDER BY month;



-- spend per customer, biggest first
SELECT customer_id, count(*) AS orders, round(sum(total), 2) AS spend
FROM order_totals
GROUP BY customer_id
ORDER BY spend DESC;



-- share of total: an aggregate divided by a scalar subquery over the same data
SELECT status,
       count(*) AS orders,
       round(100.0 * count(*) / (SELECT count(*) FROM orders), 1) AS pct
FROM orders
GROUP BY status;



-- SQLite has no ROLLUP/CUBE/GROUPING SETS — emulate subtotal rows
-- with UNION ALL (a grand-total row appended to the per-status report)
SELECT status AS label, count(*) AS orders, round(sum(total), 2) AS revenue
FROM order_totals
GROUP BY status
UNION ALL
SELECT 'TOTAL', count(*), round(sum(total), 2)
FROM order_totals;



-- min/max with their bare-column exception: best and worst month by revenue
SELECT max(revenue) AS best_revenue, month AS best_month
FROM (SELECT strftime('%Y-%m', placed_at) AS month, sum(total) AS revenue
      FROM order_totals GROUP BY month);



-- average of an aggregate needs a subquery (avg order count per customer)
SELECT round(avg(n), 2) AS avg_orders_per_customer
FROM (SELECT count(*) AS n FROM orders GROUP BY customer_id);



-- Practice
-- Q1. Revenue per quarter (hint: months 01-03 → Q1; CASE on strftime('%m')).
-- Q2. Per-country customer count with a TOTAL row via UNION ALL.
-- Q3. The single month with the most orders (subquery + max, or
--     ORDER BY + LIMIT — try both).
-- Q4. Average line-item value per order, then the average of that
--     across all orders (aggregate of an aggregate).

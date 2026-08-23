-- 04. CTEs — WITH: named, chainable subqueries
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- WITH names a subquery; the main query reads it like a table
WITH monthly AS (
  SELECT strftime('%Y-%m', placed_at) AS month, count(*) AS orders
  FROM orders
  GROUP BY month
)
SELECT * FROM monthly WHERE orders >= 2;



-- chaining: later CTEs can use earlier ones — pipelines beat deep nesting
WITH spend AS (
  SELECT customer_id, sum(total) AS total_spend
  FROM order_totals
  GROUP BY customer_id
),
ranked AS (
  SELECT customer_id, total_spend,
         (SELECT count(*) FROM spend s2 WHERE s2.total_spend > s.total_spend) + 1 AS rank
  FROM spend s
)
SELECT c.name, r.total_spend, r.rank
FROM ranked r
JOIN customers c ON c.id = r.customer_id
ORDER BY r.rank;



-- one CTE, used twice (a derived table would be written out twice)
WITH cat_avg AS (
  SELECT category_id, avg(price) AS avg_price
  FROM products
  GROUP BY category_id
)
SELECT p.name, p.price, round(a.avg_price, 2) AS category_avg
FROM products p
JOIN cat_avg a ON a.category_id = p.category_id
WHERE p.price > (SELECT max(avg_price) FROM cat_avg);



-- MATERIALIZED / NOT MATERIALIZED (3.35+): hint whether SQLite should
-- compute the CTE once into a temp table or inline it into the query
WITH big_orders AS MATERIALIZED (
  SELECT * FROM order_totals WHERE total > 300
)
SELECT count(*) FROM big_orders;



-- Practice
-- Q1. Rewrite your section-04 "revenue per month" report as a CTE chain:
--     totals per order → per month → only months above the overall
--     monthly average.
-- Q2. CTE 'usa' (USA customers) reused twice: count them AND list their
--     orders in one statement.
-- Q3. Same-category product pairs within 30.00 of each other (section 05
--     practice), readable this time via a CTE.

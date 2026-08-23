-- 03. LAG and LEAD — reaching into neighboring rows
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- lag(col) = previous row's value in window order; lead(col) = next row's
SELECT id, placed_at,
       lag(placed_at)  OVER (ORDER BY placed_at) AS prev_order,
       lead(placed_at) OVER (ORDER BY placed_at) AS next_order
FROM orders;



-- delta vs previous row: days between consecutive orders
SELECT id, placed_at,
       julianday(placed_at) - julianday(lag(placed_at) OVER (ORDER BY placed_at))
         AS days_since_previous
FROM orders;



-- 3-arg form: lag(col, n, default) — no NULL at the edges
SELECT id, placed_at,
       lag(placed_at, 1, '(first)') OVER (ORDER BY placed_at) AS prev_order
FROM orders;



-- per-partition: gap between each CUSTOMER's own consecutive orders
SELECT customer_id, id AS order_id, placed_at,
       julianday(placed_at) -
       julianday(lag(placed_at) OVER (PARTITION BY customer_id ORDER BY placed_at))
         AS days_since_their_last
FROM orders;



-- month-over-month change in order count (lag over an aggregated CTE)
WITH monthly AS (
  SELECT strftime('%Y-%m', placed_at) AS month, count(*) AS orders
  FROM orders
  GROUP BY month
)
SELECT month, orders,
       orders - lag(orders) OVER (ORDER BY month) AS change
FROM monthly;



-- first_value(): compare each row to the window's first row
SELECT name, price,
       first_value(price) OVER (PARTITION BY category_id ORDER BY price)
         AS category_cheapest,
       round(price / first_value(price)
         OVER (PARTITION BY category_id ORDER BY price), 1) AS x_cheapest
FROM products;



-- Practice
-- Q1. Each order's total next to the customer's PREVIOUS order total
--     (join order_totals, partition by customer).
-- Q2. Month-over-month revenue change in absolute and % terms.
-- Q3. For each customer: days between their first and last order
--     (first_value + last order via max — or two windows).

-- 04. Frames — running totals, moving averages, ROWS/RANGE, LAST_VALUE
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- adding ORDER BY to an aggregate window makes it CUMULATIVE:
-- default frame = RANGE UNBOUNDED PRECEDING TO CURRENT ROW
SELECT t.order_id, t.placed_at, t.total,
       round(sum(t.total) OVER (ORDER BY t.placed_at), 2) AS running_revenue
FROM order_totals t;



-- explicit frame: ROWS BETWEEN chooses by row position
SELECT order_id, placed_at, total,
       round(avg(total) OVER (ORDER BY placed_at
                              ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2)
         AS moving_avg_3
FROM order_totals;



-- ROWS vs RANGE: RANGE groups PEER rows (equal ORDER BY values) together
-- — with duplicate dates a RANGE frame includes all peers at once
SELECT customer_id, placed_at,
       count(*) OVER (ORDER BY customer_id ROWS  UNBOUNDED PRECEDING) AS by_rows,
       count(*) OVER (ORDER BY customer_id RANGE UNBOUNDED PRECEDING) AS by_range
FROM orders;



-- THE last_value gotcha: with the default frame the window ends at the
-- CURRENT row, so last_value() just returns the current row's value
SELECT name, price,
       last_value(price) OVER (PARTITION BY category_id ORDER BY price)
         AS broken_max,
       last_value(price) OVER (PARTITION BY category_id ORDER BY price
                               ROWS BETWEEN UNBOUNDED PRECEDING
                                        AND UNBOUNDED FOLLOWING)
         AS real_max
FROM products;



-- running share: cumulative % of lifetime revenue, biggest orders first
SELECT order_id, total,
       round(100.0 * sum(total) OVER (ORDER BY total DESC)
             / sum(total) OVER (), 1) AS cumulative_pct
FROM order_totals;



-- FILTER works on window aggregates too
SELECT id, placed_at, status,
       count(*) FILTER (WHERE status = 'delivered')
         OVER (ORDER BY placed_at) AS delivered_so_far
FROM orders;



-- Practice
-- Q1. Running count of signups over customers ordered by signed_up.
-- Q2. 2-order moving average of each CUSTOMER's totals (partition +
--     frame together).
-- Q3. Using cumulative_pct above: which orders make up the first 80%
--     of revenue?
-- Q4. Demonstrate ROWS vs RANGE with orders sharing the same
--     placed_at month as the ORDER BY key.

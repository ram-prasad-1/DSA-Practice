-- 03. Derived tables — subqueries in FROM
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- a subquery in FROM acts as a temporary table for this query;
-- give it an alias and select from it
SELECT month, orders
FROM (SELECT strftime('%Y-%m', placed_at) AS month, count(*) AS orders
      FROM orders
      GROUP BY month)
WHERE orders >= 2;



-- aggregate of an aggregate: average spend needs two levels
SELECT round(avg(spend), 2) AS avg_customer_spend
FROM (SELECT customer_id, sum(total) AS spend
      FROM order_totals
      GROUP BY customer_id);



-- joining a derived table: order counts back onto customers
SELECT c.name, coalesce(oc.n, 0) AS orders
FROM customers c
LEFT JOIN (SELECT customer_id, count(*) AS n
           FROM orders
           GROUP BY customer_id) oc ON oc.customer_id = c.id;



-- top-N inside, detail outside: the 3 biggest orders with customer names
SELECT c.name, top3.order_id, top3.total
FROM (SELECT order_id, customer_id, total
      FROM order_totals
      ORDER BY total DESC
      LIMIT 3) top3
JOIN customers c ON c.id = top3.customer_id;



-- Practice
-- Q1. Per country: the average of each customer's total spend.
-- Q2. Products above the median price (hint: derived table with
--     ORDER BY + LIMIT 1 OFFSET (count/2) for the median).
-- Q3. Month-level report joined back: each order with its month's
--     order count.

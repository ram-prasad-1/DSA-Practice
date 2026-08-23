-- 05. Conditional expressions — CASE WHEN, IIF
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- CASE is SQL's if/else expression: returns a value per row, usable
-- anywhere an expression fits. IIF(cond, a, b) = 2-way shorthand.



-- searched CASE: first true WHEN wins; omitted ELSE returns NULL
SELECT name, in_stock,
       CASE
         WHEN in_stock = 0  THEN 'out of stock'
         WHEN in_stock < 10 THEN 'low'
         ELSE 'in stock'
       END AS availability
FROM products;



-- simple CASE: compares one expression against values
SELECT id, status,
       CASE status
         WHEN 'pending'   THEN 'awaiting warehouse'
         WHEN 'shipped'   THEN 'on the way'
         WHEN 'delivered' THEN 'done'
         WHEN 'cancelled' THEN 'refund if paid'
       END AS next_action
FROM orders;



-- IIF(condition, then, else)
SELECT name,
       iif(city IS NULL, 'city unknown', city)           AS city,
       iif(country = 'USA', 'domestic', 'international') AS shipping_zone
FROM customers;



-- CASE in ORDER BY: custom sort orders
SELECT id, status, placed_at
FROM orders
ORDER BY CASE status
  WHEN 'pending'   THEN 1
  WHEN 'shipped'   THEN 2
  WHEN 'delivered' THEN 3
  WHEN 'cancelled' THEN 4
END, placed_at;



-- CASE in WHERE: cheap products must be in stock, expensive always shown
SELECT name, price, in_stock
FROM products
WHERE CASE WHEN price < 100 THEN in_stock > 0 ELSE 1 END;



-- pivot-style counting: CASE inside an aggregate turns rows into columns
SELECT count(CASE WHEN status = 'pending'   THEN 1 END) AS pending,
       count(CASE WHEN status = 'shipped'   THEN 1 END) AS shipped,
       count(CASE WHEN status = 'delivered' THEN 1 END) AS delivered,
       count(CASE WHEN status = 'cancelled' THEN 1 END) AS cancelled
FROM orders;



-- Practice
-- Q1. Label each product 'budget' (< 50), 'mid-range' (< 250), or 'premium'.
-- Q2. Per order (order_totals): shipping of 0 for totals >= 300, else 9.99.
-- Q3. Sort products: out-of-stock first, then by price descending.
-- Q4. One row counting UK vs USA vs other customers.

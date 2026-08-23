-- 01. INNER JOIN — combining rows that match on both sides
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- INNER JOIN keeps only rows with a match on BOTH sides
-- (bare JOIN means INNER JOIN)
SELECT o.id AS order_id, c.name AS customer, o.placed_at, o.status
FROM orders o
JOIN customers c ON c.id = o.customer_id;



-- table aliases (o, c) keep multi-table queries readable;
-- qualify columns to avoid ambiguity (both tables have an 'id')
SELECT p.name AS product, cat.name AS category, p.price
FROM products p
INNER JOIN categories cat ON cat.id = p.category_id;



-- join + WHERE: match first, then filter
SELECT c.name, o.id AS order_id, o.status
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.status = 'pending';



-- extra conditions can live in the ON clause too
SELECT c.name, o.id AS order_id
FROM orders o
JOIN customers c ON c.id = o.customer_id AND c.country = 'USA';
-- for INNER joins, ON vs WHERE placement gives the same result
-- (NOT true for LEFT JOIN — see file 02)



-- join + GROUP BY: revenue per customer name
SELECT c.name, count(DISTINCT o.id) AS orders, sum(oi.quantity * oi.unit_price) AS spend
FROM customers c
JOIN orders o  ON o.customer_id = c.id
JOIN order_items oi ON oi.order_id = o.id
GROUP BY c.id;



-- gotcha: NATURAL JOIN matches on ALL same-named columns.
-- orders.id and customers.id are both named 'id', so this joins
-- order.id = customer.id — syntactically fine, semantically nonsense
SELECT count(*) FROM orders NATURAL JOIN customers;
-- moral: always write the join condition explicitly with ON



-- Practice
-- Q1. Every order item as: customer name, product name, quantity.
-- Q2. Orders placed by UK customers.
-- Q3. Product name + category name for products with a discount set.
-- Q4. Total units sold per category name.

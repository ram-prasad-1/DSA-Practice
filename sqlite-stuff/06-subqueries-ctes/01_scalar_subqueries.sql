-- 01. Scalar subqueries — a query used as a single value
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- a scalar subquery returns exactly one row, one column — usable
-- anywhere a value fits
SELECT name, price,
       (SELECT round(avg(price), 2) FROM products) AS avg_price
FROM products;



-- classic: rows above the average
SELECT name, price
FROM products
WHERE price > (SELECT avg(price) FROM products);



-- the most recent order (subquery in WHERE against max)
SELECT id, placed_at
FROM orders
WHERE placed_at = (SELECT max(placed_at) FROM orders);



-- CORRELATED subquery: refers to the outer row, re-evaluated per row —
-- each product compared to ITS OWN category's average
SELECT p.name, p.price,
       (SELECT round(avg(p2.price), 2)
        FROM products p2
        WHERE p2.category_id = p.category_id) AS category_avg
FROM products p;

SELECT p.name, p.price
FROM products p
WHERE p.price > (SELECT avg(p2.price)
                 FROM products p2
                 WHERE p2.category_id = p.category_id);



-- if a scalar subquery matches no rows it yields NULL (not an error)
SELECT (SELECT name FROM customers WHERE country = 'Mars') AS nobody;



-- SQLite has no ANY/SOME/ALL quantifiers — rewrite with min/max:
-- "price > ALL cables" becomes "price > (SELECT max(price) ...)"
SELECT name, price
FROM products
WHERE price > (SELECT max(price) FROM products WHERE category_id = 5);



-- Practice
-- Q1. Customers who signed up before the average signup date.
-- Q2. Each order with its share of lifetime revenue
--     (order_totals.total / total revenue).
-- Q3. Products priced within 10% of their category's max price
--     (correlated subquery).

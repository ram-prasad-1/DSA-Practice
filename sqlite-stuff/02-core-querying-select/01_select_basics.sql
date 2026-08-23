-- 01. SELECT basics — projection, aliases, expressions, DISTINCT
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- SELECT retrieves rows; "projection" = choosing which columns appear.
-- SELECT * = every column. Fine for exploring, avoid in app code.
SELECT * FROM customers;
SELECT * FROM products;



-- specific columns
SELECT name, email FROM customers;
SELECT name, price, in_stock FROM products;



-- aliases: AS renames a column in the output only (AS itself is optional)
SELECT name AS product, price AS unit_price FROM products;
SELECT name product, price unit_price FROM products;



-- calculated columns: any expression is allowed
SELECT name, price, in_stock,
       price * in_stock       AS stock_value,
       round(price * 1.18, 2) AS price_with_tax
FROM products;



-- || concatenates strings
SELECT name || ' <' || email || '>' AS contact FROM customers;



-- coalesce() substitutes a fallback for NULL (city can be NULL)
SELECT name, coalesce(city, 'unknown') AS city FROM customers;



-- SELECT without FROM evaluates plain expressions
SELECT 5 * 12, upper('sqlite'), sqlite_version();



-- DISTINCT removes duplicate rows — applies to the whole selected row
SELECT country FROM customers;
SELECT DISTINCT country FROM customers;
SELECT DISTINCT country, city FROM customers;



-- Practice
-- Q1. Each product's name and price in cents (price * 100) as price_cents.
-- Q2. The distinct order statuses from the orders table.
-- Q3. One 'summary' column per customer like:
--     'Ada Lovelace signed up on 2024-01-15 (UK)'.

-- 03. ORDER BY — sorting: ASC/DESC, multiple keys, NULLs, COLLATE
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- ORDER BY sorts the final result; without it row order is UNDEFINED.



-- ASC is the default
SELECT name, price FROM products ORDER BY price;
SELECT name, price FROM products ORDER BY price DESC;



-- multiple keys: ties on the first key break on the second
SELECT category_id, name, price FROM products ORDER BY category_id, price DESC;
SELECT country, name, signed_up FROM customers ORDER BY country, signed_up;



-- by alias, expression, or column position
SELECT name, price * in_stock AS stock_value FROM products ORDER BY stock_value DESC;
SELECT name FROM products ORDER BY length(name);
SELECT name, price FROM products ORDER BY 2 DESC;   -- by position: fragile, avoid



-- NULLs sort FIRST by default; override with NULLS FIRST/LAST (3.30+)
SELECT name, city FROM customers ORDER BY city;
SELECT name, city FROM customers ORDER BY city NULLS LAST;
SELECT name, city FROM customers ORDER BY city DESC NULLS LAST;



-- COLLATE controls text comparison; default BINARY is case-sensitive,
-- so ALL uppercase letters sort before lowercase ('Z' < 'a')
SELECT column1 AS word
FROM (VALUES ('banana'), ('Apple'), ('cherry'), ('Date'))
ORDER BY word;                       -- Apple, Date, banana, cherry

SELECT column1 AS word
FROM (VALUES ('banana'), ('Apple'), ('cherry'), ('Date'))
ORDER BY word COLLATE NOCASE;        -- human-friendly A→Z



-- Practice
-- Q1. Orders by status alphabetically, newest first within a status.
-- Q2. Customers alphabetically by city, unknown-city ones last.
-- Q3. The single most expensive product as the first row (then LIMIT 1).
-- Q4. Products by in_stock ascending, ties broken by price descending.

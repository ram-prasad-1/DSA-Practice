-- 02. WHERE filtering — comparisons, logic, BETWEEN, IN, LIKE, GLOB, IS NULL
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- WHERE keeps rows where the condition is TRUE; FALSE or NULL rows are dropped.



-- comparison operators: = != <> < > <= >= (SQLite also accepts ==)
SELECT name, price FROM products WHERE price > 100;
SELECT name, country FROM customers WHERE country = 'USA';
SELECT name, price FROM products WHERE price <= 50;
SELECT id, status FROM orders WHERE status <> 'delivered';



-- AND / OR / NOT; AND binds tighter than OR — parenthesize to be explicit
SELECT name, price, in_stock FROM products WHERE price < 100 AND in_stock > 0;

SELECT name, country, signed_up
FROM customers
WHERE (country = 'UK' OR country = 'USA') AND signed_up >= '2024-03-01';

SELECT name FROM products WHERE NOT in_stock = 0;



-- BETWEEN a AND b is inclusive; works on ISO-8601 date text too
SELECT name, price FROM products WHERE price BETWEEN 50 AND 300;
SELECT name, price FROM products WHERE price NOT BETWEEN 50 AND 300;
SELECT id, placed_at FROM orders WHERE placed_at BETWEEN '2024-04-01' AND '2024-06-30';



-- IN: membership in a list (or a subquery, later)
SELECT name, country FROM customers WHERE country IN ('UK', 'Finland', 'Japan');
SELECT id, status FROM orders WHERE status IN ('pending', 'shipped');
SELECT name FROM products WHERE category_id NOT IN (5);



-- LIKE: % = any run of chars, _ = one char.
-- SQLite LIKE is case-insensitive for ASCII ('usb%' matches 'USB-C Cable 2m').
SELECT name FROM products WHERE name LIKE 'usb%';
SELECT name FROM products WHERE name LIKE '%cable%';
SELECT name FROM products WHERE name LIKE '_DMI%';
SELECT name, email FROM customers WHERE email LIKE '%@example.com';



-- ESCAPE matches a literal % or _
SELECT '50%_off' LIKE '50\%%' ESCAPE '\' AS has_percent;



-- GLOB: Unix-glob match with * and ?, case-SENSITIVE (SQLite-specific)
SELECT name FROM products WHERE name GLOB 'USB*';
SELECT name FROM products WHERE name GLOB 'usb*';   -- no rows: case matters



-- IS NULL / IS NOT NULL are the only correct NULL tests;
-- '= NULL' never matches (NULL compares as unknown, not equal)
SELECT name, city FROM customers WHERE city IS NULL;
SELECT name, city FROM customers WHERE city IS NOT NULL;
SELECT name FROM customers WHERE city = NULL;       -- always 0 rows!



-- gotcha: comparisons silently drop NULL rows —
-- city != 'London' does NOT include customers with NULL city
SELECT name, city FROM customers WHERE city != 'London';
SELECT name, city FROM customers WHERE city != 'London' OR city IS NULL;



-- Practice
-- Q1. Products that are out of stock (in_stock = 0).
-- Q2. Keyboards or mice (category_id 1 or 2) priced under 100.
-- Q3. Orders placed in 2024-05 or later that are not cancelled.
-- Q4. Products whose name contains 'mouse' or 'monitor' (any case).
-- Q5. Product names starting with a digit (hint: GLOB '[0-9]*').
-- Q6. Customers whose city is unknown OR outside the USA.

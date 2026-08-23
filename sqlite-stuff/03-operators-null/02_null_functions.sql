-- 02. NULL functions & NULL behavior — COALESCE, IFNULL, NULLIF, aggregates, NOT IN
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- coalesce(a, b, ...): first non-NULL argument
SELECT name, coalesce(city, 'no city on file') AS city FROM customers;
SELECT name, coalesce(discount, 0) AS effective_discount FROM products;



-- ifnull(a, b): 2-argument coalesce
SELECT name, ifnull(discount, 0) AS effective_discount FROM products;



-- nullif(a, b): NULL if a = b, else a — turns sentinel values back into NULL.
-- discount 0 means "decided: none"; nullif folds it into NULL for reporting
SELECT name, discount, nullif(discount, 0) AS real_discount FROM products;



-- scalar max()/min() with 2+ args return NULL if ANY argument is NULL
SELECT max(0.10, NULL), min(5, 3, NULL), max(0.10, 0.05);
SELECT name, max(coalesce(discount, 0), 0.05) AS floor_discount FROM products;



-- aggregates IGNORE NULLs: count(col) skips them, count(*) doesn't
SELECT count(*) AS all_products,
       count(discount) AS with_discount_set
FROM products;

-- avg() divides by non-NULL rows only — very different from coalescing to 0
SELECT avg(discount)              AS avg_where_set,
       avg(coalesce(discount, 0)) AS avg_over_all
FROM products;



-- NULL propagates through expressions and concatenation
SELECT name, 'city: ' || city AS label FROM customers;   -- NULL city → NULL label
SELECT name, 'city: ' || coalesce(city, '?') AS label FROM customers;



-- gotcha: NOT IN + NULL = silent empty result.
-- referred_by contains NULLs, so 'id NOT IN (...)' is never true
SELECT name FROM customers
WHERE id NOT IN (SELECT referred_by FROM customers);      -- 0 rows!

-- fix: exclude NULLs from the list (NOT EXISTS also works — later section)
SELECT name FROM customers
WHERE id NOT IN (SELECT referred_by FROM customers WHERE referred_by IS NOT NULL);



-- Practice
-- Q1. Each product's discounted price: price * (1 - discount), treating
--     NULL discount as 0.
-- Q2. Customers shown as 'name (city)' with '(unknown)' when city is NULL.
-- Q3. Count customers with and without a referrer in one row.
-- Q4. Average discount treating both NULL and 0 as "no discount"
--     (hint: nullif + avg skips NULLs).

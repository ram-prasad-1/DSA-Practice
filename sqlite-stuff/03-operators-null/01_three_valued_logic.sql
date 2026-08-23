-- 01. Three-valued logic — NULL is unknown, not a value
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- comparing anything with NULL yields NULL (unknown), never true or false
SELECT NULL = NULL, NULL <> 5, NULL > 3, 'a' = NULL;



-- logic with unknowns: AND/OR only resolve when the answer can't change
-- (0 AND anything = 0; 1 OR anything = 1; otherwise NULL stays NULL)
SELECT NULL AND 0, NULL AND 1, NULL OR 1, NULL OR 0, NOT NULL;



-- WHERE keeps only TRUE rows — unknown rows are dropped,
-- so both of these silently exclude products with NULL discount
SELECT name, discount FROM products WHERE discount > 0;
SELECT name, discount FROM products WHERE NOT discount > 0;



-- IS NULL / IS NOT NULL: the only reliable NULL tests
SELECT name, discount FROM products WHERE discount IS NULL;
SELECT name, referred_by FROM customers WHERE referred_by IS NOT NULL;



-- IS / IS NOT also work as null-safe equality (NULL IS NULL → 1)
SELECT NULL IS NULL, 5 IS NULL, 5 IS 5, NULL IS 5;



-- IS [NOT] DISTINCT FROM (3.39+): standard-SQL null-safe comparison —
-- treats two NULLs as "not distinct" (equal)
SELECT name, discount
FROM products
WHERE discount IS NOT DISTINCT FROM NULL;



-- compare two nullable columns safely: plain = misses NULL pairs
SELECT a.name, b.name
FROM customers a, customers b
WHERE a.id < b.id AND a.city IS NOT DISTINCT FROM b.city;



-- Practice
-- Q1. Predict, then run: SELECT NULL = '', NULL AND NULL, 0 OR NULL;
-- Q2. Products where discount is 0 or unset (two conditions).
-- Q3. Customers who were NOT referred by customer 2 — including the
--     never-referred ones (the naive <> 2 misses them).

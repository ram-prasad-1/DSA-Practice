-- 04. Casting & type coercion — CAST, typeof, implicit affinity
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- CAST(x AS type) is the only cast syntax (no Postgres-style x::type)
SELECT CAST('42' AS INTEGER), CAST(3.9 AS INTEGER), CAST(42 AS TEXT), CAST('3.14' AS REAL);



-- CAST parses a numeric PREFIX and never errors — silent data mangling
SELECT CAST('42abc' AS INTEGER),   -- 42
       CAST('abc' AS INTEGER),     -- 0 (!)
       CAST('' AS INTEGER);        -- 0



-- CAST to INTEGER truncates toward zero (round() rounds instead)
SELECT CAST(2.7 AS INTEGER), CAST(-2.7 AS INTEGER), round(2.7), round(-2.7);



-- typeof() shows the storage class of any value
SELECT typeof(1), typeof(1.5), typeof('x'), typeof(NULL), typeof(X'FF');
SELECT name, typeof(price), typeof(in_stock), typeof(discount) FROM products LIMIT 3;



-- arithmetic coerces text to numbers; || coerces numbers to text
SELECT '5' + 1, '5' || 1, '5e2' + 0, 'abc' + 1;   -- 6, '51', 500.0, 1 (!)



-- column affinity converts compatible literals on comparison:
-- price is REAL, so the TEXT '399' still matches 399.0
SELECT name, price FROM products WHERE price = '399';

-- but expressions have NO affinity — text stays text
SELECT '10' = 10, CAST('10' AS INTEGER) = 10;



-- Practice
-- Q1. Predict typeof(price + 0), typeof(price || ''), then verify.
-- Q2. in_stock as a zero-padded 4-char text (hint: printf('%04d', ...)).
-- Q3. Why does '2' > '10' return 1? Fix it with CAST so it compares
--     numerically.

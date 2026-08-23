-- 05. Literals & quoting — the classic SQLite footguns
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- strings take SINGLE quotes; escape a quote by doubling it
SELECT 'it''s a keyboard' AS msg;



-- there are NO backslash escapes — 'a\nb' is 4 chars; use char(10) for newline
SELECT length('a\nb'), 'a' || char(10) || 'b' AS real_newline;



-- identifiers (columns/tables) take double quotes; SQLite also accepts
-- MySQL backticks and SQL Server brackets for compatibility
SELECT "name", `name`, [name] FROM customers LIMIT 2;



-- THE footgun: a double-quoted token that matches NO column silently
-- becomes a string literal instead of an error
SELECT * FROM customers WHERE country = "Wonderland";   -- runs! compares to string
SELECT * FROM customers WHERE country = "country";      -- column = itself → ALL rows
-- moral: always single-quote strings; 'Wonderland' vs "Wonderland" differ



-- blob literals: X'hex' — a distinct storage class
SELECT X'414243', typeof(X'414243'), length(X'414243'), hex('ABC');



-- TRUE/FALSE are just aliases for 1 and 0 (no boolean type)
SELECT TRUE, FALSE, typeof(TRUE), TRUE + TRUE;
SELECT name FROM products WHERE (in_stock > 0) = TRUE;



-- SQLite also accepts non-standard == for equality (portability hazard)
SELECT name FROM customers WHERE country == 'UK';



-- Practice
-- Q1. Select the literal string: They said "hello" — it's fine
-- Q2. Predict: WHERE name = "email" on customers — how many rows and why?
-- Q3. Build a 2-line address label using char(10) between city and country.
-- Q4. What does typeof(X'') return, and what is its length?

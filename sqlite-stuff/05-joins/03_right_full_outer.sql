-- 03. RIGHT and FULL OUTER JOIN (3.39+, 2022) — and emulating them
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- RIGHT JOIN keeps every RIGHT row — it is just LEFT JOIN with
-- the sides swapped, so it is rarely needed in practice
SELECT p.name AS product, c.name AS category
FROM products p
RIGHT JOIN categories c ON c.id = p.category_id;   -- Webcams appears, product NULL

-- identical result, written as the more common LEFT JOIN
SELECT p.name AS product, c.name AS category
FROM categories c
LEFT JOIN products p ON p.category_id = c.id;



-- FULL OUTER JOIN keeps unmatched rows from BOTH sides
SELECT c.name AS category, p.name AS product
FROM categories c
FULL OUTER JOIN products p ON p.category_id = c.id;
-- here only categories can be orphaned (category_id is NOT NULL),
-- so this equals the LEFT JOIN — but with optional FKs both sides can orphan



-- pre-3.39 emulation of FULL OUTER: LEFT JOIN + the right side's
-- unmatched rows via UNION ALL
SELECT c.name AS category, p.name AS product
FROM categories c
LEFT JOIN products p ON p.category_id = c.id
UNION ALL
SELECT c.name, p.name
FROM products p
LEFT JOIN categories c ON c.id = p.category_id
WHERE c.id IS NULL;



-- check your SQLite version supports RIGHT/FULL (needs 3.39+)
SELECT sqlite_version();



-- Practice
-- Q1. Write "categories with their products" three ways: LEFT, RIGHT,
--     FULL OUTER — confirm all three return the same rows here.
-- Q2. Using FULL OUTER JOIN between customers and orders, find rows
--     unmatched on either side. Which side can actually be unmatched
--     in this schema, and why?
-- Q3. Emulate Q2's FULL OUTER with LEFT JOIN + UNION ALL.

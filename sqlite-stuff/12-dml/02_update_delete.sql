-- 02. UPDATE and DELETE — targeted changes, UPDATE FROM, safe habits
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (works on ids >= 9000; cleans up first, so it re-runs safely)

DELETE FROM products WHERE id >= 9000;
INSERT INTO products (id, category_id, name, price, in_stock, discount) VALUES
  (9001, 5, 'Cable Organizer',   12.00, 40, NULL),
  (9002, 5, 'Velcro Ties 50pk',   8.50, 200, 0.05),
  (9003, 2, 'Mouse Bungee',      19.00, 0,  NULL);



-- UPDATE ... SET ... WHERE: no WHERE = EVERY row. Habit: run the WHERE
-- as a SELECT first
SELECT id, name, price FROM products WHERE id >= 9000 AND category_id = 5;
UPDATE products SET price = price * 0.9 WHERE id >= 9000 AND category_id = 5;
SELECT changes() AS repriced;



-- multiple columns, computed from current values
UPDATE products
SET in_stock = in_stock + 25,
    discount = coalesce(discount, 0)
WHERE id = 9003;
SELECT * FROM products WHERE id = 9003;



-- UPDATE ... FROM (3.33+): update using values joined from another table
-- (here: sync each 9000-range product's discount to its category average)
UPDATE products
SET discount = round(src.avg_discount, 2)
FROM (SELECT category_id, avg(coalesce(discount, 0)) AS avg_discount
      FROM products WHERE id < 9000
      GROUP BY category_id) AS src
WHERE products.category_id = src.category_id AND products.id >= 9000;
SELECT id, name, discount FROM products WHERE id >= 9000;



-- DELETE ... WHERE, same SELECT-first habit
SELECT count(*) FROM products WHERE id >= 9000 AND in_stock = 0;
DELETE FROM products WHERE id >= 9000 AND in_stock = 0;
SELECT changes() AS deleted;



-- there is NO TRUNCATE: bare 'DELETE FROM t' clears the table, and
-- SQLite applies a fast "truncate optimization" automatically.
-- 'DELETE/UPDATE ... LIMIT' needs a compile-time option — portable form:
DELETE FROM products
WHERE id IN (SELECT id FROM products WHERE id >= 9000 ORDER BY id LIMIT 1);
SELECT id, name FROM products WHERE id >= 9000;      -- one fewer



-- Practice
-- Q1. Give every never-discounted (NULL) product in the 9000 range a
--     0.10 discount in one UPDATE.
-- Q2. UPDATE ... FROM: set each 9000-range product's price to 1.1 ×
--     the average price of its category (computed from id < 9000 rows).
-- Q3. Delete the cheapest remaining 9000-range product using the
--     IN + ORDER BY + LIMIT pattern.

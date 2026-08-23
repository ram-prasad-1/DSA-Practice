-- 01. INSERT — values, multi-row, INSERT-SELECT, conflict clauses
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (this file uses ids >= 9000 and cleans them up first, so it re-runs safely)

DELETE FROM order_items WHERE order_id >= 9000;
DELETE FROM orders    WHERE id >= 9000;
DELETE FROM customers WHERE id >= 9000;
DELETE FROM products  WHERE id >= 9000;



-- plain INSERT: name the columns (never rely on column order)
INSERT INTO customers (id, name, email, city, country, signed_up)
VALUES (9001, 'Edsger Dijkstra', 'edsger@example.com', 'Nuenen', 'Netherlands', '2024-09-10');



-- multi-row VALUES: one statement, one transaction — much faster than many
INSERT INTO customers (id, name, email, city, country, signed_up) VALUES
  (9002, 'Donald Knuth', 'don@example.com',  'Stanford', 'USA', '2024-09-11'),
  (9003, 'Radia Perlman','radia@example.com', NULL,      'USA', '2024-09-12');



-- omitted columns take their DEFAULT (or NULL); INTEGER PRIMARY KEY
-- auto-assigns when omitted
INSERT INTO products (id, category_id, name, price)
VALUES (9001, 5, 'Cable Organizer', 12.00);
SELECT id, name, in_stock, discount FROM products WHERE id = 9001;   -- in_stock: DEFAULT 0



-- INSERT ... SELECT: copy/transform rows from a query
INSERT INTO orders (id, customer_id, placed_at, status)
SELECT 9000 + row_number() OVER (ORDER BY id), id, '2024-09-15', 'pending'
FROM customers
WHERE id >= 9000;
SELECT * FROM orders WHERE id >= 9000;



-- conflict clauses: INSERT OR IGNORE skips constraint violations...
INSERT OR IGNORE INTO customers (id, name, email, city, country, signed_up)
VALUES (9001, 'Impostor', 'edsger@example.com', NULL, 'USA', '2024-09-20');
SELECT changes() AS inserted;                    -- 0: duplicate id/email ignored

-- ...INSERT OR REPLACE deletes the old row and inserts the new one
-- (DANGER: it is a delete+insert, not an update — defaults reset,
--  ON DELETE CASCADE fires; usually you want UPSERT — see file 03)
INSERT OR REPLACE INTO customers (id, name, email, city, country, signed_up)
VALUES (9001, 'Edsger W. Dijkstra', 'edsger@example.com', 'Nuenen', 'Netherlands', '2024-09-10');
SELECT name FROM customers WHERE id = 9001;



-- Practice
-- Q1. Insert 3 products in one statement into a new 'Docks' category
--     (insert the category first, use last_insert_rowid()).
-- Q2. Copy every UK customer into a 9100+ id range with '-copy'
--     appended to the email (INSERT-SELECT must keep email UNIQUE).
-- Q3. Show that INSERT OR REPLACE on order id 1001 would delete its
--     order_items (count them, don't actually do it — or do, then
--     re-run 00_schema).

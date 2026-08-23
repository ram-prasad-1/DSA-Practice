-- 03. UPSERT & RETURNING — ON CONFLICT DO UPDATE, excluded., RETURNING
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (works on ids >= 9000; cleans up first, so it re-runs safely)

DELETE FROM customers WHERE id >= 9000;



-- UPSERT: insert, or update the existing row on conflict.
-- the conflict target names the UNIQUE constraint that may fire
INSERT INTO customers (id, name, email, city, country, signed_up)
VALUES (9001, 'Ada L.', 'ada-alt@example.com', 'London', 'UK', '2024-09-01')
ON CONFLICT (email) DO UPDATE SET name = excluded.name, city = excluded.city;

-- run a "second import" of the same email: updates instead of failing.
-- excluded.* = the row that FAILED to insert
INSERT INTO customers (id, name, email, city, country, signed_up)
VALUES (9002, 'Ada Byron-Lovelace', 'ada-alt@example.com', 'Oxford', 'UK', '2024-09-05')
ON CONFLICT (email) DO UPDATE SET name = excluded.name, city = excluded.city;
SELECT id, name, city FROM customers WHERE email = 'ada-alt@example.com';
-- note: id stayed 9001 — unlike INSERT OR REPLACE, the row survives



-- DO NOTHING: idempotent inserts (safe re-imports)
INSERT INTO customers (id, name, email, city, country, signed_up)
VALUES (9003, 'Duplicate Ada', 'ada-alt@example.com', NULL, 'UK', '2024-09-06')
ON CONFLICT (email) DO NOTHING;
SELECT changes() AS inserted;        -- 0



-- conditional upsert: only overwrite when the new data is fresher
INSERT INTO customers (id, name, email, city, country, signed_up)
VALUES (9001, 'Ada (stale import)', 'ada-alt@example.com', 'London', 'UK', '2024-08-01')
ON CONFLICT (email) DO UPDATE SET name = excluded.name
WHERE excluded.signed_up > customers.signed_up;
SELECT name FROM customers WHERE email = 'ada-alt@example.com';   -- unchanged



-- RETURNING (3.35+): read back what INSERT/UPDATE/DELETE actually did —
-- no second query, no last_insert_rowid() dance
INSERT INTO customers (name, email, city, country, signed_up)
VALUES ('Barbara J.', 'barbara-j@example.com', 'Cambridge', 'USA', '2024-09-07')
RETURNING id, name;

UPDATE customers SET city = 'Boston'
WHERE email = 'barbara-j@example.com'
RETURNING id, name, city;

DELETE FROM customers WHERE email = 'barbara-j@example.com'
RETURNING id AS deleted_id, name AS deleted_name;



-- counters idiom: insert-or-increment in one statement
DROP TABLE IF EXISTS page_hits;
CREATE TABLE page_hits (page TEXT PRIMARY KEY, hits INTEGER NOT NULL DEFAULT 1);
INSERT INTO page_hits (page) VALUES ('/home')
ON CONFLICT (page) DO UPDATE SET hits = hits + 1;
INSERT INTO page_hits (page) VALUES ('/home')
ON CONFLICT (page) DO UPDATE SET hits = hits + 1
RETURNING page, hits;



-- Practice
-- Q1. Upsert a product by a UNIQUE name (add the unique index first:
--     CREATE UNIQUE INDEX ... ON products(name)) — update price on conflict.
-- Q2. Re-run this whole file: why do the results stay stable?
-- Q3. Bulk-upsert: INSERT ... SELECT ... ON CONFLICT to raise every
--     9000-range customer's signed_up to the newer of old/new.
-- Q4. Use RETURNING to delete cancelled orders and list what went
--     (on a scratch copy: re-run 00_schema after!).

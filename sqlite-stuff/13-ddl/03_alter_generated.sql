-- 03. ALTER TABLE & generated columns — what SQLite can and cannot alter
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (creates scratch table: suppliers)

DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS vendors;       -- this file renames suppliers → vendors
DROP TABLE IF EXISTS vendors_new;
CREATE TABLE suppliers (
  id   INTEGER PRIMARY KEY,
  name TEXT NOT NULL
);
INSERT INTO suppliers (name) VALUES ('Keychron'), ('Logitech');



-- the four things ALTER TABLE can do:
ALTER TABLE suppliers RENAME TO vendors;                    -- 1. rename table
ALTER TABLE vendors RENAME COLUMN name TO vendor_name;      -- 2. rename column (3.25+)
ALTER TABLE vendors ADD COLUMN country TEXT DEFAULT '?';    -- 3. add column
ALTER TABLE vendors ADD COLUMN rating REAL;
ALTER TABLE vendors DROP COLUMN rating;                     -- 4. drop column (3.35+)
SELECT * FROM vendors;

-- ADD COLUMN limits: default must be constant-ish for existing rows;
-- cannot add a PRIMARY KEY or UNIQUE column; DROP COLUMN refuses columns
-- used by indexes, PKs, or generated columns



-- everything else (change type, add/remove constraints, reorder) =
-- the documented 12-step rebuild; core of it:
CREATE TABLE vendors_new (
  id          INTEGER PRIMARY KEY,
  vendor_name TEXT NOT NULL UNIQUE,          -- the constraint we "added"
  country     TEXT NOT NULL DEFAULT '?'
);
INSERT INTO vendors_new SELECT id, vendor_name, country FROM vendors;
DROP TABLE vendors;
ALTER TABLE vendors_new RENAME TO vendors;
SELECT * FROM vendors;
-- in real life: wrap in a transaction, PRAGMA foreign_keys=OFF around it,
-- recreate indexes/triggers/views, then PRAGMA foreign_key_check



-- GENERATED columns (3.31+): computed from other columns.
-- VIRTUAL computes on read (free storage); STORED computes on write
ALTER TABLE vendors ADD COLUMN name_upper TEXT
  GENERATED ALWAYS AS (upper(vendor_name)) VIRTUAL;
SELECT vendor_name, name_upper FROM vendors;
-- (STORED cannot be added via ALTER — only in CREATE TABLE)

DROP TABLE IF EXISTS line_items_demo;
CREATE TABLE line_items_demo (
  qty        INTEGER NOT NULL,
  unit_price REAL NOT NULL,
  line_total REAL GENERATED ALWAYS AS (qty * unit_price) STORED
);
INSERT INTO line_items_demo (qty, unit_price) VALUES (3, 9.99), (2, 49.00);
SELECT * FROM line_items_demo;
-- INSERT INTO line_items_demo (qty, unit_price, line_total) VALUES (1, 1, 5);
--   → uncomment: cannot INSERT into generated column



-- Practice
-- Q1. Add a 'website' column to vendors with DEFAULT NULL, then rename it.
-- Q2. Rebuild vendors to change country's default from '?' to 'unknown'
--     (12-step pattern above).
-- Q3. Add a VIRTUAL generated column to line_items_demo:
--     total_with_tax = line_total * 1.18.

-- 01. CREATE TABLE & constraints — PK, FK, UNIQUE, CHECK, DEFAULT
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (creates scratch tables: warehouses, stock_moves)

PRAGMA foreign_keys = ON;   -- ⚠ OFF by default, per connection!

DROP TABLE IF EXISTS stock_moves;
DROP TABLE IF EXISTS warehouses;



-- the constraint toolbox in one table
CREATE TABLE warehouses (
  id       INTEGER PRIMARY KEY,                  -- rowid alias, auto-assigns
  code     TEXT NOT NULL UNIQUE,                 -- one per column...
  city     TEXT NOT NULL,
  capacity INTEGER NOT NULL CHECK (capacity > 0),
  opened   DATE NOT NULL DEFAULT CURRENT_DATE,
  notes    TEXT DEFAULT ('(none)'),              -- expression default in parens
  UNIQUE (city, code)                            -- ...or table-level, composite
);

INSERT INTO warehouses (code, city, capacity) VALUES ('BLR-1', 'Bengaluru', 10000);
SELECT * FROM warehouses;



-- FOREIGN KEY with actions; composite PRIMARY KEY at table level
CREATE TABLE stock_moves (
  warehouse_id INTEGER NOT NULL
               REFERENCES warehouses(id) ON DELETE CASCADE ON UPDATE CASCADE,
  product_id   INTEGER NOT NULL REFERENCES products(id) ON DELETE RESTRICT,
  moved_on     DATE NOT NULL,
  qty          INTEGER NOT NULL CHECK (qty != 0),   -- +in / -out
  PRIMARY KEY (warehouse_id, product_id, moved_on)
);

INSERT INTO stock_moves VALUES (1, 1, '2024-09-01', 50);



-- constraint violations are errors (uncomment to see each):
-- INSERT INTO warehouses (code, city, capacity) VALUES ('BLR-1', 'Delhi', 5);
--   → UNIQUE constraint failed: warehouses.code
-- INSERT INTO warehouses (code, city, capacity) VALUES ('DEL-1', 'Delhi', -5);
--   → CHECK constraint failed: capacity > 0
-- INSERT INTO stock_moves VALUES (999, 1, '2024-09-02', 10);
--   → FOREIGN KEY constraint failed (only with PRAGMA foreign_keys = ON)



-- ON DELETE CASCADE in action: deleting the warehouse removes its moves
DELETE FROM warehouses WHERE code = 'BLR-1';
SELECT count(*) AS remaining_moves FROM stock_moves;



-- deferred FKs: check at COMMIT instead of per-statement
-- (declare with: REFERENCES t(c) DEFERRABLE INITIALLY DEFERRED)



-- CREATE TABLE ... AS SELECT: copies data and column names,
-- but NO constraints, defaults, or PK
DROP TABLE IF EXISTS products_snapshot;
CREATE TABLE products_snapshot AS SELECT * FROM products;
SELECT count(*) FROM products_snapshot;
DROP TABLE products_snapshot;



-- TEMP tables live in the separate 'temp' schema: visible only to THIS
-- connection, gone when it closes — the everyday scratch tool
DROP TABLE IF EXISTS temp.restock_candidates;
CREATE TEMP TABLE restock_candidates AS
SELECT id, name FROM products WHERE in_stock = 0;
SELECT * FROM restock_candidates;
SELECT name FROM pragma_table_list WHERE schema = 'temp';
-- another connection opening play.db will NOT see this table



-- quirk: UNIQUE treats NULLs as all-distinct — a UNIQUE column happily
-- holds MANY NULLs (standard SQL, but it surprises everyone once)
DROP TABLE IF EXISTS gift_cards;
CREATE TABLE gift_cards (
  id   INTEGER PRIMARY KEY,
  code TEXT UNIQUE             -- NULL = not yet issued
);
INSERT INTO gift_cards (code) VALUES ('A1'), (NULL), (NULL), (NULL);
SELECT count(*) AS null_codes FROM gift_cards WHERE code IS NULL;    -- 3, no error!

-- want "at most one NULL"? dedupe first (classic keep-the-min pattern),
-- then a partial unique index enforces it from now on
DELETE FROM gift_cards
WHERE code IS NULL
  AND id NOT IN (SELECT min(id) FROM gift_cards WHERE code IS NULL);
DROP INDEX IF EXISTS one_unissued_card;
CREATE UNIQUE INDEX one_unissued_card ON gift_cards(code IS NULL) WHERE code IS NULL;
-- INSERT INTO gift_cards (code) VALUES (NULL);   -- uncomment → now fails



-- Practice
-- Q1. A 'coupons' table: code (PK, uppercase-only via CHECK),
--     percent 1-90, expires DATE defaulting to +30 days
--     (DEFAULT (date('now', '+30 day'))).
-- Q2. Verify each constraint fires by uncommenting bad inserts.
-- Q3. What happens to stock_moves rows on DELETE of a product with
--     ON DELETE RESTRICT? Try it.
-- Q4. Delete the 3 NULL gift cards, insert one NULL back, and show the
--     partial index now blocks a second one.

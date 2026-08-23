-- 02. rowid, INTEGER PRIMARY KEY, AUTOINCREMENT, WITHOUT ROWID
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (creates scratch tables: notes, notes_ai, kv)



-- every ordinary table has a hidden 64-bit rowid — query it by name
SELECT rowid, id, name FROM products LIMIT 3;
-- id IS the rowid here: INTEGER PRIMARY KEY makes the column an ALIAS
SELECT count(*) FROM products WHERE rowid != id;    -- 0



-- without INTEGER PRIMARY KEY the rowid is separate and unstable
-- (VACUUM can renumber it — never store bare rowids externally)
DROP TABLE IF EXISTS notes;
CREATE TABLE notes (body TEXT);
INSERT INTO notes VALUES ('alpha'), ('beta');
SELECT rowid, body FROM notes;



-- plain INTEGER PRIMARY KEY reuses freed ids: max(rowid)+1
DELETE FROM notes WHERE body = 'beta';
INSERT INTO notes VALUES ('gamma');
SELECT rowid, body FROM notes;                      -- gamma took rowid 2 again



-- AUTOINCREMENT guarantees monotonic, never-reused ids —
-- at the cost of the sqlite_sequence bookkeeping table
DROP TABLE IF EXISTS notes_ai;
CREATE TABLE notes_ai (id INTEGER PRIMARY KEY AUTOINCREMENT, body TEXT);
INSERT INTO notes_ai (body) VALUES ('alpha'), ('beta');
DELETE FROM notes_ai WHERE body = 'beta';
INSERT INTO notes_ai (body) VALUES ('gamma');
SELECT id, body FROM notes_ai;                      -- gamma is 3, 2 never reused
SELECT * FROM sqlite_sequence WHERE name = 'notes_ai';
-- rule of thumb: you rarely need AUTOINCREMENT — id reuse only matters
-- when external systems remember deleted ids



-- WITHOUT ROWID: the table is stored as a b-tree keyed on its PK —
-- good for non-integer PKs and lookup tables (no rowid exists at all)
DROP TABLE IF EXISTS kv;
CREATE TABLE kv (
  k TEXT PRIMARY KEY,
  v TEXT NOT NULL
) WITHOUT ROWID;
INSERT INTO kv VALUES ('theme', 'dark'), ('lang', 'en');
SELECT k, v FROM kv;
-- SELECT rowid FROM kv;      -- uncomment → error: no such column



-- Practice
-- Q1. Prove id reuse on 'notes' vs no-reuse on 'notes_ai' by deleting
--     and reinserting a few more rows.
-- Q2. Why must an AUTOINCREMENT column be exactly INTEGER PRIMARY KEY?
--     Try AUTOINCREMENT on a TEXT PK and read the error.
-- Q3. Make a WITHOUT ROWID composite-key table mapping
--     (customer_id, product_id) → wishlist_added DATE.

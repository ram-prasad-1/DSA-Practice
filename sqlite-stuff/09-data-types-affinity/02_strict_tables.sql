-- 02. STRICT tables (3.37+) — real type enforcement, opt-in
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (this file creates its own scratch tables: readings, flexible)



-- STRICT allows only INT, INTEGER, REAL, TEXT, BLOB, ANY as types
-- and REJECTS values that don't convert losslessly
DROP TABLE IF EXISTS readings;
CREATE TABLE readings (
  id     INTEGER PRIMARY KEY,
  sensor TEXT NOT NULL,
  value  REAL NOT NULL
) STRICT;

INSERT INTO readings (sensor, value) VALUES ('temp', 21.5);
INSERT INTO readings (sensor, value) VALUES ('temp', '22.1');  -- lossless → ok
SELECT sensor, value, typeof(value) FROM readings;

-- these would ERROR on a STRICT table (uncomment to see):
-- INSERT INTO readings (sensor, value) VALUES ('temp', 'warm');
--   → cannot store TEXT value in REAL column
-- CREATE TABLE bad (x VARCHAR(10)) STRICT;
--   → unknown datatype: VARCHAR



-- the ANY type keeps full dynamic typing inside a STRICT table
DROP TABLE IF EXISTS flexible;
CREATE TABLE flexible (
  k TEXT NOT NULL,
  v ANY
) STRICT;

INSERT INTO flexible VALUES ('n', 1), ('s', 'one'), ('b', X'01'), ('f', 1.0);
SELECT k, v, typeof(v) FROM flexible;
-- note: in a STRICT table ANY stores values EXACTLY as given
-- ('1' would stay TEXT; in a non-strict ANY column it would become INTEGER)



-- checking which tables are strict
SELECT name, strict FROM pragma_table_list WHERE schema = 'main' AND type = 'table';



-- rule of thumb: new projects → STRICT for real columns, ANY where you
-- genuinely want mixed types; legacy schemas (like our store) rely on
-- affinity + CHECK constraints instead
SELECT 'CHECK-constraint alternative: ' ||
       'price REAL NOT NULL CHECK (typeof(price) = ''real'')' AS note;



-- Practice
-- Q1. Recreate the store's products table as STRICT — which column
--     types must change, and why does VARCHAR fail?
-- Q2. Uncomment the failing INSERT above and read the error message.
-- Q3. Into 'flexible', insert the text '123' and verify it stays TEXT.

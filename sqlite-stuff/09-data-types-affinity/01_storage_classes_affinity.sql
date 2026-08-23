-- 01. Storage classes & type affinity — types suggest, values decide
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (this file also creates its own scratch table: affinity_demo)



-- 5 storage classes; every VALUE has one, whatever the column says
SELECT typeof(NULL), typeof(42), typeof(4.2), typeof('42'), typeof(X'42');



-- column types map to one of 5 AFFINITIES by name-matching rules:
-- INT* → INTEGER, CHAR/CLOB/TEXT → TEXT, BLOB/'' → BLOB,
-- REAL/FLOA/DOUB → REAL, everything else → NUMERIC
DROP TABLE IF EXISTS affinity_demo;
CREATE TABLE affinity_demo (
  a INTEGER,
  b TEXT,
  c REAL,
  d BLOB,
  e NUMERIC,
  f VARCHAR(5),        -- TEXT affinity; the (5) is IGNORED, not enforced
  g FLOATING_POINT     -- gotcha: 'INT' inside the name → INTEGER affinity!
);



-- affinity CONVERTS compatible values on insert...
INSERT INTO affinity_demo (a, b, c, e, f) VALUES ('42', 42, '3.14', '7', 'more than five chars');
SELECT a, typeof(a), b, typeof(b), c, typeof(c), e, typeof(e), f, typeof(f)
FROM affinity_demo;
-- '42' became INTEGER 42; 42 became TEXT '42'; f kept 20 chars — no error



-- ...but an INCONVERTIBLE value is stored AS-IS (dynamic typing!)
INSERT INTO affinity_demo (a) VALUES ('not a number');
SELECT a, typeof(a) FROM affinity_demo;      -- TEXT inside an INTEGER column



-- cross-type ORDER BY uses the storage-class order:
-- NULL < INTEGER/REAL < TEXT < BLOB
INSERT INTO affinity_demo (b) VALUES (NULL);
SELECT a FROM affinity_demo ORDER BY a;



-- our store schema relies on affinity: prices arrive as text from a
-- CSV and still land as REAL
SELECT price, typeof(price) FROM products LIMIT 3;



-- Practice
-- Q1. Predict the affinity of columns declared as: BIGINT, STRING,
--     DATETIME, BOOLEAN, POINT (check the name-matching rules).
-- Q2. Insert '00042' into an INTEGER and a TEXT column — what is
--     stored in each? (leading zeros!)
-- Q3. Query affinity_demo for rows where typeof(a) != 'integer' —
--     a data-quality check you can run on any real table.

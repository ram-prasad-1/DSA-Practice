-- 03. Numbers, text & blobs — precision, money, collations
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- INTEGER is a 64-bit signed int; REAL is an IEEE-754 double
SELECT 9223372036854775807 AS max_int, 9223372036854775807 + 1 AS overflows_to_real;



-- classic float trap: 0.1 has no exact binary representation
SELECT 0.1 + 0.2, 0.1 + 0.2 = 0.3;             -- 0.30000000000000004, false!



-- money: never REAL — store integer cents (SQLite has no DECIMAL type)
SELECT CAST(round(price * 100) AS INTEGER) AS price_cents, name
FROM products LIMIT 3;
-- display formatting back: printf with cents
SELECT printf('$%d.%02d', 1299 / 100, 1299 % 100) AS formatted;



-- REAL keeps ~15 significant digits; big integers lose precision as REAL
SELECT CAST(9007199254740993 AS REAL) AS lossy,
       9007199254740993              AS exact;



-- text encodings: length() counts CHARACTERS, octet_length() bytes (3.43+)
SELECT length('héllo'), octet_length('héllo');



-- blobs: hex()/unhex(), randomblob(), zeroblob()
SELECT hex('SQLite'), unhex('53514C697465');
SELECT length(randomblob(16)) AS uuid_bytes, hex(zeroblob(4));



-- collations decide text EQUALITY and ORDER:
-- BINARY (default, case-sensitive), NOCASE (ASCII-insensitive), RTRIM
SELECT 'Cable' = 'cable',
       'Cable' = 'cable' COLLATE NOCASE,
       'pad   ' = 'pad' COLLATE RTRIM;

-- collation per expression...
SELECT name FROM products WHERE name = 'wireless mouse' COLLATE NOCASE;

-- ...or baked into the column/index at CREATE time
DROP TABLE IF EXISTS tags;
CREATE TABLE tags (label TEXT COLLATE NOCASE UNIQUE);
INSERT INTO tags VALUES ('Sale');
INSERT OR IGNORE INTO tags VALUES ('SALE');    -- duplicate under NOCASE, ignored
SELECT count(*) FROM tags;



-- Practice
-- Q1. Show 3 prices from products in cents, then format them back
--     with printf.
-- Q2. Compare sorting products by name with and without COLLATE NOCASE.
-- Q3. Generate a random 16-byte hex token (hint: hex(randomblob(16))).
-- Q4. Why is total(price) REAL even over an INTEGER column? (see §04
--     aggregates — check typeof).

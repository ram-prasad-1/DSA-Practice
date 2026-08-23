-- 01. FTS5 — full-text search over the product catalog
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (needs an FTS5-enabled build — check: PRAGMA compile_options)



-- an FTS5 table is a VIRTUAL table: it tokenizes text into an inverted index
DROP TABLE IF EXISTS product_search;
CREATE VIRTUAL TABLE product_search USING fts5(
  name,
  category,
  tokenize = 'porter'          -- stemming: 'cables' matches 'cable'
);

INSERT INTO product_search (rowid, name, category)
SELECT p.id, p.name, c.name
FROM products p JOIN categories c ON c.id = p.category_id;



-- MATCH is the query operator; bare words are ANDed
SELECT rowid, name FROM product_search WHERE product_search MATCH 'keyboard';
SELECT rowid, name FROM product_search WHERE product_search MATCH 'wireless mouse';



-- the query mini-language: OR, NOT, "phrases", prefix*, NEAR, columns
SELECT name FROM product_search WHERE product_search MATCH 'monitor OR mic';
SELECT name FROM product_search WHERE product_search MATCH 'cable NOT hdmi';
SELECT name FROM product_search WHERE product_search MATCH '"ergonomic keyboard"';
SELECT name FROM product_search WHERE product_search MATCH 'ultra*';
SELECT name FROM product_search WHERE product_search MATCH 'NEAR(noise headphones, 2)';
SELECT name FROM product_search WHERE product_search MATCH 'category: audio';



-- stemming at work (porter): singular finds plural and vice versa
SELECT name FROM product_search WHERE product_search MATCH 'cables';



-- ranking: ORDER BY rank (bm25 relevance; lower = better)
SELECT name, round(rank, 3) AS score
FROM product_search
WHERE product_search MATCH 'wireless OR keyboard'
ORDER BY rank;



-- highlight() and snippet() decorate matches for display
SELECT highlight(product_search, 0, '[', ']') AS hl
FROM product_search WHERE product_search MATCH 'mouse';
SELECT snippet(product_search, 0, '<b>', '</b>', '…', 5) AS snip
FROM product_search WHERE product_search MATCH 'monitor';



-- joining search hits back to the real table via rowid
SELECT p.name, p.price
FROM product_search s
JOIN products p ON p.id = s.rowid
WHERE product_search MATCH 'cable'
ORDER BY s.rank;



-- keeping FTS in sync: mirror writes with triggers (the standard recipe)
DROP TRIGGER IF EXISTS products_fts_insert;
CREATE TRIGGER products_fts_insert AFTER INSERT ON products BEGIN
  INSERT INTO product_search (rowid, name, category)
  VALUES (NEW.id, NEW.name,
          (SELECT name FROM categories WHERE id = NEW.category_id));
END;
-- (production setups add UPDATE/DELETE triggers, or use content= tables)



-- Practice
-- Q1. Search for products matching 'usb' ranked by relevance, with
--     snippets.
-- Q2. All Audio-category matches for 'noise OR mic' (column filter).
-- Q3. Insert a new product and confirm the trigger indexed it.
-- Q4. Rebuild product_search with tokenize='unicode61' — what stops
--     matching that porter caught?

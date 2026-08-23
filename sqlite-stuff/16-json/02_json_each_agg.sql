-- 02. JSON ↔ rows — json_each, json_tree, aggregates, indexing JSON
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- json_each: UNNEST a JSON array into rows (a table-valued function)
SELECT je.value AS color
FROM product_specs ps, json_each(ps.specs, '$.colors') je
WHERE ps.product_id = 4;



-- classic use: filter by membership in a JSON array
SELECT p.name
FROM products p
JOIN product_specs ps ON ps.product_id = p.id
WHERE EXISTS (SELECT 1 FROM json_each(ps.specs, '$.colors')
              WHERE value = 'black');



-- aggregate over unnested values: how popular is each color?
SELECT je.value AS color, count(*) AS products
FROM product_specs ps, json_each(ps.specs, '$.colors') je
GROUP BY color
ORDER BY products DESC;



-- json_tree walks NESTED structure recursively (json_each is one level)
SELECT fullkey, value, type
FROM product_specs ps, json_tree(ps.specs)
WHERE ps.product_id = 3 AND type NOT IN ('object', 'array');



-- the aggregate builders: rows → one JSON value
SELECT json_group_array(name) FROM products WHERE category_id = 5;

SELECT json_group_object(name, price) FROM products WHERE category_id = 2;

-- nested document per category
SELECT c.name AS category,
       json_group_array(json_object('name', p.name, 'price', p.price)) AS items
FROM categories c
JOIN products p ON p.category_id = c.id
GROUP BY c.id;



-- ⭐ indexing JSON: an expression index (or a generated column + index)
-- makes JSON lookups SEARCH instead of SCAN
DROP INDEX IF EXISTS idx_specs_wireless;
CREATE INDEX idx_specs_wireless ON product_specs(specs ->> 'wireless');
EXPLAIN QUERY PLAN
SELECT product_id FROM product_specs WHERE specs ->> 'wireless' = 1;

-- generated-column flavor: visible, typed, indexable
DROP TABLE IF EXISTS specs_gen;
CREATE TABLE specs_gen (
  product_id INTEGER PRIMARY KEY,
  specs      TEXT NOT NULL,
  wireless   INTEGER GENERATED ALWAYS AS (specs ->> 'wireless') VIRTUAL
);
INSERT INTO specs_gen SELECT product_id, specs FROM product_specs;
SELECT product_id, wireless FROM specs_gen;



-- when to use JSON columns vs normalized tables: JSON for ragged,
-- read-mostly attributes; real columns for anything you filter, join,
-- or aggregate on constantly



-- Practice
-- Q1. One row per (product, port) from the monitors' ports arrays.
-- Q2. The full store catalog as ONE JSON document: array of categories,
--     each with its products array (nested json_group_array).
-- Q3. Add an expression index on specs ->> 'inches' and verify the
--     plan for finding 27"+ monitors.
-- Q4. Find every spec key in use with its type (json_tree over all rows,
--     GROUP BY fullkey).

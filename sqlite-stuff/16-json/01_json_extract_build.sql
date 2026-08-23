-- 01. JSON basics — ->, ->>, json_extract, building and modifying JSON
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (this section's schema adds product_specs with JSON documents)



-- the documents
SELECT product_id, specs FROM product_specs;



-- extraction: -> returns JSON (quoted), ->> returns SQL values (3.38+)
SELECT product_id,
       specs -> 'switches'   AS as_json,      -- '"brown"'
       specs ->> 'switches'  AS as_text       -- 'brown'
FROM product_specs WHERE product_id = 1;



-- paths: $.key, nested keys, array indexes
SELECT product_id,
       specs ->> '$.colors[0]'          AS first_color,
       specs ->> '$.tenting.max_deg'    AS max_tilt
FROM product_specs;

-- json_extract is the function form (multiple paths at once)
SELECT json_extract(specs, '$.inches', '$.hdr') FROM product_specs
WHERE product_id = 7;



-- filtering on JSON fields: booleans come back as 1/0
SELECT p.name, ps.specs ->> 'wireless' AS wireless
FROM product_specs ps
JOIN products p ON p.id = ps.product_id
WHERE ps.specs ->> 'wireless' = 1;



-- building JSON from relational rows
SELECT json_object(
         'id', id, 'name', name, 'price', price,
         'tags', json_array('store', 'demo')
       ) AS doc
FROM products LIMIT 3;



-- modifying: json_set (insert or overwrite), json_insert (only if
-- missing), json_replace (only if present), json_remove
SELECT json_set(specs, '$.hdr', json('false'), '$.stand', 'vesa')
FROM product_specs WHERE product_id = 7;
SELECT json_remove(specs, '$.colors[1]') FROM product_specs WHERE product_id = 4;
-- note json('false'): raw 'false' would store the STRING "false"



-- validity & types
SELECT json_valid('{"a": 1}'), json_valid('{oops'),
       json_type('[1,2]'), json_type('{"a":1}', '$.a');



-- JSONB (3.45+): binary storage — smaller, faster to reparse;
-- same functions with jsonb_ prefix, readable via json()
SELECT length(specs) AS text_bytes, length(jsonb(specs)) AS jsonb_bytes
FROM product_specs WHERE product_id = 1;



-- Practice
-- Q1. Every monitor's inches and resolution from its specs.
-- Q2. Products whose specs list more than one color
--     (json_array_length).
-- Q3. Add '"warranty_months": 24' to every document (json_set over a
--     SELECT; then as an UPDATE if you feel brave — re-run 00_schema after).
-- Q4. Build a full JSON API response for product 1: row fields +
--     embedded specs (json_object + json(specs)).

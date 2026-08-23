-- 05. Schema introspection — sqlite_schema and the pragma functions
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- sqlite_schema (a.k.a. sqlite_master): every object + its creating SQL
SELECT type, name FROM sqlite_schema ORDER BY type, name;
SELECT sql FROM sqlite_schema WHERE name = 'products';



-- pragma table-valued functions are queryable (and joinable!)
SELECT name, type, "notnull", dflt_value, pk
FROM pragma_table_info('products');

-- table_xinfo also shows hidden/generated columns
SELECT name, type, hidden FROM pragma_table_xinfo('products');



-- all tables with row-shape info: join two pragmas
SELECT t.name AS table_name, count(*) AS columns
FROM pragma_table_list AS t
JOIN pragma_table_info(t.name) AS c
WHERE t.schema = 'main' AND t.type = 'table' AND t.name NOT LIKE 'sqlite_%'
GROUP BY t.name;



-- indexes and their columns
SELECT name, "unique", origin, partial FROM pragma_index_list('products');
SELECT * FROM pragma_index_info('idx_products_category');



-- foreign keys of a table
SELECT "table", "from", "to", on_delete FROM pragma_foreign_key_list('order_items');



-- find every table referencing customers (schema-wide FK scan)
SELECT t.name AS referencing_table, fk."from" AS via_column
FROM pragma_table_list t
JOIN pragma_foreign_key_list(t.name) fk
WHERE t.schema = 'main' AND fk."table" = 'customers';



-- generate row counts for every table (build SQL from the catalog —
-- run the OUTPUT of this query)
SELECT 'SELECT ''' || name || ''' AS tbl, count(*) FROM "' || name || '" UNION ALL'
FROM sqlite_schema
WHERE type = 'table' AND name NOT LIKE 'sqlite_%';



-- Practice
-- Q1. Which columns anywhere are NOT NULL without a default?
-- Q2. List all views and the tables they mention (LIKE against
--     sqlite_schema.sql).
-- Q3. Find tables that have no PRIMARY KEY (pragma_table_info pk = 0
--     for every column).
-- Q4. Which FK columns have no index on them? (join index pragmas
--     against FK pragmas — the classic performance audit.)

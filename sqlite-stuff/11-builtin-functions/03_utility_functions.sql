-- 03. Utility functions — metadata, session state, misc tools
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- environment introspection
SELECT sqlite_version(), sqlite_source_id();



-- typeof / coalesce / ifnull / nullif / iif: section 03's toolkit, recap
SELECT typeof(1.0), coalesce(NULL, NULL, 3), nullif(5, 5), iif(2 > 1, 'y', 'n');



-- last_insert_rowid(): the rowid of THIS connection's last insert
INSERT INTO categories (name) VALUES ('Docks');
SELECT last_insert_rowid() AS new_category_id;
DELETE FROM categories WHERE name = 'Docks';       -- clean up



-- changes() / total_changes(): rows affected by the last / all statements
UPDATE products SET in_stock = in_stock WHERE category_id = 5;
SELECT changes() AS rows_touched, total_changes() AS since_connect;



-- likelihood hints for the planner (no effect on results)
SELECT count(*) FROM orders WHERE likely(status = 'delivered');
SELECT count(*) FROM orders WHERE unlikely(status = 'cancelled');



-- randomblob + hex: tokens and pseudo-UUIDs
SELECT lower(hex(randomblob(16))) AS token_128bit;
-- a v4-shaped UUID (formatting only — not RFC-perfect)
SELECT lower(
  substr(hex(randomblob(16)), 1, 8) || '-' ||
  substr(hex(randomblob(16)), 1, 4) || '-4' ||
  substr(hex(randomblob(16)), 1, 3) || '-' ||
  substr(hex(randomblob(16)), 1, 4) || '-' ||
  substr(hex(randomblob(16)), 1, 12)) AS uuid_ish;



-- glob()/like() also exist as functions (operator forms are sugar)
SELECT like('Wire%', 'Wireless Mouse'), glob('Wire*', 'Wireless Mouse');



-- table-valued functions: pragma_* lets you QUERY pragma output
SELECT name, type FROM pragma_table_info('products');



-- Practice
-- Q1. Insert a category, capture last_insert_rowid(), delete it by
--     that id, and confirm changes() = 1.
-- Q2. Generate 5 random tokens using a recursive CTE + randomblob.
-- Q3. List every column of every store table via pragma_table_info
--     joined to pragma_table_list.

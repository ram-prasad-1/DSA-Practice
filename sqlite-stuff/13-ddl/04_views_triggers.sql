-- 04. Views & triggers — stored queries, reactive logic
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (creates: v_catalog, v_customer_stats, audit_log + triggers)



-- a view is a named SELECT — always fresh, computed on each read
DROP VIEW IF EXISTS v_catalog;
CREATE VIEW v_catalog AS
SELECT p.id, p.name, c.name AS category, p.price,
       iif(p.in_stock > 0, 'in stock', 'out') AS availability
FROM products p
JOIN categories c ON c.id = p.category_id;

SELECT * FROM v_catalog WHERE availability = 'out';



-- views compose like tables (the schema's order_totals is itself a view)
DROP VIEW IF EXISTS v_customer_stats;
CREATE VIEW v_customer_stats AS
SELECT c.id, c.name, count(o.id) AS orders, coalesce(sum(t.total), 0) AS spend
FROM customers c
LEFT JOIN orders o       ON o.customer_id = c.id
LEFT JOIN order_totals t ON t.order_id = o.id
GROUP BY c.id;

SELECT * FROM v_customer_stats ORDER BY spend DESC LIMIT 3;



-- SQLite views are READ-ONLY; INSTEAD OF triggers make them writable
DROP TRIGGER IF EXISTS v_catalog_price_update;
CREATE TRIGGER v_catalog_price_update
INSTEAD OF UPDATE OF price ON v_catalog
BEGIN
  UPDATE products SET price = NEW.price WHERE id = OLD.id;
END;

UPDATE v_catalog SET price = 10.99 WHERE id = 11;
SELECT id, name, price FROM products WHERE id = 11;    -- really changed



-- audit trigger: AFTER UPDATE, recording OLD and NEW
DROP TABLE IF EXISTS audit_log;
CREATE TABLE audit_log (
  at        TEXT NOT NULL DEFAULT (datetime('now')),
  table_    TEXT NOT NULL,
  row_id    INTEGER NOT NULL,
  change    TEXT NOT NULL
);

DROP TRIGGER IF EXISTS products_price_audit;
CREATE TRIGGER products_price_audit
AFTER UPDATE OF price ON products
WHEN OLD.price != NEW.price                      -- fire only on real change
BEGIN
  INSERT INTO audit_log (table_, row_id, change)
  VALUES ('products', OLD.id, OLD.price || ' -> ' || NEW.price);
END;

UPDATE products SET price = 11.49 WHERE id = 11;
SELECT * FROM audit_log;



-- validation trigger: BEFORE + RAISE aborts the statement
DROP TRIGGER IF EXISTS products_no_free;
CREATE TRIGGER products_no_free
BEFORE UPDATE OF price ON products
WHEN NEW.price <= 0
BEGIN
  SELECT RAISE(ABORT, 'price must be positive');
END;
-- UPDATE products SET price = 0 WHERE id = 11;   -- uncomment → aborts



-- list what exists
SELECT type, name FROM sqlite_schema WHERE type IN ('view', 'trigger') ORDER BY type;



-- Practice
-- Q1. A view of monthly revenue (month, orders, revenue) on order_totals.
-- Q2. An AFTER INSERT trigger on orders writing to audit_log.
-- Q3. A BEFORE INSERT trigger rejecting order_items with quantity > 100.
-- Q4. INSTEAD OF DELETE on v_catalog that sets in_stock = 0 instead of
--     deleting the product.

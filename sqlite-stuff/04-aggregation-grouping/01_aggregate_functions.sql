-- 01. Aggregate functions — COUNT, SUM, TOTAL, AVG, MIN, MAX
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- an aggregate collapses many rows into one value
SELECT count(*), sum(in_stock), avg(price), min(price), max(price) FROM products;



-- count(*) counts rows; count(col) counts NON-NULL values in col
SELECT count(*) AS customers, count(city) AS with_city FROM customers;



-- count(DISTINCT col) counts unique non-NULL values
SELECT count(country) AS rows_, count(DISTINCT country) AS countries FROM customers;



-- sum() returns NULL when no rows match; total() returns 0.0 (and always REAL)
SELECT sum(in_stock), total(in_stock) FROM products WHERE price > 9999;



-- aggregates ignore NULLs entirely (recap from section 03)
SELECT avg(price) FROM products;
SELECT min(city), max(city) FROM customers;   -- NULL cities skipped



-- aggregates over expressions
SELECT sum(quantity * unit_price) AS lifetime_revenue FROM order_items;
SELECT round(avg(price), 2) AS avg_price, max(price) - min(price) AS price_spread
FROM products;



-- WHERE filters rows BEFORE they are aggregated
SELECT count(*) AS delivered_orders FROM orders WHERE status = 'delivered';
SELECT sum(quantity) AS cable_units
FROM order_items
WHERE product_id IN (11, 12, 13);



-- FILTER (WHERE ...) (3.30+): per-aggregate conditions in one pass
SELECT count(*)                                        AS all_orders,
       count(*) FILTER (WHERE status = 'delivered')    AS delivered,
       count(*) FILTER (WHERE status = 'cancelled')    AS cancelled
FROM orders;



-- Practice
-- Q1. Total units in stock across all products, and how many distinct
--     categories actually have a product.
-- Q2. Average order value using the order_totals view.
-- Q3. In one row: count of orders placed before and after 2024-06-01
--     (FILTER twice).
-- Q4. Why does count(city) differ from count(*) on customers?

-- 02. GROUP BY — one value per group, multiple keys, group_concat
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- GROUP BY splits rows into groups; aggregates run once per group
SELECT country, count(*) AS customers FROM customers GROUP BY country;
SELECT category_id, count(*) AS products, round(avg(price), 2) AS avg_price
FROM products
GROUP BY category_id;



-- frequency table / histogram: the bread-and-butter GROUP BY
SELECT status, count(*) AS orders FROM orders GROUP BY status;



-- multiple grouping keys: one group per distinct combination
SELECT customer_id, status, count(*) AS orders
FROM orders
GROUP BY customer_id, status;



-- grouping by an expression (orders per month)
SELECT strftime('%Y-%m', placed_at) AS month, count(*) AS orders
FROM orders
GROUP BY strftime('%Y-%m', placed_at);



-- gotcha: SQLite allows selecting BARE columns not in GROUP BY —
-- the value comes from an ARBITRARY row of the group (most DBs error)
SELECT country, name, count(*) FROM customers GROUP BY country;

-- exception: with a lone min()/max(), bare columns come from the winning row
SELECT country, name, max(signed_up) AS newest_signup
FROM customers
GROUP BY country;



-- group_concat(col, sep): collapse a group into one string
SELECT country, group_concat(name, ', ') AS customer_names
FROM customers
GROUP BY country;

-- DISTINCT inside; string_agg() is a standard-named alias (3.44+)
SELECT group_concat(DISTINCT status) AS statuses_seen FROM orders;
SELECT country, string_agg(name, '; ') FROM customers GROUP BY country;

-- ORDER BY inside an aggregate controls element order (3.44+)
SELECT country, group_concat(name ORDER BY signed_up DESC) AS newest_first
FROM customers
GROUP BY country;



-- Practice
-- Q1. Units sold per product_id from order_items (sum of quantity),
--     highest first.
-- Q2. Orders per customer per month.
-- Q3. Per country: the newest customer's name and signup date
--     (use the min/max bare-column exception).
-- Q4. One comma-separated list of product names per category,
--     alphabetical inside each list.

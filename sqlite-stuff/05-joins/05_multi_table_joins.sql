-- 05. Multi-table joins — chaining 3-4 tables, mixing join types
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- order detail lines: 4 tables chained on their foreign keys
SELECT o.id AS order_id, c.name AS customer, p.name AS product,
       oi.quantity, oi.unit_price, oi.quantity * oi.unit_price AS line_total
FROM order_items oi
JOIN orders o    ON o.id = oi.order_id
JOIN customers c ON c.id = o.customer_id
JOIN products p  ON p.id = oi.product_id
ORDER BY o.id;



-- revenue per category name (order_items → products → categories)
SELECT cat.name AS category, round(sum(oi.quantity * oi.unit_price), 2) AS revenue
FROM order_items oi
JOIN products p    ON p.id = oi.product_id
JOIN categories cat ON cat.id = p.category_id
GROUP BY cat.id
ORDER BY revenue DESC;



-- mixing join types: start LEFT to keep empty categories, and keep the
-- chain LEFT — an INNER join later would silently drop the NULL rows again
SELECT cat.name AS category, coalesce(sum(oi.quantity), 0) AS units_sold
FROM categories cat
LEFT JOIN products p     ON p.category_id = cat.id
LEFT JOIN order_items oi ON oi.product_id = p.id
GROUP BY cat.id
ORDER BY units_sold DESC;          -- Webcams and Bluetooth Speaker count as 0



-- who bought what: distinct product list per customer (join + group_concat)
SELECT c.name, group_concat(DISTINCT p.name) AS products_bought
FROM customers c
JOIN orders o     ON o.customer_id = c.id
JOIN order_items oi ON oi.order_id = o.id
JOIN products p   ON p.id = oi.product_id
GROUP BY c.id;



-- top spender per country: join, aggregate, then pick with min/max
SELECT country, name, max(spend) AS top_spend
FROM (
  SELECT c.country, c.name, sum(oi.quantity * oi.unit_price) AS spend
  FROM customers c
  JOIN orders o     ON o.customer_id = c.id
  JOIN order_items oi ON oi.order_id = o.id
  GROUP BY c.id
)
GROUP BY country;



-- Practice
-- Q1. Per customer: name, country, number of distinct products bought
--     — including customers who bought nothing (mind the join types).
-- Q2. Revenue per country per category.
-- Q3. For each category, the single best-selling product by units
--     (subquery + max, like the top-spender example).
-- Q4. Orders containing any 'Cables' item, with customer names.

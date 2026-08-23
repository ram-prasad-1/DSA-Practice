-- 02. LEFT JOIN — keep every left row, NULLs where the right side is missing
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- LEFT JOIN keeps ALL customers; order columns are NULL for
-- customers with no orders (Barbara has none)
SELECT c.name, o.id AS order_id, o.placed_at
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id;



-- anti-join pattern: rows with NO match = right side IS NULL
SELECT c.name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;                        -- customers who never ordered

SELECT p.name
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.id
WHERE oi.product_id IS NULL;               -- products never ordered



-- counting gotcha: count(*) counts the customer's NULL row as 1;
-- count(o.id) correctly gives 0 for order-less customers
SELECT c.name, count(*) AS wrong, count(o.id) AS orders
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.id;



-- THE LEFT JOIN gotcha: filtering the RIGHT table in WHERE
-- silently turns the join back into an INNER join
SELECT c.name, o.id AS order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.status = 'delivered';              -- drops customers w/o delivered orders

-- the condition belongs in ON to keep every customer
SELECT c.name, o.id AS order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id AND o.status = 'delivered';



-- LEFT JOIN + aggregate: orders per customer including the zeroes
SELECT c.name, count(o.id) AS orders, coalesce(sum(t.total), 0) AS spend
FROM customers c
LEFT JOIN orders o       ON o.customer_id = c.id
LEFT JOIN order_totals t ON t.order_id = o.id
GROUP BY c.id
ORDER BY spend DESC;



-- Practice
-- Q1. Every category with its product count — including Webcams with 0
--     (count the right column, not *).
-- Q2. Products with total units sold, never-ordered ones showing 0.
-- Q3. Customers with their count of DELIVERED orders — everyone listed,
--     zeroes included (condition in ON!).
-- Q4. Rewrite Q3 with the status filter in WHERE and compare row counts.

-- 02. INTERSECT and EXCEPT — overlap and difference
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- INTERSECT: rows present in BOTH sets (deduplicated)
SELECT email FROM customers
INTERSECT
SELECT email FROM newsletter_subscribers;      -- customers on the newsletter



-- EXCEPT: rows in the first set but NOT the second (order matters!)
SELECT email FROM customers
EXCEPT
SELECT email FROM newsletter_subscribers;      -- customers not subscribed

SELECT email FROM newsletter_subscribers
EXCEPT
SELECT email FROM customers;                   -- subscribers who never bought



-- set ops compare the WHOLE row — multi-column works too
SELECT customer_id, status FROM orders WHERE placed_at < '2024-06-01'
INTERSECT
SELECT customer_id, status FROM orders WHERE placed_at >= '2024-06-01';
-- (customer, status) combos occurring in both halves of the year



-- the same answers via joins — know both shapes:
-- INTERSECT ~ inner join / IN; EXCEPT ~ anti-join / NOT IN
SELECT DISTINCT c.email
FROM customers c
JOIN newsletter_subscribers n ON n.email = c.email;

SELECT c.email
FROM customers c
LEFT JOIN newsletter_subscribers n ON n.email = c.email
WHERE n.email IS NULL;
-- unlike NOT IN, EXCEPT and the anti-join are both NULL-safe



-- chaining set ops: evaluated left to right
SELECT email FROM customers
UNION
SELECT email FROM newsletter_subscribers
EXCEPT
SELECT email FROM customers WHERE country = 'USA';



-- Practice
-- Q1. Product ids ordered in 2024-03 AND again in 2024-04 (INTERSECT
--     two order_items/orders queries).
-- Q2. Countries with customers but no delivered orders (EXCEPT).
-- Q3. Rewrite Q2 with NOT EXISTS and compare.
-- Q4. Predict the result of A EXCEPT B UNION C given ties — is it
--     (A EXCEPT B) UNION C or A EXCEPT (B UNION C)? Verify.

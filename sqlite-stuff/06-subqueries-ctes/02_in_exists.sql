-- 02. IN and EXISTS subqueries — membership and existence tests
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- IN (subquery): membership in a computed set
SELECT name FROM customers
WHERE id IN (SELECT customer_id FROM orders WHERE status = 'pending');



-- EXISTS: true as soon as the subquery finds ONE row —
-- correlated on the outer row, often reads more naturally
SELECT c.name FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o
              WHERE o.customer_id = c.id AND o.status = 'pending');



-- NOT EXISTS: the safe "has none" test
SELECT c.name FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);



-- recap gotcha: NOT IN over a set containing NULL returns nothing —
-- referred_by has NULLs, so prefer NOT EXISTS
SELECT name FROM customers
WHERE id NOT IN (SELECT referred_by FROM customers);          -- 0 rows!

SELECT c.name FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM customers r WHERE r.referred_by = c.id);
-- customers who never referred anyone — NULLs are a non-issue



-- semi-join vs join: EXISTS/IN return each outer row AT MOST ONCE;
-- a JOIN duplicates the customer per matching order
SELECT c.name FROM customers c
JOIN orders o ON o.customer_id = c.id AND o.status = 'delivered';   -- dupes

SELECT c.name FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o
              WHERE o.customer_id = c.id AND o.status = 'delivered');



-- Practice
-- Q1. Products that appear in at least one 2024-03 order (IN, then EXISTS).
-- Q2. Categories with no products in stock (NOT EXISTS over products).
-- Q3. Customers who ordered something from the 'Cables' category.
-- Q4. Why is SELECT DISTINCT + JOIN usually worse than EXISTS for Q3?

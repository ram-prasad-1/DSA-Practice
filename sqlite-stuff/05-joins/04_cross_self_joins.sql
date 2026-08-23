-- 04. CROSS JOIN & self-joins — cartesian products, joining a table to itself
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- CROSS JOIN: every row paired with every row (no ON clause).
-- useful deliberately — e.g. scaffold every category × sales channel
SELECT cat.name AS category, ch.column1 AS channel
FROM categories cat
CROSS JOIN (VALUES ('online'), ('retail')) ch;



-- accidental cartesian products are the danger: a comma join with a
-- forgotten condition multiplies row counts (8 customers × 12 orders = 96)
SELECT count(*) FROM customers, orders;
-- (in SQLite, CROSS JOIN also pins the join order as a planner hint)



-- self-join: the table appears twice under different aliases.
-- referred_by points at another customer — who referred whom?
SELECT c.name AS customer, r.name AS referred_by
FROM customers c
JOIN customers r ON r.id = c.referred_by;

-- LEFT version keeps the non-referred customers too
SELECT c.name AS customer, coalesce(r.name, '—') AS referred_by
FROM customers c
LEFT JOIN customers r ON r.id = c.referred_by;



-- self-join for pairs: customers from the same country,
-- a.id < b.id avoids self-pairs and mirrored duplicates
SELECT a.name, b.name, a.country
FROM customers a
JOIN customers b ON b.country = a.country AND a.id < b.id;



-- USING (col): shorthand when BOTH sides name the column identically —
-- natural fit for self-joins; the shared column appears once, unqualified
SELECT a.name, b.name, country
FROM customers a
JOIN customers b USING (country)
WHERE a.id < b.id;
-- our FK pairs are named differently (orders.customer_id vs customers.id),
-- so between tables this schema always needs ON



-- Practice
-- Q1. Scaffold every product × the sizes ('S','M','L') via CROSS JOIN.
-- Q2. Referral chains of length 2: customer → referrer → referrer's
--     referrer (three aliases).
-- Q3. Pairs of products in the same category within 30.00 of each
--     other's price.
-- Q4. Which customers were referred by someone from another country?

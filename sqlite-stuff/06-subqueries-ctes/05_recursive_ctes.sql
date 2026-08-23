-- 05. Recursive CTEs — WITH RECURSIVE: sequences, dates, hierarchies
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- anatomy: seed row UNION ALL recursive step reading the CTE itself,
-- until the step produces no rows
WITH RECURSIVE n(x) AS (
  SELECT 1
  UNION ALL
  SELECT x + 1 FROM n WHERE x < 10
)
SELECT x FROM n;



-- date series: one row per day (great for filling report gaps)
WITH RECURSIVE days(d) AS (
  SELECT '2024-03-01'
  UNION ALL
  SELECT date(d, '+1 day') FROM days WHERE d < '2024-03-10'
)
SELECT d FROM days;

-- every month with its order count, INCLUDING zero months
WITH RECURSIVE months(m) AS (
  SELECT '2024-01'
  UNION ALL
  SELECT strftime('%Y-%m', m || '-01', '+1 month') FROM months WHERE m < '2024-09'
)
SELECT m, count(o.id) AS orders
FROM months
LEFT JOIN orders o ON strftime('%Y-%m', o.placed_at) = m
GROUP BY m;



-- hierarchy walk: referral chains (referred_by points at the referrer).
-- start from the roots and carry the depth and path along
WITH RECURSIVE tree(id, name, depth, path) AS (
  SELECT id, name, 0, name
  FROM customers
  WHERE referred_by IS NULL
  UNION ALL
  SELECT c.id, c.name, t.depth + 1, t.path || ' -> ' || c.name
  FROM customers c
  JOIN tree t ON c.referred_by = t.id
)
SELECT depth, path FROM tree ORDER BY path;



-- UNION instead of UNION ALL dedupes visited rows — the standard
-- guard for graphs that may contain cycles; LIMIT is the emergency brake
WITH RECURSIVE r(x) AS (
  SELECT 0
  UNION
  SELECT (x + 1) % 5 FROM r          -- would loop forever with UNION ALL
)
SELECT x FROM r LIMIT 20;



-- Practice
-- Q1. Powers of 2 up to 1024.
-- Q2. All descendants of Grace Hopper in the referral tree (start the
--     seed from her id instead of the roots).
-- Q3. A week-by-week (Monday-dated) order count for 2024 Q1 with zero
--     weeks included.
-- Q4. Fibonacci numbers below 100 (carry two columns).

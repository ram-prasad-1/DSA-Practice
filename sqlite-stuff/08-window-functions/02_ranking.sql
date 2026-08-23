-- 02. Ranking — ROW_NUMBER, RANK, DENSE_RANK, NTILE, top-N per group
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- row_number(): unique 1,2,3... in window order (ties broken arbitrarily)
-- rank(): ties share a rank, next rank SKIPS (1,1,3)
-- dense_rank(): ties share a rank, no gaps (1,1,2)
SELECT name, price,
       row_number() OVER (ORDER BY price DESC) AS row_num,
       rank()       OVER (ORDER BY price DESC) AS rank,
       dense_rank() OVER (ORDER BY price DESC) AS dense
FROM products;



-- ranking within partitions: cheapest first per category
SELECT category_id, name, price,
       row_number() OVER (PARTITION BY category_id ORDER BY price) AS pos
FROM products;



-- top-N per group: rank in a CTE, filter outside (windows can't go in WHERE)
WITH ranked AS (
  SELECT category_id, name, price,
         row_number() OVER (PARTITION BY category_id ORDER BY price DESC) AS pos
  FROM products
)
SELECT category_id, name, price
FROM ranked
WHERE pos <= 2;                      -- 2 most expensive per category



-- ntile(n): split ordered rows into n buckets (quartiles, quintiles...)
SELECT name, price,
       ntile(4) OVER (ORDER BY price) AS price_quartile
FROM products;



-- percent_rank() and cume_dist(): relative standing in [0, 1]
SELECT name, price,
       round(percent_rank() OVER (ORDER BY price), 2) AS pct_rank,
       round(cume_dist()    OVER (ORDER BY price), 2) AS cume
FROM products;



-- a named WINDOW avoids repeating the same spec
SELECT name, price,
       rank()       OVER w AS rnk,
       dense_rank() OVER w AS drnk
FROM products
WINDOW w AS (ORDER BY price DESC);



-- Practice
-- Q1. Each customer's orders numbered 1..n oldest-first.
-- Q2. The single most recent order per customer (top-1 per group).
-- Q3. Rank customers by total spend; show where rank and dense_rank
--     would differ if two customers tie.
-- Q4. Split all orders into spending terciles (ntile(3) on total).

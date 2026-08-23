-- 02. Math functions — round, abs, and the 3.35+ math extension
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- always available: abs, round, sign, min/max (scalar), random
SELECT abs(-7), round(3.567), round(3.567, 2), sign(-3), sign(0), sign(9);



-- random(): a random 64-bit integer; scale it yourself
SELECT random(),
       abs(random()) % 100        AS d100,
       abs(random()) % 6 + 1      AS die_roll;



-- built-in math functions (3.35+): ceil/floor, power, roots, logs, trig
SELECT ceil(4.2), floor(4.8), trunc(4.9), pow(2, 10), sqrt(144), mod(17, 5);

SELECT ln(exp(1)), log10(1000), log2(1024), log(8, 64);    -- log(base, x)

SELECT pi(), sin(pi() / 2), degrees(pi()), radians(180);



-- rounding money correctly: round() half-away-from-zero at 2 decimals
SELECT price, round(price * 1.18, 2) AS with_tax FROM products LIMIT 4;



-- integer math recap: promote before dividing
SELECT sum(in_stock) / count(*)        AS truncated_avg,
       sum(in_stock) * 1.0 / count(*)  AS real_avg,
       avg(in_stock)                   AS builtin_avg
FROM products;



-- practical stats without extensions: stddev via two passes
WITH stats AS (SELECT avg(price) AS mu FROM products)
SELECT round(sqrt(avg((price - mu) * (price - mu))), 2) AS stddev_pop
FROM products, stats;



-- bucketing values: floor(x / width) * width makes histogram bins
SELECT (CAST(price / 100 AS INTEGER)) * 100 AS price_bin, count(*) AS products
FROM products
GROUP BY price_bin
ORDER BY price_bin;



-- Practice
-- Q1. Simulate 5 coin flips in one row (random + %).
-- Q2. Price bins of width 50 with counts.
-- Q3. Geometric mean of product prices (exp of avg of ln).
-- Q4. Round 2.5 and 3.5 with round() — which way do halves go?

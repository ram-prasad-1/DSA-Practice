-- 02. R-Tree & generate_series — the other bundled extensions
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- generate_series(start, stop, step): a table-valued sequence —
-- often simpler than a recursive CTE
SELECT value FROM generate_series(1, 10);
SELECT value FROM generate_series(0, 100, 25);

-- a date series without recursion
SELECT date('2024-03-01', '+' || value || ' days') AS d
FROM generate_series(0, 9);

-- months with zero orders, series-style (recap of section 10)
SELECT strftime('%Y-%m', '2024-01-01', '+' || value || ' months') AS month,
       count(o.id) AS orders
FROM generate_series(0, 8) s
LEFT JOIN orders o ON strftime('%Y-%m', o.placed_at) =
                      strftime('%Y-%m', '2024-01-01', '+' || value || ' months')
GROUP BY month;



-- R-Tree: an index for RANGES/RECTANGLES — spatial queries, intervals.
-- columns are (id, min1, max1[, min2, max2...]) up to 5 dimensions
DROP TABLE IF EXISTS store_zones;
CREATE VIRTUAL TABLE store_zones USING rtree(
  id, min_x, max_x, min_y, max_y
);

INSERT INTO store_zones VALUES
  (1, 0,  10, 0,  10),     -- warehouse A footprint
  (2, 8,  20, 5,  15),     -- warehouse B (overlaps A)
  (3, 30, 40, 30, 40);     -- warehouse C (far away)



-- containment: which zones contain point (9, 7)?
SELECT id FROM store_zones
WHERE min_x <= 9 AND max_x >= 9 AND min_y <= 7 AND max_y >= 7;

-- overlap: which zones intersect the rectangle (5..12, 0..8)?
SELECT id FROM store_zones
WHERE min_x <= 12 AND max_x >= 5 AND min_y <= 8 AND max_y >= 0;
-- the rtree answers these from its tree structure — on millions of
-- boxes this is the difference between instant and full-scan



-- 1-D rtree = fast interval lookups (e.g. price bands, time windows)
DROP TABLE IF EXISTS price_bands;
CREATE VIRTUAL TABLE price_bands USING rtree(id, lo, hi);
INSERT INTO price_bands VALUES (1, 0, 50), (2, 50, 200), (3, 200, 1000);
SELECT pb.id AS band, p.name, p.price
FROM products p
JOIN price_bands pb ON p.price >= pb.lo AND p.price < pb.hi
ORDER BY pb.id, p.price;



-- other loadable extensions exist beyond the bundled ones
-- (.load in the CLI): sqlite-vec (vectors), spatialite (GIS), etc.
SELECT count(*) AS compile_options FROM pragma_compile_options;



-- Practice
-- Q1. Multiplication table 1-10 via two generate_series cross-joined.
-- Q2. A zone that contains ALL current zones (bounding box: min of
--     mins, max of maxes).
-- Q3. Rebuild price_bands so no product falls into two bands even at
--     exact boundaries. Where did the half-open logic go?
-- Q4. Every 3rd day in 2024-06 using generate_series step.

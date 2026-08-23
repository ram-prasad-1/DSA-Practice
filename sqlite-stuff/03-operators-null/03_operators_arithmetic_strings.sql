-- 03. Operators — arithmetic, string concat, bitwise, precedence
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- arithmetic: + - * / %
SELECT name, price, price * 1.18 AS with_tax, price - 5 AS coupon FROM products;



-- gotcha: integer / integer TRUNCATES; promote one side to float
SELECT 5 / 2, 5.0 / 2, 5 / 2.0, CAST(5 AS REAL) / 2;
SELECT name, in_stock, in_stock / 12 AS full_boxes, in_stock % 12 AS loose_units
FROM products;



-- % is modulo (remainder); works for even/odd, cycling, bucketing
SELECT id, id % 2 AS is_odd FROM customers;



-- || is string concatenation; numbers are coerced to text
SELECT name || ' — $' || price AS label FROM products;

-- concat()/concat_ws() (3.44+): concat skips NULLs, unlike ||
SELECT concat('city: ', city) AS c1, 'city: ' || city AS c2 FROM customers;
SELECT concat_ws(', ', name, city, country) AS address_line FROM customers;



-- bitwise: & | ~ << >> operate on 64-bit integers
SELECT 5 & 3, 5 | 3, ~5, 1 << 4, 16 >> 2;

-- flags pattern: pack booleans into one integer (1=new, 2=featured, 4=clearance)
SELECT name,
       (id % 4)                    AS flags,          -- fake flags for the demo
       (id % 4) & 1                AS is_new,
       ((id % 4) & 2) != 0         AS is_featured
FROM products;



-- precedence: * / % bind tighter than + -, comparisons bind tighter than
-- AND, AND tighter than OR — when in doubt, parenthesize
SELECT 2 + 3 * 4, (2 + 3) * 4;
SELECT 1 OR 0 AND 0;       -- AND first → 1



-- Practice
-- Q1. Price per unit in stock (price / in_stock) as REAL, avoiding
--     division by zero (hint: nullif(in_stock, 0)).
-- Q2. Each order item's line total (quantity * unit_price) from order_items.
-- Q3. 'Ada Lovelace <ada@example.com>' style labels via concat_ws or ||.
-- Q4. Which product ids have bit 2 set in (id % 8)?

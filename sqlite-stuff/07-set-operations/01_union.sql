-- 01. UNION and UNION ALL — stacking result sets
-- Setup once: sqlite3 play.db ".read 00_schema.sql"
-- (this section's schema adds newsletter_subscribers, overlapping customers)



-- UNION ALL stacks rows as-is; UNION also deduplicates (costs a sort)
SELECT email FROM customers
UNION ALL
SELECT email FROM newsletter_subscribers;      -- overlaps appear twice

SELECT email FROM customers
UNION
SELECT email FROM newsletter_subscribers;      -- each email once



-- compatibility rules: same COLUMN COUNT per SELECT; names come from
-- the first SELECT; types may mix (SQLite is lenient — most DBs aren't)
SELECT name, country       AS place FROM customers
UNION ALL
SELECT name, 'category #' || id FROM categories;



-- tagging the source is a common reporting trick
SELECT 'customer' AS source, email FROM customers
UNION ALL
SELECT 'newsletter', email FROM newsletter_subscribers
ORDER BY email;



-- ORDER BY / LIMIT apply to the WHOLE compound, and only at the end
SELECT email FROM customers WHERE country = 'UK'
UNION
SELECT email FROM newsletter_subscribers
ORDER BY email
LIMIT 5;



-- UNION ALL for subtotal rows (recap from section 04)
SELECT country AS label, count(*) AS n FROM customers GROUP BY country
UNION ALL
SELECT 'TOTAL', count(*) FROM customers;



-- Practice
-- Q1. One deduplicated list of all names: customers + product names.
-- Q2. Emails on either list, each tagged 'both', 'customer only', or
--     'newsletter only' (UNION ALL + GROUP BY the email, count sources).
-- Q3. Why does putting ORDER BY inside the first SELECT of a UNION
--     fail? Where must it go?

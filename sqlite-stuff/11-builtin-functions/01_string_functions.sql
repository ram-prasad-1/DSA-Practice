-- 01. String functions — length, substr, instr, replace, trim, printf
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- the basics
SELECT name,
       length(name)        AS chars,
       upper(name)         AS shouty,
       lower(name)         AS quiet
FROM customers LIMIT 3;



-- substr(s, start, len): 1-based; negative start counts from the end
SELECT substr('SQLite', 1, 3), substr('SQLite', 4), substr('SQLite', -3);



-- instr(haystack, needle): 1-based position, 0 if absent —
-- combine with substr to split strings
SELECT email,
       instr(email, '@')                          AS at_pos,
       substr(email, 1, instr(email, '@') - 1)    AS local_part,
       substr(email, instr(email, '@') + 1)       AS domain
FROM customers LIMIT 4;



-- replace(s, from, to): every occurrence
SELECT name, replace(name, ' ', '_') AS slug FROM products LIMIT 4;



-- trim/ltrim/rtrim: strip spaces, or any character set you pass
SELECT trim('  padded  '),
       trim('--flag--', '-'),
       ltrim('0042', '0');



-- printf/format: typed placeholders (%d int, %f float, %s text, %02d pad)
SELECT printf('%s: $%.2f (%d left)', name, price, in_stock) AS label
FROM products LIMIT 4;
SELECT format('%,d', 1234567) AS with_thousands;    -- format() = printf alias



-- padding trick: printf %-10s / %10s for alignment
SELECT printf('%-30s|%8.2f', name, price) AS fixed_width FROM products LIMIT 4;



-- quote(): SQL-quotes a value — handy for generating SQL or debugging
SELECT quote('it''s'), quote(42), quote(NULL), quote(X'AB');



-- char()/unicode(): codepoints to text and back
SELECT char(83, 81, 76), unicode('S');



-- Practice
-- Q1. Everyone's initials (first letter of each name part; two-part
--     names — substr + instr on the space).
-- Q2. Mask emails like a***@example.com.
-- Q3. Product names as URL slugs: lowercase, spaces → '-'.
-- Q4. A right-aligned price column: '$    9.99' width 10 via printf.

-- 01. Date & time functions — date, time, datetime, julianday, unixepoch, strftime
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- SQLite has NO date type — dates are TEXT (ISO-8601), REAL (Julian day),
-- or INTEGER (Unix epoch). The store schema uses ISO-8601 TEXT.
SELECT placed_at, typeof(placed_at) FROM orders LIMIT 2;



-- the function family: each returns one representation
SELECT date('now'), time('now'), datetime('now'),
       julianday('now'), unixepoch('now');



-- parsing: all functions accept ISO text, Julian numbers, or epoch
-- (epoch needs the 'unixepoch' modifier to disambiguate from Julian)
SELECT datetime('2024-03-01'),
       datetime(2460370.5),
       datetime(1709251200, 'unixepoch');



-- strftime: format any date with % placeholders
SELECT strftime('%Y-%m-%d', 'now')      AS iso_date,
       strftime('%d/%m/%Y', 'now')      AS eu_date,
       strftime('%H:%M', 'now')         AS hhmm,
       strftime('%w', 'now')            AS weekday_0_sun,
       strftime('%j', 'now')            AS day_of_year,
       strftime('%s', 'now')            AS epoch_secs;



-- date arithmetic via julianday/unixepoch differences
SELECT id, placed_at,
       CAST(julianday('2024-12-31') - julianday(placed_at) AS INTEGER)
         AS days_until_year_end
FROM orders LIMIT 3;

-- timediff() (3.43+): human-readable difference
SELECT timediff('2024-09-02', '2024-03-01');



-- converting between conventions
SELECT unixepoch('2024-06-01')                 AS text_to_epoch,
       date(1717200000, 'unixepoch')           AS epoch_to_text,
       julianday('2024-06-01')                 AS text_to_julian;



-- Practice
-- Q1. Each order's age in days as of 2024-12-31.
-- Q2. Show every customer's signup date as 'Mon 15 Jan 2024' style
--     (strftime has no month names — build with CASE on %m).
-- Q3. Convert all order dates to unix epochs and back, verifying
--     round-trip equality.

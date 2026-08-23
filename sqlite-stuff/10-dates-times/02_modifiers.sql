-- 02. Date modifiers — '+1 day', 'start of month', 'weekday', timezones
-- Setup once: sqlite3 play.db ".read 00_schema.sql"



-- modifiers chain left to right after the time value
SELECT date('2024-03-15', '+1 day'),
       date('2024-03-15', '-3 months'),
       date('2024-03-15', '+1 year', '+10 days');



-- snapping: start of month / year / day (there is no 'end of' —
-- go to next start, minus a day)
SELECT date('2024-03-15', 'start of month'),
       date('2024-03-15', 'start of year'),
       date('2024-03-15', 'start of month', '+1 month', '-1 day') AS month_end;



-- 'weekday N' advances to the NEXT weekday N (0 = Sunday), staying put
-- if already there — e.g. the Monday of an order's week:
SELECT placed_at,
       date(placed_at, 'weekday 1', '-7 days') AS wrong_if_monday,
       date(placed_at, '-6 days', 'weekday 1') AS week_monday
FROM orders LIMIT 5;



-- fractional and second-level arithmetic
SELECT datetime('2024-03-15 10:30:00', '+90 minutes'),
       datetime('2024-03-15 10:30:00', '+1.5 hours'),
       datetime('2024-03-15 10:30:00', '+45 seconds');



-- timezones: 'now' is UTC; 'localtime' converts to the machine's zone,
-- 'utc' converts back. Store UTC, convert only at the edges.
SELECT datetime('now')              AS utc_now,
       datetime('now', 'localtime') AS local_now,
       datetime('2024-03-15 09:00:00', 'localtime') AS stored_utc_shown_local;



-- deadline-style logic on the store data: orders older than 60 days
-- at a given reference date
SELECT id, placed_at
FROM orders
WHERE placed_at < date('2024-08-01', '-60 days');



-- Practice
-- Q1. The last day of each order's month.
-- Q2. Each customer's signup anniversary in 2025.
-- Q3. Orders placed in the FIRST 7 days of their month.
-- Q4. What does date('2024-03-31', '+1 month') return? Why? (month
--     arithmetic overflows into the next month — verify).

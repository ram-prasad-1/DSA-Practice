-- 01. sqlite3 CLI dot-commands — ⚠ CLI ONLY: these are shell features,
-- not SQL. PyCharm/JDBC cannot run them; open a terminal:
--   sqlite3 play.db
-- Setup once (in that shell): .read 00_schema.sql



-- ── looking around ─────────────────────────────────────────
-- .tables                     list tables (and views)
-- .tables 'prod%'             filtered by LIKE pattern
-- .schema products            the CREATE statement(s) for one object
-- .schema                     the whole schema
-- .indexes products           indexes on a table
-- .dbinfo                     page size, counts, encoding, versions
-- .databases                  attached database files



-- ── output formatting ──────────────────────────────────────
-- .mode box                   pretty unicode tables (try: list, column,
--                             csv, json, markdown, insert, quote)
-- .headers on                 column names in output
-- .nullvalue ∅                make NULLs visible
-- .width 20 10                fixed column widths (column mode)
-- try it:
SELECT id, name, city FROM customers LIMIT 4;



-- ── getting data OUT ───────────────────────────────────────
-- .once report.csv            next query's output → file (once)
-- .output all.txt             ALL output → file until .output stdout
-- .mode csv                   combine with .once for CSV export
-- .excel                      send next result straight to a spreadsheet
-- .dump products              SQL text that recreates the table + data
-- .dump                       the whole database as SQL



-- ── getting data IN ────────────────────────────────────────
-- .import --csv data.csv items         load a CSV into a table
-- .import --csv --skip 1 data.csv t    skip a header row
-- .read 00_schema.sql                  execute a SQL file
-- .parameter set :cid 3                bind named parameters, then:
SELECT count(*) FROM orders WHERE customer_id = 3;   -- (use :cid in CLI)



-- ── session & diagnostics ──────────────────────────────────
-- .open other.db              switch database files
-- .timer on                   print elapsed time per statement
-- .eqp on                     auto-EXPLAIN QUERY PLAN every query
-- .changes on                 print rows-affected after DML
-- .bail on                    stop scripts at first error
-- .shell ls -la               run a shell command
-- .help / .quit



-- Practice (all in a real terminal)
-- Q1. Export delivered orders as orders.csv with headers.
-- Q2. .dump just the categories table and read the SQL it emits.
-- Q3. Turn on .eqp and .timer, then run one of section 14's queries.
-- Q4. Import your Q1 csv into a new table with .import --csv --skip 1.

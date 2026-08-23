---
title: SQLite Concepts — Multi-Level Outline
---

A structured, multi-level map of SQLite concepts — from the core SQL language
through engine internals and operations. Distilled from
`SQL_LEARNING_ROADMAP.md` and the book table of contents in
`sql contents.pdf`, refocused entirely on **SQLite**.

> ⚠️ = common gotcha · ⭐ = high day-to-day value

---

## 1. Foundations & Mental Model

- **What SQLite is**
  - Embedded, serverless, zero-configuration database library
  - The whole database is a **single file** (plus `-wal`/`-shm` sidecars in WAL mode)
  - In-process: your app links the library — no network, no daemon, no users
  - Public domain; the most deployed database engine in the world
- **What a relational database is**
  - Tables, rows, columns, relationships
  - Keys: primary, foreign, candidate, surrogate vs natural
  - Reading a schema / ER diagram; entity relationships (1:1, 1:N, M:N)
- **Database engine vs SQL dialect** — SQLite implements most of standard SQL with deliberate omissions and extensions
- **Declarative SQL** — describe *what* you want, not *how* to compute it
- **ACID** — atomicity, consistency, isolation, durability; the classic bank-transfer example
- **SQL statement categories**
  - DDL (define schema), DML (modify data), DQL (query), TCL (transactions)
  - DCL (`GRANT`/`REVOKE`) — ⚠️ does **not** exist in SQLite; access control is file permissions
- **When SQLite fits (and when it doesn't)**
  - Great: on-device/mobile, desktop apps, edge, caches, file formats, small-to-medium websites, testing
  - Poor fit: many concurrent writers, network-shared filesystems, fine-grained user permissions
- **Tooling**
  - `sqlite3` CLI
  - DB Browser for SQLite, SQLiteStudio, DBeaver
  - Language drivers (Python `sqlite3`, better-sqlite3, TypeORM, SQLAlchemy, …)

---

## 2. Core Querying — `SELECT`

- **Projection**
  - `SELECT` columns, `SELECT *` (⚠️ avoid in app code), column aliases (`AS`)
  - Calculated/derived columns (expressions in the select list)
  - `DISTINCT` vs duplicate rows
- **Filtering — `WHERE`**
  - Comparison operators: `=` `!=` `<>` `<` `>` `<=` `>=` (💡 SQLite also accepts `==`)
  - Logical operators: `AND` / `OR` / `NOT`; parentheses and precedence
  - `BETWEEN ... AND ...`
  - `IN (...)` / `NOT IN (...)`
  - `LIKE` with `%` and `_`; `ESCAPE` clause
    - ⚠️ SQLite `LIKE` is case-insensitive for **ASCII only**; there is no `ILIKE`
  - `GLOB` (Unix-glob matching, case-sensitive — SQLite-specific)
  - `REGEXP` — parsed but ⚠️ no default implementation; must register a `regexp()` function
  - `IS NULL` / `IS NOT NULL`; `IS` / `IS NOT` (null-safe comparison)
  - `IS DISTINCT FROM` / `IS NOT DISTINCT FROM` (3.39+)
  - `EXISTS (subquery)`
- **Sorting — `ORDER BY`**
  - `ASC` / `DESC`, multiple sort keys
  - Ordering by alias or column position
  - `NULLS FIRST` / `NULLS LAST` (3.30+); ⚠️ NULLs sort first by default
  - `COLLATE` in ordering (`NOCASE`, `BINARY`, `RTRIM`)
- **Paging**
  - `LIMIT` and `OFFSET`
  - ⭐ Keyset/cursor pagination (`WHERE id > :last ORDER BY id LIMIT n`) vs `OFFSET` (degrades on large tables)
- **Conditional expressions**
  - `CASE WHEN ... THEN ... ELSE ... END` (searched and simple forms)
  - `IIF(cond, a, b)`
- **⚠️ Logical order of evaluation**: `FROM → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT`

---

## 3. Operators, Expressions & NULL

- **Three-valued logic** — `NULL` is *unknown*: `NULL = NULL` is not true; ⚠️ `= NULL` never matches → use `IS NULL`
- **NULL functions**
  - `COALESCE(a, b, ...)` — first non-null
  - `IFNULL(a, b)` (two-arg form), `NULLIF(a, b)`
  - `MAX(a, b, ...)` / `MIN(a, b, ...)` scalar forms — return NULL if any argument is NULL
- **NULL behavior**
  - Ignored by most aggregates (`COUNT(col)` skips NULLs; `COUNT(*)` doesn't)
  - ⚠️ `NOT IN` + NULLs → silent empty results; prefer `NOT EXISTS`
  - `'a' || NULL → NULL`
  - Data-cleaning idioms: replace NULL with 0 / with a computed average
- **String & arithmetic operators**
  - `||` concatenation; `concat()` / `concat_ws()` (3.44+)
  - `+ - * / %`; ⚠️ integer division truncates (`5 / 2 → 2`; use `5.0 / 2`)
  - Bitwise: `& | ~ << >>`
- **Casting** — `CAST(x AS type)` only (⚠️ no Postgres-style `x::type`); implicit affinity conversions
- **Literals & quoting** (the big footgun section)
  - String literals: **single quotes** `'text'`; escape by doubling: `'it''s'`
  - ⚠️ **No backslash escapes** — `'\n'` is two characters
  - Identifiers: `"col"` (standard), plus compatibility forms `` `col` `` and `[col]`
  - ⚠️ **Classic SQLite bug**: a double-quoted token that matches no column is silently treated as a **string literal** — `WHERE name = "John"` "works" by accident. Always single-quote strings.
  - Identifiers are case-insensitive (quoting does not change that)
  - Blob literals: `X'53514C697465'`
  - `TRUE`/`FALSE` keywords are aliases for `1`/`0` (3.23+)

---

## 4. Aggregation & Grouping

- **Aggregate functions**: `COUNT`, `SUM`, `TOTAL` (SQLite-specific: never NULL, always REAL), `AVG`, `MIN`, `MAX`
- `COUNT(*)` vs `COUNT(col)` vs `COUNT(DISTINCT col)`
- `group_concat(col, sep)` / `string_agg(col, sep)` (3.44+)
- `ORDER BY` and `FILTER (WHERE ...)` **inside** aggregate calls (3.44+)
- **`GROUP BY`**
  - One and multiple columns; grouping by expression
  - ⚠️ **Bare columns** in `GROUP BY` queries are allowed (an arbitrary row per group, MySQL-style) — a portability trap
  - 💡 Special case: bare columns with a lone `MIN()`/`MAX()` *do* come from the winning row
- **`HAVING`** — filters *after* grouping (vs `WHERE`, before)
- Histograms / frequency counts with `GROUP BY` + `COUNT`
- ⚠️ No `GROUPING SETS`, `ROLLUP`, or `CUBE` — emulate with `UNION ALL` or window functions
- Summary-report patterns: subtotals, top-N per group, largest distinct values

---

## 5. Joins

- `INNER JOIN` (and bare `JOIN`)
- ⭐ `LEFT JOIN` / `LEFT OUTER JOIN` — the workhorse
  - ⚠️ Filtering the right table in `WHERE` vs in `ON` changes results (WHERE turns it back into an inner join)
- `RIGHT JOIN` and `FULL OUTER JOIN` — only since **3.39** (2022)
- `CROSS JOIN` — cartesian products (deliberate and accidental)
  - 💡 In SQLite, `CROSS JOIN` also disables join reordering by the planner (a hint)
- `NATURAL JOIN` and `USING (col)` vs explicit `ON a.x = b.x`
- Self-joins; joining on multiple conditions; multi-table (3–4 table) joins
- Table aliases and readable join order
- Join-based DML patterns: deleting duplicates, `UPDATE ... FROM` (3.33+)

---

## 6. Subqueries & CTEs

- **Subquery placements**
  - Scalar subqueries (single value in `SELECT` or `WHERE`)
  - `WHERE ... IN / NOT IN (subquery)`
  - `EXISTS` / `NOT EXISTS`
  - Derived tables — subqueries in `FROM`
  - Correlated vs non-correlated subqueries
  - ⚠️ No `ANY` / `SOME` / `ALL` quantifiers — rewrite with `MIN`/`MAX` or `EXISTS`
- **Common Table Expressions** — `WITH name AS (...)`
  - Chaining multiple CTEs; readability over nested subqueries
  - `AS MATERIALIZED` / `AS NOT MATERIALIZED` hints (3.35+)
- **Recursive CTEs** — `WITH RECURSIVE`
  - Sequences/number generation, trees & hierarchies, graph walks
  - `UNION` vs `UNION ALL` in the recursive step; cycle control with `LIMIT`
- Classic exercises: customers without orders, greatest-per-group (tallest student per classroom), 2nd/3rd largest value (`ORDER BY ... LIMIT 1 OFFSET n`), top-N per group

---

## 7. Set Operations

- `UNION` vs `UNION ALL` (dedup cost)
- `INTERSECT`
- `EXCEPT`
- Column count & type-compatibility rules; `ORDER BY`/`LIMIT` apply to the whole compound
- Compound `SELECT`s inside CTEs and views

---

## 8. Window Functions (3.25+) — the big level-up

- **Core syntax**: `func() OVER (PARTITION BY ... ORDER BY ...)`
- **Ranking**: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE(n)`, `PERCENT_RANK()`, `CUME_DIST()`
- **Offset**: `LAG(col, n, default)`, `LEAD(col, n, default)`
- **Frame-anchored values**: `FIRST_VALUE()`, `LAST_VALUE()`, `NTH_VALUE()`
- **Aggregates as windows**: running totals, moving averages, cumulative counts
- **Frame specs**: `ROWS` / `RANGE` / `GROUPS BETWEEN ... AND ...`; `EXCLUDE` clause
  - ⚠️ `LAST_VALUE` needs an explicit frame (`ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`) to behave as expected
- Named windows: `WINDOW w AS (...)`
- `FILTER (WHERE ...)` on window aggregates
- Applications: dedup with `ROW_NUMBER()`, sessionization, z-scores/statistics, cumulative revenue, ranking medals-table style reports

---

## 9. Data Types, Affinity & Storage Classes

- **The 5 storage classes**: `NULL`, `INTEGER`, `REAL`, `TEXT`, `BLOB`
- **Type affinity** — column types *suggest*, not enforce: `TEXT`, `NUMERIC`, `INTEGER`, `REAL`, `BLOB`
  - How declared type names map to affinity (the `VARCHAR(255)` → TEXT rules; length is ⚠️ ignored)
  - ⚠️ Dynamic typing: `'abc'` can land in an `INTEGER` column
- **`STRICT` tables** (3.37+) — real type enforcement; allowed types include `ANY`
- **Booleans** — no native type; `TRUE`/`FALSE` map to `1`/`0`
- **No dedicated date/time type** (see §10)
- **Numbers**
  - 64-bit signed integers; IEEE-754 doubles
  - ⚠️ Never store money as `REAL` — use integer cents (no `DECIMAL`/`NUMERIC` exact type)
  - Large-number caveats: 15–17 significant digits in REAL; integer overflow behavior
- **Text & blobs** — UTF-8/UTF-16 encodings; blob I/O; `hex()`/`unhex()`, `randomblob()`, `zeroblob()`
- **Collating sequences**: `BINARY` (default), `NOCASE`, `RTRIM`; per-column and per-expression `COLLATE`; custom collations via the API
- Type introspection: `typeof(x)`

---

## 10. Dates, Times & Intervals

- **Storage conventions** (pick one and stick to it ⚠️)
  - TEXT — ISO-8601 strings (`'2026-08-22 14:30:00'`)
  - INTEGER — Unix epoch seconds
  - REAL — Julian day numbers
- **The date/time functions**
  - `date()`, `time()`, `datetime()`, `julianday()`, `unixepoch()`, `strftime()`, `timediff()` (3.43+)
  - Time values: `'now'`, epoch with `'unixepoch'` flag, `'localtime'` / `'utc'` conversion
  - **Modifiers**: `'+1 day'`, `'-3 months'`, `'start of month'`, `'start of year'`, `'weekday N'`
- **Date arithmetic & reporting patterns**
  - Extracting components (`strftime('%Y'/'%m'/'%d'/'%w'/'%W', ...)`)
  - Rounding/truncating dates (`'start of day'`, `'start of month'`)
  - Date ranges in `WHERE`; grouping by week/month (e.g., weekly revenue reports)
  - Converting strings to date values (data cleaning)
- Audit columns: `created_at`/`updated_at` with `DEFAULT (datetime('now'))` or `CURRENT_TIMESTAMP`
- ⚠️ Time zones are a manual concern — store UTC, convert at the edge

---

## 11. Built-in Functions

- **Scalar string functions**
  - `length()`, `substr()`/`substring()`, `instr()`, `replace()`, `trim()`/`ltrim()`/`rtrim()`, `upper()`, `lower()`, `printf()`/`format()`, `quote()`, `char()`, `unicode()`, `octet_length()` (3.43+)
- **Numeric/math functions**
  - `abs()`, `round()`, `sign()`, `random()`, `randomblob()`
  - Math extension (built-in since 3.35): `ceil()`, `floor()`, `pow()`, `sqrt()`, `exp()`, `ln()`, `log()`, `log2()`, trig (`sin`, `cos`, …), `pi()`, `mod()`
- **Utility/metadata functions**
  - `typeof()`, `coalesce()`, `ifnull()`, `nullif()`, `iif()`, `likely()`/`unlikely()`
  - `last_insert_rowid()`, `changes()`, `total_changes()`
  - `sqlite_version()`, `sqlite_source_id()`
- **Aggregates** — §4; **window functions** — §8; **JSON functions** — §16
- **Application-defined functions** — register scalar/aggregate/window functions and collations from the host language (C API, Python `create_function`, driver hooks)
- ⚠️ No stored procedures, no procedural language (no PL/SQL analog) — logic lives in the app or in triggers

---

## 12. Modifying Data (DML)

- **`INSERT`**
  - `INSERT INTO ... VALUES (...)`; multi-row `VALUES`
  - `INSERT INTO ... SELECT ...` (copying/appending between tables)
  - `INSERT OR REPLACE / IGNORE / ABORT / ROLLBACK / FAIL` (conflict-resolution clauses, also on `UPDATE`)
  - `DEFAULT VALUES`
- **Upserts** — `INSERT ... ON CONFLICT (cols) DO UPDATE SET ... / DO NOTHING`
  - `excluded.col` pseudo-table; conflict-target rules; multiple ON CONFLICT clauses (3.35+)
  - ⚠️ `INSERT OR REPLACE` **deletes then reinserts** (fires delete triggers, resets defaults) — different from upsert
- **`UPDATE`**
  - `UPDATE ... SET ... WHERE ...`
  - `UPDATE ... FROM other_table` (3.33+)
  - ⚠️ Test the `WHERE` as a `SELECT` first
- **`DELETE`**
  - `DELETE FROM ... WHERE ...`
  - ⚠️ No `TRUNCATE` — bare `DELETE FROM t` uses the fast "truncate optimization"
  - `DELETE`/`UPDATE ... LIMIT` only with compile-time option `SQLITE_ENABLE_UPDATE_DELETE_LIMIT` — portable form: `WHERE rowid IN (SELECT ... LIMIT n)`
- **`RETURNING`** clause (3.35+) on INSERT/UPDATE/DELETE
- `last_insert_rowid()` and `changes()` for feedback
- **Bulk loading**
  - CLI `.import` (CSV/TSV), `.mode csv`
  - Batch inserts inside one transaction (⭐ the single biggest bulk-insert speedup)
  - Populating tables from text/CSV files; merging CSV data (with pandas or shell tools)

---

## 13. Schema Definition (DDL)

- **`CREATE TABLE`**
  - Columns, type names (affinity), `IF NOT EXISTS`
  - `CREATE TABLE ... AS SELECT` (copies data, ⚠️ not constraints)
  - `TEMP`/`TEMPORARY` tables
  - `STRICT` and `WITHOUT ROWID` table options
- **Constraints**
  - `PRIMARY KEY` — single & composite
    - ⚠️ In ordinary (rowid) tables, PK columns can be NULL unless declared `NOT NULL` (legacy quirk); `INTEGER PRIMARY KEY` is the exception
  - `NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT` (literal, `CURRENT_TIMESTAMP`, or `(expression)`)
  - `FOREIGN KEY ... REFERENCES`
    - ⚠️ **Enforcement OFF by default** — `PRAGMA foreign_keys = ON;` per connection
    - `ON DELETE` / `ON UPDATE`: `CASCADE`, `SET NULL`, `SET DEFAULT`, `RESTRICT`, `NO ACTION`
    - `DEFERRABLE INITIALLY DEFERRED`
  - Conflict clauses on constraints (`ON CONFLICT ROLLBACK/ABORT/...`)
- **rowid & auto-increment**
  - The implicit `rowid`; `INTEGER PRIMARY KEY` as its alias
  - `AUTOINCREMENT` — what it actually guarantees (monotonic, no reuse) and why you usually ⚠️ don't need it; `sqlite_sequence`
  - `WITHOUT ROWID` tables — clustered-by-PK storage; when they win
- **Generated columns** (3.31+) — `GENERATED ALWAYS AS (...) VIRTUAL | STORED`
- **`ALTER TABLE`**
  - `RENAME TO`, `RENAME COLUMN`, `ADD COLUMN`, `DROP COLUMN` (3.35+)
  - ⚠️ Everything else (change type, alter constraints, reorder) requires the **12-step table-rebuild recipe** (new table → copy → drop → rename, inside a transaction)
- **`DROP TABLE [IF EXISTS]`**; DELETE vs DROP vs (no) TRUNCATE
- **Views**
  - `CREATE VIEW` / `DROP VIEW`; single-table and multi-table views
  - Advantages: abstraction, reusable joins, security-by-omission
  - ⚠️ Views are read-only — simulate updatable views with `INSTEAD OF` triggers
- **Triggers**
  - `CREATE TRIGGER` — `BEFORE`/`AFTER`/`INSTEAD OF` × `INSERT`/`UPDATE [OF col]`/`DELETE`
  - `FOR EACH ROW`, `WHEN` condition, `NEW.`/`OLD.` references
  - `RAISE(ABORT, 'msg')` for validation; recursive triggers pragma
  - Use cases: audit trails, updated_at maintenance, denormalized counters
- **Schema introspection**
  - `sqlite_schema` (aka `sqlite_master`) table
  - `PRAGMA table_info / table_xinfo / table_list / index_list / index_info / foreign_key_list`
  - CLI: `.schema`, `.tables`, `.indexes`
- ⚠️ No schemas/namespaces, no `GRANT`/`REVOKE`, no users/roles — one file, one namespace (use `ATTACH` for multiple files)

---

## 14. Indexes & Query Performance

- **Why indexes exist** — B-tree lookups vs full scans; SQLite stores tables *and* indexes as B-trees
- **Creating**
  - `CREATE [UNIQUE] INDEX ... ON table (cols)`; `IF NOT EXISTS`
  - Composite indexes — ⚠️ column order matters (leftmost-prefix rule)
  - Covering indexes (`USING COVERING INDEX` in plans)
  - Partial indexes — `CREATE INDEX ... WHERE ...`
  - Expression indexes — `CREATE INDEX ... ON t (lower(email))`
  - Implicit indexes from `PRIMARY KEY`/`UNIQUE`
  - Descending indexes, `COLLATE` in index definitions
- **Reading query plans**
  - `EXPLAIN QUERY PLAN` — `SCAN` vs `SEARCH`, which index, covering or not
  - `EXPLAIN` (bytecode/VDBE level — occasional deep dives)
- **The query planner**
  - `ANALYZE` and `sqlite_stat1` statistics; `PRAGMA optimize` (⭐ run periodically / on close)
  - Next-generation query planner; join reordering; `CROSS JOIN` as an ordering hint
  - `INDEXED BY` / `NOT INDEXED` hints; `likely()`/`unlikely()`
- **Index strategy**
  - ⭐ Always index foreign-key columns (SQLite doesn't do it for you)
  - When indexes hurt: write-heavy tables, low-cardinality columns; cost of over-indexing
  - Finding unused/missing indexes; index overhead & maintenance
  - ⚠️ Functions on indexed columns in `WHERE` defeat the index (unless you build an expression index)
  - ⚠️ `LIKE '%x'` (leading wildcard) can't use an ordinary index; `LIKE 'x%'` needs the right collation to use one
- **Query shaping**: `EXISTS` vs `IN` vs `JOIN`; pushing filters down; avoiding `SELECT *`; avoiding implicit type conversions
- **Micro/macro performance levers**: transactions around bulk writes, prepared statements, `PRAGMA cache_size` / `mmap_size` / `synchronous`, WAL mode

---

## 15. Transactions, Concurrency & Locking

- **Basics**
  - `BEGIN` / `COMMIT` / `ROLLBACK`; autocommit mode (every bare statement is its own transaction)
  - `BEGIN DEFERRED | IMMEDIATE | EXCLUSIVE` — ⭐ use `IMMEDIATE` for write transactions to avoid late `SQLITE_BUSY`
  - Savepoints: `SAVEPOINT`, `RELEASE`, `ROLLBACK TO`
- **ACID in SQLite** — atomic commit via journaling; durability vs `PRAGMA synchronous`
- **Isolation model**
  - `SERIALIZABLE` by default; one writer at a time, database-level locking
  - Lock states: UNLOCKED → SHARED → RESERVED → PENDING → EXCLUSIVE
  - `SQLITE_BUSY` / "database is locked" — causes and cures; `PRAGMA busy_timeout` ⭐
- **Journal modes** — `PRAGMA journal_mode`
  - Rollback journal: `DELETE` (default), `TRUNCATE`, `PERSIST`, `MEMORY`, `OFF`
  - **WAL** (Write-Ahead Logging) ⭐
    - Readers don't block the writer; writer doesn't block readers
    - The `-wal` and `-shm` files; checkpointing (`PRAGMA wal_checkpoint`, `wal_autocheckpoint`); WAL growth
    - Limitations: no network filesystems; persists in the DB file
- **Concurrency patterns**
  - Read snapshot semantics in WAL; `PRAGMA read_uncommitted` (shared-cache)
  - Multi-process vs multi-thread access; threading modes (serialized/multi-thread)
  - Connection pooling with one-writer discipline
- ⚠️ No MVCC row versioning, no row-level locks, no `SELECT ... FOR UPDATE` — design around single-writer

---

## 16. JSON

- **JSON1 functions** (built into core since 3.38)
  - Extraction: `json_extract()`, `->` and `->>` operators (3.38+)
  - Construction: `json_object()`, `json_array()`, `json_quote()`, `json()`
  - Modification: `json_set()`, `json_insert()`, `json_replace()`, `json_remove()`, `json_patch()`
  - Interrogation: `json_type()`, `json_valid()`, `json_array_length()`, `json_error_position()`
  - **Table-valued**: `json_each()`, `json_tree()` — unnest JSON into rows ⭐
  - Aggregates: `json_group_array()`, `json_group_object()`
- **JSONB** (3.45+) — binary storage format (`jsonb()`, `jsonb_extract()`, …): smaller, faster reparse
- JSON5 input support (3.43+)
- **Path syntax**: `'$.store.book[0].title'`
- Indexing JSON: expression indexes on `json_extract(...)`; generated columns over JSON + index ⭐
- Design judgment: JSON columns vs normalized tables

---

## 17. Full-Text Search & Extensions

- **FTS5** ⭐
  - `CREATE VIRTUAL TABLE ... USING fts5(...)`; content tables & external content
  - `MATCH` queries; phrase, prefix (`x*`), NEAR, boolean operators
  - Ranking: `bm25()`; auxiliary functions `highlight()`, `snippet()`
  - Tokenizers: `unicode61`, `porter`, `trigram`
  - Keeping FTS in sync with triggers
  - (Legacy: FTS3/FTS4)
- **R-Tree module** — spatial/range indexes (bounding boxes, geo queries)
- **Other virtual tables**: `generate_series`, `dbstat`, CSV virtual table, `carray`
- **Loadable extensions** — `.load` / `load_extension()`; notable ecosystem: sqlite-vec (vectors), spatialite (GIS)
- The virtual-table mechanism itself (writing your own via the API)

---

## 18. PRAGMAs, Configuration & Introspection

- **Behavior**: `foreign_keys` ⚠️, `recursive_triggers`, `defer_foreign_keys`, `case_sensitive_like` (deprecated), `trusted_schema`
- **Performance**: `journal_mode`, `synchronous` (OFF/NORMAL/FULL), `cache_size`, `mmap_size`, `temp_store`, `page_size`, `busy_timeout`
- **Maintenance/health**: `integrity_check` / `quick_check`, `optimize`, `wal_checkpoint`, `auto_vacuum` (+ `incremental_vacuum`), `secure_delete`
- **Introspection**: `table_info`, `table_list` (3.37+), `index_list`, `foreign_key_list`, `database_list`, `compile_options`, `user_version` ⭐ (poor-man's migration version), `application_id`, `schema_version`
- ⭐ A sane app-startup block: `foreign_keys=ON`, `journal_mode=WAL`, `synchronous=NORMAL`, `busy_timeout=5000`

---

## 19. Administration, Backup & the CLI

- **`sqlite3` CLI dot-commands**
  - Inspect: `.tables`, `.schema`, `.indexes`, `.dbinfo`, `.databases`
  - I/O: `.mode` (csv/json/table/box/…), `.headers`, `.output`, `.once`, `.import`, `.excel`
  - Maintenance: `.dump` (SQL export), `.backup`, `.recover`, `.clone`
  - Session: `.open`, `.read`, `.parameter`, `.timer`, `.eqp on`
- **Backup & restore**
  - `.backup` / Online Backup API vs naive file copy (⚠️ unsafe mid-write; copy `-wal` too or checkpoint first)
  - `.dump` to SQL text; `VACUUM INTO 'file.db'` (3.27+) ⭐
  - ⚠️ Backups are sensitive data — encrypt and access-control them
- **Maintenance**
  - `VACUUM` (rebuild/defragment/reclaim), `auto_vacuum` trade-offs
  - `ANALYZE` / `PRAGMA optimize`
  - Corruption: causes (broken filesystems, copied-while-writing, multiple links), `PRAGMA integrity_check`, `.recover` (3.40+)
- **Multiple databases** — `ATTACH DATABASE` / `DETACH`; cross-database queries and `schema.table` names; transactions across attached DBs
- **Special databases** — `:memory:`, temp DBs, shared-cache mode, deserialized/in-memory snapshots
- **Engine limits** — `SQLITE_MAX_*`: columns (2000 default), SQL length, attached DBs (10 default), page size, DB size (theoretical ~281 TB), depth limits

---

## 20. Programming with SQLite

- **API fundamentals** (any language)
  - Open/close connections; connection-per-thread patterns
  - Prepared statements & parameter binding ⭐ (`?`, `?N`, `:name`, `@name`, `$name`)
  - Step/reset/finalize lifecycle; statement caching
  - Reading results; column types at runtime
  - Error codes: `SQLITE_BUSY`, `SQLITE_LOCKED`, `SQLITE_CONSTRAINT`, extended result codes
- **Host-language integrations**
  - Python: `sqlite3` stdlib module, SQLAlchemy, pandas `read_sql`/`to_sql`, SQLiteDict
  - JavaScript/TypeScript: better-sqlite3, TypeORM (this repo's stack ⭐), Drizzle, WASM build (sql.js / official WASM, 3.40+)
  - Registering application-defined functions & collations from the host
- **ORM interaction** ⭐
  - The **N+1 query problem** — spotting and fixing (eager loading / JOINs)
  - Query builder vs repository vs raw SQL — when to drop down
  - Lazy vs eager relations
  - **Migrations**: generate, review, run, revert; deterministic migrations; `user_version` or a migrations table
  - ⚠️ TypeORM `synchronize: true` in production — never
- **Security in code**
  - ⭐ SQL injection: always parameterize; never string-concat user input
  - `PRAGMA trusted_schema`; limits as DoS defense (`sqlite3_limit`)
  - **SQLCipher** — page-level encryption at rest (`PRAGMA key`); the official SEE alternative
- **Sessions/changesets** — the session extension for diff/sync; ties into offline-first sync design (last-write-wins vs version vectors, tombstones, idempotent writes)

---

## 21. Data Modeling, Quality & Best Practices

- **Normalization** — 1NF → 2NF → 3NF (BCNF awareness); when to denormalize deliberately
- **Key strategy** — surrogate (`INTEGER PRIMARY KEY`) vs natural; integers vs UUIDs (store UUIDs as BLOB(16) or TEXT; consider UUIDv7 for ordering)
- **Naming conventions** — snake_case; singular vs plural tables; consistent index names
- **Referential integrity** — FK actions (`CASCADE`/`SET NULL`/`RESTRICT`); remember `PRAGMA foreign_keys=ON` ⚠️
- **Modeling patterns**
  - Soft deletes (`deleted_at`) vs hard deletes
  - Audit columns (`created_at`, `updated_at`) + trigger maintenance
  - History/temporal tables (versioned rows)
  - Trees: adjacency list (+ recursive CTE) vs materialized path vs nested sets
  - Polymorphic associations and their trade-offs
  - EAV — and when **not** to use it
  - Lookup/enum tables vs `CHECK (x IN (...))`
- **Data cleaning in SQL**
  - Replace NULLs (with 0, with averages), collapse mismatched attribute values, normalize casing/whitespace, string-to-date conversion
  - `UPDATE` + `CASE`/`replace()`/`trim()` idioms; staging tables
- **Anti-pattern checklist** ⚠️
  - `SELECT *` in app code · unindexed foreign keys · money as REAL · N+1 queries · implicit type conversions · `NOT IN` with NULLs · relying on bare `GROUP BY` columns · double quotes for strings · giant single transactions holding the write lock · `OFFSET` pagination on big tables
- **Portable SQL vs SQLite-specific SQL** — know which features travel (to Postgres/MySQL) and which don't (affinity, `PRAGMA`, rowid, `GLOB`, conflict clauses)

---

## 22. Version Highlights (know what's built in)

- **3.24** (2018) — UPSERT (`ON CONFLICT DO ...`)
- **3.25** (2018) — **window functions**; `ALTER TABLE RENAME COLUMN`
- **3.31** (2020) — **generated columns**
- **3.33** (2020) — `UPDATE ... FROM`
- **3.35** (2021) — **`RETURNING`**; `ALTER TABLE DROP COLUMN`; built-in math functions; `MATERIALIZED` CTE hints
- **3.37** (2021) — **`STRICT` tables**; `PRAGMA table_list`
- **3.38** (2022) — JSON `->` / `->>` operators; JSON in core by default
- **3.39** (2022) — **`RIGHT`/`FULL OUTER JOIN`**; `IS [NOT] DISTINCT FROM`
- **3.40** (2022) — official **WASM** build; `.recover`
- **3.43** (2023) — `timediff()`, `octet_length()`; JSON5
- **3.44** (2023) — `ORDER BY`/`FILTER` in aggregates; `concat()`, `string_agg()`
- **3.45** (2024) — **JSONB**
- **3.46–3.50** (2024–2025) — planner, PRAGMA, and WAL/VACUUM refinements
- ⚠️ Embedded/bundled SQLite (mobile OS, old distros) may predate **all** of the above — always check `sqlite_version()`

---

## Suggested learning order

1. **§1–§3** — mental model, SELECT, operators/NULL (the daily 80%)
2. **§4–§8** — aggregation, joins, subqueries/CTEs, sets, windows (query mastery)
3. **§9–§13** — types, dates, functions, DML, DDL (production competence)
4. **§14–§15, §18** — indexes, transactions/WAL, PRAGMAs (performance & reliability)
5. **§16–§17, §19–§20** — JSON, FTS, ops, programming APIs (specialization)
6. **§21–§22** — modeling judgment and version awareness (seniority)

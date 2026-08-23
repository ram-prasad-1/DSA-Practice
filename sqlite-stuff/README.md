# SQLite Practice Files

Topic-wise `.sql` practice files following [`SQLITE_CONCEPTS.md`](SQLITE_CONCEPTS.md)
(folder numbers match its section numbers). Each section folder has a
`00_schema.sql` that creates and seeds every table the section's files use.
Run it once (re-run anytime to reset the data), then work through the
numbered files in any order — they only query those shared tables.

## Running in PyCharm Professional (recommended)

PyCharm Pro bundles the DataGrip database tooling, which runs `.sql` files
statement-by-statement with results in a grid.

### One-time setup

1. **Create the data source**
   - Open the **Database** tool window (`View → Tool Windows → Database`, or the
     database icon in the right sidebar).
   - Click **+ → Data Source → SQLite**.
   - In **File**, enter a path for your scratch database, e.g.
     `sqlite-stuff/02-core-querying-select/play.db` (it doesn't need to
     exist — SQLite creates it on first connect).
   - If prompted with *"Download missing driver files"*, click **Download**.
   - Click **Test Connection**, then **OK**.
2. **Attach the console to your files**
   - Open any `.sql` file, e.g. `02-core-querying-select/01_select_basics.sql`.
   - A toolbar appears at the top of the editor. In the
     **session/data source selector**, pick the `play.db` data source
     (choose the default session when asked).
   - PyCharm remembers this per file; new files just need the same pick once.
3. *(Optional)* Set the SQL dialect so highlighting/completion match SQLite:
   `Settings → Languages & Frameworks → SQL Dialects` → set the
   `sqlite-stuff` folder to **SQLite**.

### Daily workflow

- First, run the section's `00_schema.sql` with the **Run** (▶) button in the
  editor toolbar — it (re)creates and seeds all tables. Re-run it whenever
  you want fresh data.
- Then in any other file, put the caret on a statement and press
  **`Cmd+Enter`** (`Ctrl+Enter` on Windows/Linux) — runs **just that
  statement**; results open in the grid below.
- If the caret is ambiguous, PyCharm pops a chooser — pick the statement (or
  select the exact text first and `Cmd+Enter` runs the selection).
- Explore the created tables live in the **Database** tool window
  (double-click a table to browse its rows). Refresh (⟳) if new tables
  don't show up.
- Multiple result tabs pile up per console; pin the ones you want to compare.

## Running from the terminal (alternative)

```sh
cd 02-core-querying-select

# create/reset the tables once
sqlite3 play.db ".read 00_schema.sql"

# then query interactively
sqlite3 play.db
sqlite> .headers on
sqlite> .mode box
sqlite> SELECT * FROM products;

# or run a whole practice file
sqlite3 play.db ".read 01_select_basics.sql"
```

## Folder layout

- `02-core-querying-select/` — SELECT basics, WHERE, ORDER BY, LIMIT/paging, CASE
  - `00_schema.sql` — a small store schema (categories, customers, products,
    orders, order_items + an order_totals view) with seed data; the section's
    files query only these tables
- `03-operators-null/` — three-valued logic, COALESCE/IFNULL/NULLIF, aggregates
  vs NULL, arithmetic/string/bitwise operators, casting & affinity, quoting
  footguns
  - `00_schema.sql` — same store schema, plus nullable `products.discount`
    and `customers.referred_by` for the NULL lessons
- `04-aggregation-grouping/` — aggregate functions, GROUP BY, HAVING,
  summary reports (monthly revenue, subtotals, ROLLUP emulation)
  - `00_schema.sql` — same store schema, unchanged
- `05-joins/` — INNER, LEFT (+ the ON-vs-WHERE gotcha), RIGHT/FULL OUTER
  (3.39+), CROSS & self-joins, multi-table chains
  - `00_schema.sql` — same store schema, plus an empty 'Webcams' category
    and a never-ordered product for the outer-join lessons
    *(sections 06+ copy this richer schema)*
- `06-subqueries-ctes/` — scalar & correlated subqueries, IN/EXISTS,
  derived tables, CTE chains, recursive CTEs (sequences, calendars, trees)
- `07-set-operations/` — UNION/UNION ALL, INTERSECT, EXCEPT, join
  equivalents (adds a `newsletter_subscribers` table)
- `08-window-functions/` — OVER/PARTITION BY, ranking & top-N per group,
  LAG/LEAD, frames, running totals, the LAST_VALUE gotcha
- `09-data-types-affinity/` — storage classes, affinity rules, STRICT
  tables + ANY, float traps, money-as-cents, collations
- `10-dates-times/` — date function family, modifiers, timezones,
  period grouping, gaps, cohorts
- `11-builtin-functions/` — string, math (3.35+ extension), and utility
  functions (printf, changes(), pragma_* table functions)
- `12-dml/` — INSERT variants, UPDATE/DELETE (+ UPDATE FROM), UPSERT,
  RETURNING *(mutates data in a 9000+ id range; files self-clean)*
- `13-ddl/` — constraints & FK actions, rowid/AUTOINCREMENT/WITHOUT ROWID,
  ALTER + the 12-step rebuild, generated columns, views & triggers,
  schema introspection
- `14-indexes-performance/` — index types, EXPLAIN QUERY PLAN,
  sargability traps, ANALYZE/optimize (adds a 5000-row `events` table)
- `15-transactions/` — BEGIN/COMMIT/ROLLBACK, savepoints, WAL,
  BEGIN IMMEDIATE, busy_timeout, the recommended startup block
- `16-json/` — ->/->>, json_set/remove, json_each/tree, JSON aggregates,
  indexing JSON, JSONB (adds a `product_specs` table)
- `17-fts-extensions/` — FTS5 (MATCH, rank, highlight/snippet, sync
  triggers), R-Tree, generate_series
- `18-pragmas/` — the startup block, behavior/performance pragmas,
  integrity checks, user_version migrations
- `19-admin-backup-cli/` — CLI dot-commands (⚠ terminal only),
  VACUUM / VACUUM INTO, .backup/.dump, ATTACH patterns
- `play.db` (per section folder) — your local scratch database; safe to delete
  anytime (`00_schema.sql` rebuilds it). Don't commit it.

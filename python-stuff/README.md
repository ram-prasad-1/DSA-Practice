# Python Practice Files

Topic-wise `.py` practice files distilled from the `python/core` notes,
one folder per category and one file per concept. Every file is a runnable
script: run it top-to-bottom to see the output, then edit and re-run.
Sections inside a file are separated by three blank lines and introduced by a
single `#` comment; each file ends with a short **Practice** block.

Targets Python 3.10+. A few files need something newer and say so in their
header — `11-typing/02_generics.py` uses PEP 695 syntax (3.12+),
`04-iteration-and-generators/06_itertools.py` uses `batched` (3.12+), and the
free-threading and subinterpreter notes in `13-concurrency/` assume 3.13+.

## Running in PyCharm

- Open any file and press **Ctrl+Shift+R** (macOS) / **Ctrl+Shift+F10** to run it.
- Or put the caret in a section and use **Execute selection in Python Console**
  (⌥⇧E) to run just those lines against a live console — closest to the
  statement-by-statement workflow of `sqlite-stuff`.
- The `08-modules-and-imports/` demos must run with the folder itself as the
  working directory (see below); set it in *Run → Edit Configurations →
  Working directory* if PyCharm defaults elsewhere.
- Files that start processes (`13-concurrency/02`–`04`) keep their whole body in
  `main()` under an `if __name__ == "__main__"` guard, because a spawned child
  re-imports the module. Don't unindent them.

## Running from the terminal

```sh
cd 04-iteration-and-generators
python 02_generators.py

# or the whole set
find . -name '*.py' -exec python {} \;
```

The import demos are the exception — they are about how you launch Python:

```sh
cd 08-modules-and-imports
python 01_import_rules.py        # runs the comparisons below for you
python demo/foo/foo.py           # fails: relative import, no parent package
python -m demo.foo.foo           # works: __package__ is set
python main.py                   # root entry point, absolute imports
```

## Folder layout

- `01-objects-and-names/` — pass by object reference, mutable defaults,
  multiple assignment and star targets, `is` vs `==` vs truthiness,
  shallow vs deep copy
- `02-strings-and-collections/` — `str` vs `bytes`, string prefixes and
  f-string format specs, dict rules and idioms, strong typing, lists/tuples/sets,
  slicing, the `collections` module
- `03-functions-and-decorators/` — `*args`/`**kwargs`, keyword- and
  positional-only parameters, PEP 448 unpacking, decorators with and without
  arguments, `functools.wraps`/`cache`, scope and closures (incl. late binding),
  `partial`/`singledispatch`/`total_ordering`
- `04-iteration-and-generators/` — iterable vs iterator, generators and
  `yield from`/`send`, comprehensions, `zip`/`map`/`filter`/`reduce`,
  sorting with `key`, `itertools`
- `05-classes-and-objects/` — `namedtuple` vs dataclasses, descriptors,
  `staticmethod`/`classmethod`, `__str__` vs `__repr__`, context managers,
  the `contextlib` toolbox, class basics (`super`/MRO), dunder protocols,
  `property`/`__slots__`, ABCs vs Protocols, `__init_subclass__`/metaclasses/`weakref`
- `06-errors-logging-debugging/` — exception details and tracebacks, module
  loggers and filters, `breakpoint()` and post-mortem `pdb`
- `07-stdlib-toolbox/` — `json`, `re` (searching, groups, lookaheads),
  `textwrap`/`math`/`random` helpers, `pprint` and profiling, small idioms,
  `enum`, `Decimal`/`Fraction`
- `08-modules-and-imports/` — import rules, `sys.path` vs `PYTHONPATH`, and a
  `demo/` package that shows what script-vs-`-m` changes
- `09-control-flow/` — `match`/`case` patterns and guards, `for`/`else`,
  `while`/`else`, the walrus operator
- `10-files-and-io/` — `open()` modes and encodings, iterating a file,
  `pathlib` (parts, globbing, create/rename/delete)
- `11-typing/` — annotations and unions, generics (PEP 695, `Self`, `ParamSpec`),
  `TypedDict`/`Literal`/`Final`/`NewType`/`Annotated`, narrowing and running
  mypy/pyright
- `12-async/` — coroutines and `await`, tasks/`gather`/`TaskGroup`/timeouts/
  cancellation, `async for`/`async with`/async generators, blocking-call traps
- `13-concurrency/` — threads and locks, `multiprocessing`,
  `concurrent.futures`, and what the GIL does and doesn't stop

Each file names the concept in its first line, so `grep -rn '^# ' .` gives a
one-screen table of contents.

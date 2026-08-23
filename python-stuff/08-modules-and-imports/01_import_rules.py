# 01. Import rules — absolute imports and explicit relative imports only
# Run: python 01_import_rules.py
# Then compare: python demo/foo/foo.py   vs   python -m demo.foo.foo
# (run both from this directory)



# Python 3 allows only absolute imports and explicit relative imports
# (from . import x); Python 2's implicit relative imports are gone
import sys
from pathlib import Path

print("__name__     =", __name__)
print("__package__  =", repr(__package__))
print("sys.path[0]  =", sys.path[0])



# explicit relative imports need __package__ to be set, which happens when the
# module is run or imported as part of a package — not as a plain script
print("relative imports available here:", bool(__package__))



# the tree used by the demo below
print(
    """
demo/
├── __init__.py
├── sample.py
├── bar/
│   ├── __init__.py
│   └── bar.py
└── foo/
    ├── __init__.py
    └── foo.py
main.py
""".strip()
)



# python demo/foo/foo.py
#   -> demo/foo/ lands on sys.path; the project root does not
#   -> __package__ is empty, so the relative import in foo.py fails
result = __import__("subprocess").run(
    [sys.executable, "demo/foo/foo.py"], capture_output=True, text=True
)
print("as a script  ->", result.stdout.strip() or result.stderr.strip().splitlines()[-1])



# python -m demo.foo.foo
#   -> the current directory lands on sys.path and __package__ = 'demo.foo'
#   -> relative imports work throughout demo/
result = __import__("subprocess").run(
    [sys.executable, "-m", "demo.foo.foo"], capture_output=True, text=True
)
print("with -m      ->", result.stdout.strip() or result.stderr.strip().splitlines()[-1])



# python -m main
#   -> same path setup, but main.py is __main__ with no package, so relative
#      imports do not work IN main.py; subpackages behave normally
result = __import__("subprocess").run(
    [sys.executable, "-m", "main"], capture_output=True, text=True
)
print("root entry   ->", result.stdout.strip() or result.stderr.strip().splitlines()[-1])



# rule of thumb: run code inside packages with `python -m pkg.module` from the
# project root; keep entry-point scripts at the root using absolute imports



# namespace packages (PEP 420, 3.3+): a directory without __init__.py can still
# be imported. Regular packages stay the norm for libraries — unambiguous and
# they support package-level initialization
print("demo has __init__.py:", Path("demo/__init__.py").exists())



# Practice
# Q1. Delete demo/foo/__init__.py and re-run both commands — does anything change?
# Q2. Add `from . import sample` to demo/foo/foo.py — which invocation still works?
# Q3. Why can this folder (08-modules-and-imports) never be a package name?

# Explicit relative import — works only when __package__ is set,
# i.e. `python -m demo.foo.foo`, not `python demo/foo/foo.py`

from ..bar.bar import label

if __name__ == "__main__":
    print(f"foo.py: __package__={__package__!r} imported label={label()}")

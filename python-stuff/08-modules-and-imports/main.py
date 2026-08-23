# Root entry point — absolute imports only, since __main__ has no package
# Run: python main.py   or   python -m main

from demo.bar.bar import label
from demo.sample import shout

if __name__ == "__main__":
    print(f"main.py: __package__={__package__!r} label={label()} shout={shout('hi')}")

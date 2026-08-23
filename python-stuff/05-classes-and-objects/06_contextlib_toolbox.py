# 06. contextlib toolbox — ContextDecorator, nullcontext, ExitStack, suppress
# Run: python 06_contextlib_toolbox.py



# ContextDecorator: the manager also works as a function decorator
from contextlib import ContextDecorator


class makeparagraph(ContextDecorator):
    def __enter__(self):
        print("<p>")
        return self

    def __exit__(self, *exc):
        print("</p>")
        return False


@makeparagraph()
def emit_html():
    print("Here is some non-HTML")


emit_html()
with makeparagraph():
    print("works as a with block too")



# @contextmanager functions get the decorator behaviour for free
from contextlib import contextmanager


@contextmanager
def banner():
    print("---")
    yield
    print("---")


@banner()
def report():
    print("report body")


report()



# nullcontext: a no-op manager for "sometimes there is nothing to manage"
import sys
from contextlib import nullcontext

path = None
cm = open(path) if path else nullcontext(sys.stdin)
with cm as f:
    print("stream is", f.name)



# ExitStack: a variable number of managers (and arbitrary cleanup callbacks)
from contextlib import ExitStack
from pathlib import Path

tmp = Path(__file__).with_name("scratch_a.txt")
tmp2 = Path(__file__).with_name("scratch_b.txt")
tmp.write_text("one")
tmp2.write_text("two")

filenames = [tmp, tmp2]
with ExitStack() as stack:
    files = [stack.enter_context(open(name)) for name in filenames]
    print([f.read() for f in files])
    stack.callback(lambda: print("cleanup callback runs last-in-first-out"))

tmp.unlink()
tmp2.unlink()



# suppress: a readable replacement for try/except/pass
from contextlib import suppress

with suppress(FileNotFoundError):
    Path("does-not-exist.txt").unlink()
print("no traceback")



# closing: turn an object with .close() into a context manager
from contextlib import closing


class Handle:
    def close(self):
        print("closed")


with closing(Handle()):
    print("using handle")



# redirect_stdout: capture prints from code you do not control
import io
from contextlib import redirect_stdout

buf = io.StringIO()
with redirect_stdout(buf):
    print("captured")
print("got:", buf.getvalue().strip())



# Practice
# Q1. Use ExitStack to open N files only if a flag is set, else use nullcontext.
# Q2. Why is `with suppress(Exception):` around a large block a bad idea?
# Q3. Rewrite the makeparagraph class as a @contextmanager function.

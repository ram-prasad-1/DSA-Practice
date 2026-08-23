# 05. Context managers — guaranteed setup/teardown around a block
# Run: python 05_context_managers.py



# reach for one whenever you see a paired pattern:
# open/close, lock/release, change/reset, enter/exit, start/stop



# class-based: __enter__ returns the value bound after `as`
class Session:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("open", self.name)
        return self

    def __exit__(self, exc_type, exc, tb):
        print("close", self.name)
        return False


with Session("db") as s:
    print("using", s.name)



# __exit__ runs even when the body raises; returning False re-raises
try:
    with Session("db") as s:
        raise RuntimeError("boom")
except RuntimeError as e:
    print("propagated:", e)



# returning a truthy value from __exit__ SUPPRESSES the exception (rarely wanted)
class Swallow:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        print("suppressing", exc_type.__name__ if exc_type else None)
        return True


with Swallow():
    raise ValueError("ignored")
print("still running")



# if __enter__ itself raises, __exit__ is NOT called — nothing was acquired
class BadEnter:
    def __enter__(self):
        raise OSError("cannot acquire")

    def __exit__(self, *exc):
        print("never printed")


try:
    with BadEnter():
        pass
except OSError as e:
    print("OSError:", e)



# generator-based: usually the shortest way to write one
from contextlib import contextmanager


@contextmanager
def session(name):
    print("open", name)
    try:
        yield name
    finally:
        print("close", name)


with session("cache") as name:
    print("using", name)

try:
    with session("cache"):
        raise RuntimeError("boom")
except RuntimeError:
    print("try/finally around yield is what guarantees cleanup")



# multiple managers in one with statement, closed in reverse order
with Session("a"), Session("b"):
    print("both open")



# Practice
# Q1. Write a context manager that times its block and prints the elapsed seconds.
# Q2. Write chdir(path) that restores the original directory on exit.
# Q3. Show a case where suppressing an exception in __exit__ hides a real bug.

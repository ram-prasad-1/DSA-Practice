# 02. Mutable default arguments — defaults are evaluated once, at def time
# Run: python 02_mutable_default_arguments.py



# one list is created at definition time and shared by every call
def bad(item, bucket=[]):
    bucket.append(item)
    return bucket


print(bad("a"))
print(bad("b"))
print(bad.__defaults__)



# the fix: a None sentinel, with a fresh object per call
def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket


print(good("a"))
print(good("b"))



# immutable defaults are safe — they cannot be mutated at all
def scale(values, factor=2):
    return [v * factor for v in values]


print(scale([1, 2, 3]))



# the same trap with dicts and sets
def register(name, seen=set()):
    seen.add(name)
    return seen


print(register("x"), register("y"))



# Practice
# Q1. Rewrite register() so each call starts with an empty set.
# Q2. When is a shared mutable default actually useful? (hint: a hand-rolled cache)
# Q3. What does `def f(x=[]) -> None: ...` show in f.__defaults__ after three calls that append?

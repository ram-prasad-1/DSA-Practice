# 02. Mutable default arguments — defaults are evaluated once, at def time
# Run: python 02_mutable_default_arguments.py



# one list is created at definition time and shared by every call
def bad(item, bucket=[]):
    bucket.append(item)
    return bucket


print(bad("a"))
print(bad("b"))
print(bad.__defaults__)




# Practice
# Q1. Rewrite register() so each call starts with an empty set.
# Q2. When is a shared mutable default actually useful? (hint: a hand-rolled cache)
# Q3. What does `def f(x=[]) -> None: ...` show in f.__defaults__ after three calls that append?

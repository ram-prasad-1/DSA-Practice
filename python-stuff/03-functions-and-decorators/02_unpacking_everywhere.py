# 02. Packing vs unpacking — same symbols, opposite directions
# Run: python 02_unpacking_everywhere.py



# in a definition * / ** pack; in a call they unpack
def move(x, y, z):
    print(x, y, z)


point = (1, 2, 3)
move(*point)

opts = {"x": 1, "y": 2, "z": 3}
move(**opts)



# since PEP 448 (3.5+) unpacking also works inside literals
defaults = {"debug": False, "level": "info"}
overrides = {"level": "debug"}
print({**defaults, **overrides})

list_a, list_b = [1, 2], [3, 4]
print([*list_a, *list_b], {*list_a, *list_b}, (*list_a, *list_b))



# multiple unpackings in one call, mixed with plain arguments
def show(*args, **kwargs):
    print(args, kwargs)


show(0, *list_a, *list_b, **defaults, extra=1)



# d1 | d2 (3.9+) is the modern alternative to {**d1, **d2}
print(defaults | overrides)



# assignment-side packing (PEP 3132)
first, *rest = [1, 2, 3, 4]
print(first, rest)



# unpacking consumes an iterator — useful, but one-shot
it = iter([1, 2, 3])
print([*it], [*it])



# Practice
# Q1. Merge three dicts so the first one wins on conflicts.
# Q2. Call move() with a dict that has an extra key — what error, and how do you absorb it?
# Q3. Flatten [[1,2],[3,4]] using * unpacking, then with itertools.chain.

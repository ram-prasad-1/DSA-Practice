# 04. zip, map, filter, reduce — lazy iterators, not lists
# Run: python 04_zip_map_filter_reduce.py



# zip pairs elementwise and stops at the shortest input
x = [1, 2, 3]
y = [4, 5, 6]
print(list(zip(x, y)))
print(list(zip(x, [4, 5])))



# strict=True (3.10+) raises instead of silently truncating
try:
    list(zip(x, [4, 5], strict=True))
except ValueError as e:
    print("ValueError:", e)



# zip(*rows) transposes
rows = [(1, 2), (3, 4), (5, 6)]
print(list(zip(*rows)))



# map applies a function lazily; it accepts several iterables
print(list(map(lambda s: f"a {s}", ["cat", "dog", "cow"])))
print(list(map(lambda a, b: a + b, [1, 2, 3], [5, 15, 25])))



# filter keeps truthy results; filter(None, it) drops falsy items
print(list(filter(lambda s: "o" in s, ["cat", "dog", "cow"])))
print(list(filter(None, [0, 1, "", "x", None, []])))



# reduce lives in functools — it is not a builtin in Python 3
from functools import reduce

print(reduce(lambda acc, s: f"{acc} | {s}", ["cat", "dog", "cow"]))
print(reduce(lambda a, b: a * b, [1, 2, 3, 4], 1))



# modern style: a comprehension is usually clearer than map/filter with a lambda
animals = ["cat", "dog", "cow"]
print([f"a {s}" for s in animals], [s for s in animals if "o" in s])



# map/filter stay useful with an existing named function
print(list(map(str.upper, animals)))



# they are one-shot iterators
m = map(str.upper, animals)
print(list(m), list(m))



# Practice
# Q1. Sum two lists elementwise, once with zip and once with map.
# Q2. Replace reduce(lambda a,b: a+b, nums) with a builtin.
# Q3. What does list(zip()) return, and what about list(zip(*[])) ?

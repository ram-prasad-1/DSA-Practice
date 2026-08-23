# 05. Lists, tuples and sets — the other built-in containers
# Run: python 05_lists_tuples_sets.py



# list: mutable sequence
nums = [3, 1, 2]
nums.append(4)
nums.extend([5, 6])
nums.insert(0, 0)
print(nums)
print(nums.pop(), nums.pop(0), nums)
nums.remove(3)
print(nums, nums.index(2), nums.count(2))
nums.reverse()
print(nums)



# append vs extend — a classic mix-up
a, b = [1], [1]
a.append([2, 3])
b.extend([2, 3])
print(a, b)



# tuple: immutable sequence, hashable if its contents are
t = (1, "two", 3.0)
print(t, t[1], len(t), t + (4,), t * 2)
try:
    t[0] = 9
except TypeError as e:
    print("TypeError:", e)



# the comma makes the tuple, not the parentheses
print(type((1)), type((1,)))
single = 1,
print(single, type(single), ())



# tuple as a record and as a dict key
point = (10, 20)
seen = {point: "origin-ish"}
print(seen[(10, 20)])
try:
    {([1], 2): "x"}
except TypeError as e:
    print("TypeError:", e)



# set: unordered, unique, membership in O(1)
s = {3, 1, 2, 2}
print(s, len(s), 2 in s)
s.add(4)
s.discard(99)
print(s)
try:
    s.remove(99)
except KeyError as e:
    print("KeyError:", e)



# the empty set needs set(), not {}
print(type({}), type(set()))



# set algebra: | union  & intersection  - difference  ^ symmetric difference
x, y = {1, 2, 3}, {3, 4}
print(x | y, x & y, x - y, y - x, x ^ y)
print(x.issubset({1, 2, 3, 4}), {1, 2} <= x, x.isdisjoint({9}))



# the method forms accept any iterable; the operators require sets
print(x.union([4, 5]))
try:
    x | [4, 5]
except TypeError as e:
    print("TypeError:", e)



# frozenset is the hashable, immutable set
fs = frozenset([1, 2])
print(fs, {fs: "usable as a key"}[frozenset([2, 1])])



# choosing: list for order and duplicates, tuple for fixed records,
# set for membership and dedupe, dict when you need a value per key
words = ["b", "a", "b"]
print(len(words), len(set(words)), sorted(set(words)))



# Practice
# Q1. Find items in list A missing from list B, preserving A's order.
# Q2. Why is `x in a_set` far faster than `x in a_list` for large collections?
# Q3. Predict: {1, True, 1.0} — how many elements, and why?

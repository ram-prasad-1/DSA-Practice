# 03. Dictionaries — hashable keys, guaranteed order, modern idioms
# Run: python 03_dictionaries.py



# keys must be hashable — in practice, immutable
ok = {"s": 1, 2: "int", (3, 4): "tuple", frozenset({5}): "frozenset"}
print(list(ok))

try:
    {[1, 2]: "list"}
except TypeError as e:
    print("TypeError:", e)



# insertion order is a language guarantee since 3.7
d = {}
for key in "cba":
    d[key] = key.upper()
print(d)



# merge operators (3.9+)
a = {"x": 1}
b = {"y": 2, "x": 99}
print(a | b)
a |= b
print(a)



# safe reads and accumulating writes
d = {"k": 1}
print(d.get("missing"), d.get("missing", 0))
d.setdefault("list", []).append("item")
print(d)



# defaultdict beats repeated setdefault for multi-value maps
from collections import defaultdict

groups = defaultdict(list)
for word in ["ant", "bee", "ape", "bat"]:
    groups[word[0]].append(word)
print(dict(groups))



# comprehensions and iteration
squares = {n: n * n for n in range(5)}
print(squares)
for k, v in squares.items():
    print(f"{k}={v}", end=" ")
print()



# OrderedDict still differs: order-sensitive equality and move_to_end()
from collections import OrderedDict

print({"a": 1, "b": 2} == {"b": 2, "a": 1})
print(OrderedDict(a=1, b=2) == OrderedDict(b=2, a=1))



# fromkeys doubles as an order-preserving dedupe
print(list(dict.fromkeys(["b", "a", "b", "c", "a"])))



# Practice
# Q1. Invert a dict {k: v} into {v: k} — what breaks when values repeat?
# Q2. Count word frequencies two ways: defaultdict(int) and collections.Counter.
# Q3. Why can a tuple of lists not be a key, even though tuples are immutable?

# 07. collections — Counter, deque, defaultdict, ChainMap
# Run: python 07_collections_module.py



# Counter: a dict subclass for tallying
from collections import Counter

words = "the quick the lazy the dog".split()
c = Counter(words)
print(c, c["the"], c["absent"])
print(c.most_common(2), sum(c.values()))



# counters do arithmetic and accept an update from any iterable or mapping
other = Counter(["the", "cat"])
print(c + other, c - other)
print(c & other, c | other)
c.update(["dog", "dog"])
print(c["dog"])



# elements() expands the tally back out; total() (3.10+) sums it
print(sorted(Counter("aab").elements()), Counter("aab").total())



# defaultdict: a factory fills in missing keys on first access
from collections import defaultdict

groups = defaultdict(list)
for w in words:
    groups[w[0]].append(w)
print(dict(groups))

tally = defaultdict(int)
for w in words:
    tally[w] += 1
print(dict(tally))



# the factory takes no arguments — pass a lambda for anything that needs one
nested = defaultdict(lambda: defaultdict(int))
nested["a"]["b"] += 1
print(nested["a"])



# careful: a plain read INSERTS the default
d = defaultdict(list)
print(d["never-set"], dict(d))



# deque: fast appends and pops at BOTH ends (a list is O(n) at the left)
from collections import deque

q = deque([1, 2, 3])
q.appendleft(0)
q.append(4)
print(q, q.popleft(), q.pop(), q)



# maxlen gives a fixed-size sliding window that drops from the far end
window = deque(maxlen=3)
for n in range(6):
    window.append(n)
print(window)



# rotate and extendleft (which reverses what you give it)
q = deque("abcde")
q.rotate(2)
print("".join(q))
q = deque("ab")
q.extendleft("cd")
print("".join(q))



# ChainMap: search several mappings in order without merging them
from collections import ChainMap

defaults = {"color": "red", "size": "M"}
overrides = {"size": "L"}
cfg = ChainMap(overrides, defaults)
print(cfg["size"], cfg["color"], dict(cfg))



# writes only ever hit the first mapping; new_child layers another on top
cfg["color"] = "blue"
print(overrides, defaults)
print(dict(cfg.new_child({"size": "XL"})), cfg.maps)



# also here: namedtuple (see 05-classes-and-objects) and OrderedDict (see 03_dictionaries)
from collections import namedtuple, OrderedDict

print(namedtuple("P", "x y")(1, 2), list(OrderedDict.fromkeys("aba")))



# Practice
# Q1. Find the 3 most common characters in a file with Counter.
# Q2. Why is deque the right structure for a "last N events" buffer?
# Q3. Build a config that layers CLI args over env vars over defaults with ChainMap.

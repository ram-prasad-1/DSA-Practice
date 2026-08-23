# 06. itertools — fast, memory-efficient building blocks for iterators
# Run: python 06_itertools.py



# combinatorics
from itertools import permutations, combinations, combinations_with_replacement, product

print(["".join(p) for p in permutations("ABCD", 2)])
print(["".join(map(str, p)) for p in permutations(range(3))])
print(["".join(c) for c in combinations("ABCD", 2)])
print(["".join(c) for c in combinations_with_replacement("ABC", 2)])
print(["".join(p) for p in product("AB", "12")])
print(["".join(p) for p in product("AB", repeat=2)])



# groupby groups CONSECUTIVE elements only
from itertools import groupby

data = ["ant", "bee", "cow", "dodo", "emu"]
for key, group in groupby(data, key=len):
    print(key, list(group))



# so sort by the same key first for SQL-style grouping
data = ["dodo", "ant", "bee", "emu", "cow"]
for key, group in groupby(sorted(data, key=len), key=len):
    print(key, list(group))



# each group is invalidated once you advance to the next key
groups = [(k, g) for k, g in groupby(sorted(data, key=len), key=len)]
print([list(g) for _, g in groups])



# infinite iterators, bounded by islice or takewhile
from itertools import count, cycle, repeat, islice, takewhile

print(list(islice(count(10, 5), 4)))
print(list(islice(cycle("AB"), 5)))
print(list(repeat("x", 3)))
print(list(takewhile(lambda n: n < 5, count())))



# chaining, slicing, pairing, batching
from itertools import chain, pairwise, accumulate

print(list(chain.from_iterable([[1, 2], [3], [4, 5]])))
print(list(pairwise([1, 2, 3, 4])))
print(list(accumulate([1, 2, 3, 4])))

from itertools import batched

print([list(b) for b in batched(range(7), 3)])



# everything is lazy — wrap in list() to see the values
print(chain("ab", "cd"))



# Practice
# Q1. Use groupby to group words by first letter (remember the sort).
# Q2. Generate all 3-digit PIN codes with product(range(10), repeat=3) — how many?
# Q3. Read the recipes section of the itertools docs and implement `take(n, iterable)`.

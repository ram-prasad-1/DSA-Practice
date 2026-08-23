# 03. Comprehensions — declarative list/set/dict/generator building
# Run: python 03_comprehensions.py



# the four forms
print([n * n for n in range(5)])
print({n % 3 for n in range(5)})
print({n: n * n for n in range(5)})
print(sum(n * n for n in range(5)))



# filtering with if, and a conditional expression in the output slot
nums = range(10)
print([n for n in nums if n % 2 == 0])
print(["even" if n % 2 == 0 else "odd" for n in nums])



# nested for clauses read left-to-right, outer loop first
list_of_lists = [[0, 1, 2, 3], [0, 1, 2]]
flat = [y for x in list_of_lists for y in x]
print(flat)

manual = []
for x in list_of_lists:
    for y in x:
        manual.append(y)
print(manual == flat)



# nesting a comprehension inside a comprehension is a different shape
print([[y * 2 for y in x] for x in list_of_lists])



# itertools alternatives for flattening
import itertools

print(list(itertools.chain.from_iterable(list_of_lists)))
print(list(itertools.chain(*list_of_lists)))



# set union merges two lists but dedupes and loses order — not a flatten
list_one, list_two = [3, 1, 2], [2, 4]
print(list(set(list_one) | set(list_two)))



# the loop variable does not leak (unlike Python 2)
squares = [n * n for n in range(3)]
print("n" in dir())



# walrus in a comprehension: compute once, filter and use
words = ["alpha", "be", "gamma"]
print([length for w in words if (length := len(w)) > 3])



# Practice
# Q1. Build {word: len(word)} for words longer than 3 characters.
# Q2. Rewrite [y for x in lists for y in x if y] as explicit nested loops.
# Q3. Prefer chain.from_iterable over chain(*lists) — why does laziness matter here?

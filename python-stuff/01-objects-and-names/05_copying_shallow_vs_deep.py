# 05. Copying — assignment aliases, a shallow copy shares the inner objects
# Run: python 05_copying_shallow_vs_deep.py



import copy



# assignment is not a copy at all — both names point at one object
original = [1, 2, 3]
alias = original
alias.append(4)
print(original, alias is original)



# the four shallow-copy spellings
shallow = list(original)
print(shallow, shallow is original, shallow == original)
print(original[:], copy.copy(original), {"a": 1}.copy(), set("ab").copy())



# shallow means: a new outer container, the SAME inner objects
nested = [[1, 2], [3, 4]]
shallow = nested[:]
shallow.append([5])
shallow[0].append(99)
print(nested, shallow)
print(nested[0] is shallow[0])



# deepcopy recurses, so the inner objects are new too
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
deep[0].append(99)
print(nested, deep, nested[0] is deep[0])



# the same trap builds a grid with N aliases of one row
grid = [[0] * 3] * 2
grid[0][0] = 1
print(grid)
grid = [[0] * 3 for _ in range(2)]
grid[0][0] = 1
print(grid)



# copying an immutable is a no-op — there is nothing to protect
t = (1, 2)
print(copy.copy(t) is t, copy.deepcopy("abc") == "abc")



# but an immutable container holding mutables still shares them
pair = ([1], [2])
print(copy.copy(pair)[0] is pair[0], copy.deepcopy(pair)[0] is pair[0])



# deepcopy handles cycles and shared references
node = {"name": "a"}
node["self"] = node
clone = copy.deepcopy(node)
print(clone["self"] is clone)

shared = [1]
holder = [shared, shared]
clone = copy.deepcopy(holder)
print(clone[0] is clone[1])



# classes can customise both operations
class Box:
    def __init__(self, items):
        self.items = items

    def __copy__(self):
        print("  __copy__ called")
        return Box(self.items)

    def __deepcopy__(self, memo):
        print("  __deepcopy__ called")
        return Box(copy.deepcopy(self.items, memo))


b = Box([1, 2])
print(copy.copy(b).items, copy.deepcopy(b).items)



# deepcopy is slow and can be surprising (it copies everything reachable) —
# prefer building a fresh object, or copy only the level you actually need
print(copy.deepcopy({"cfg": {"retries": 3}}))



# Practice
# Q1. Write a function that returns a defensive copy of a dict of lists.
# Q2. Why does `dict(d)` not protect d's values from mutation?
# Q3. Predict: after `a = [[]] * 3; a[0].append(1)`, what is a?

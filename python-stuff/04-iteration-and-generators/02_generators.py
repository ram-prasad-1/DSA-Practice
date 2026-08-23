# 02. Generators — the easy way to write an iterator
# Run: python 02_generators.py



# a generator function returns a generator object, which is an iterator
def countdown(n):
    while n > 0:
        yield n
        n -= 1


print(list(countdown(4)))
gen = countdown(2)
print(type(gen), next(gen))



# generator expressions: same laziness, less code
squares = (x * x for x in range(10))
print(next(squares), sum(squares))



# laziness is the point — this never builds a huge list
def naturals():
    n = 0
    while True:
        yield n
        n += 1


from itertools import islice

print(list(islice(naturals(), 5)))



# execution pauses at each yield and resumes on the next next()
def traced():
    print("  start")
    yield 1
    print("  middle")
    yield 2
    print("  end")


for value in traced():
    print("got", value)



# yield from delegates to another iterable
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


print(list(flatten([1, [2, [3, 4]], 5])))



# a generator can receive values with send(), and return a final value
def accumulator():
    total = 0
    while True:
        received = yield total
        if received is None:
            return total
        total += received


acc = accumulator()
next(acc)
print(acc.send(5), acc.send(10))



# build a list only when you need random access or multiple passes
values = list(countdown(3))
print(values[0], len(values))



# Practice
# Q1. Write a generator that yields lines of a file with trailing whitespace stripped.
# Q2. Compare memory: sum(x*x for x in range(10**6)) vs sum([x*x for x in range(10**6)]).
# Q3. What does StopIteration carry when a generator hits a `return value` statement?

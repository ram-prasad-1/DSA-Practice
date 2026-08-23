# 01. Iterables vs iterators — an iterable can be looped, an iterator holds the position
# Run: python 01_iterables_vs_iterators.py



# iterable: has __iter__ (or __getitem__). iterator: has __next__ and returns self from __iter__
nums = [1, 2, 3]
it = iter(nums)
print(type(nums), type(it))
print(next(it), next(it), next(it))
try:
    next(it)
except StopIteration:
    print("StopIteration")



# every iterator is an iterable; the reverse is not true
print(hasattr(nums, "__iter__"), hasattr(nums, "__next__"))
print(hasattr(it, "__iter__"), hasattr(it, "__next__"))
print(iter(it) is it)



# iterators are single-pass; a list gives a fresh iterator each time
shared = iter(nums)
print(list(shared), list(shared))
print(list(nums), list(nums))



# what `for` really does
it = iter(nums)
while True:
    try:
        value = next(it)
    except StopIteration:
        break
    print(value, end=" ")
print()



# many builtins return lazy iterators, not lists
print(zip([1], [2]), map(str, nums), filter(None, nums), enumerate(nums), reversed(nums))



# next() with a default avoids the exception
empty = iter([])
print(next(empty, "fallback"))



# a hand-written iterator class
class Countdown:
    def __init__(self, start):
        self.n = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1


print(list(Countdown(4)))



# Practice
# Q1. Why does `sum(gen)` return 0 the second time you call it on the same generator?
# Q2. Make Countdown restartable (hint: separate the iterable from the iterator).
# Q3. Which of these can be indexed: list, generator, range, zip object?

# 06. Slicing — [start:stop:step] on any sequence
# Run: python 06_slicing.py



letters = list("abcdefg")
print(letters)



# start is inclusive, stop is exclusive — so stop - start is the length
print(letters[1:4], len(letters[1:4]))
print(letters[:3], letters[3:], letters[:])



# negative indices count from the end
print(letters[-1], letters[-2:], letters[:-2])



# step, and the reversal idiom
print(letters[::2], letters[1::2], letters[::-1], letters[::-3])



# slices never raise for out-of-range bounds (indexing does)
print(letters[2:99], letters[99:])
try:
    letters[99]
except IndexError as e:
    print("IndexError:", e)



# a slice of a list is a new (shallow) list — a cheap copy idiom
copy_of = letters[:]
print(copy_of == letters, copy_of is letters)



# slice assignment can replace, resize, insert or delete in place
nums = [0, 1, 2, 3, 4]
nums[1:3] = ["x", "y", "z"]
print(nums)
nums[1:4] = []
print(nums)
nums[len(nums):] = [9]
print(nums)
del nums[0:2]
print(nums)



# extended-slice assignment must match the length exactly
nums = [0, 1, 2, 3]
nums[::2] = ["a", "b"]
print(nums)
try:
    nums[::2] = ["a"]
except ValueError as e:
    print("ValueError:", e)



# strings and tuples slice the same way, but are immutable
s = "hello world"
print(s[6:], s[::-1], s[:5].upper())
try:
    s[0] = "H"
except TypeError as e:
    print("TypeError:", e)



# slice objects are first-class — name the ones you reuse
HEAD = slice(0, 3)
print(letters[HEAD], HEAD.indices(len(letters)))



# iterators cannot be sliced; use itertools.islice
from itertools import islice

gen = (n * n for n in range(10))
try:
    gen[2:4]
except TypeError as e:
    print("TypeError:", e)
print(list(islice((n * n for n in range(10)), 2, 5)))



# __getitem__ receives the slice object, so your own classes can support it
class Sequence:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, key):
        print("  key was", type(key).__name__, key)
        return self.data[key]


seq = Sequence(letters)
print(seq[1], seq[1:3])



# Practice
# Q1. Take every third element of a list, starting from the end.
# Q2. Replace the middle two items of a 6-item list with one item, in place.
# Q3. Why is s[::-1] a poor way to reverse a huge file's lines?

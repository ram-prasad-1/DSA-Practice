# 05. sorted() vs list.sort() — new list vs in place, both stable
# Run: python 05_sorting.py



# sort() mutates and returns None; sorted() returns a new list from any iterable
values = [5, 2, 3, 1, 4]
print(sorted(values), values)
print(values.sort(), values)
print(sorted({"b": 1, "a": 2}), sorted("cba"))



# key is applied to each element before comparison
print(sorted("This is a test string from Andrew".split(), key=str.lower))



# sort records by a field
students = [("john", "A", 15), ("jane", "B", 12), ("dave", "B", 10)]
print(sorted(students, key=lambda s: s[2]))



# operator.itemgetter / attrgetter are faster and clearer than index lambdas
from operator import itemgetter, attrgetter

print(sorted(students, key=itemgetter(1, 2)))

from collections import namedtuple

Student = namedtuple("Student", "name grade age")
people = [Student(*s) for s in students]
print(sorted(people, key=attrgetter("age"))[0])



# stability: equal keys keep their original order, so multi-pass sorting works
print(sorted(sorted(students, key=itemgetter(2)), key=itemgetter(1)))



# reverse=True, and descending on one key only via a negated value
print(sorted(values, reverse=True))
print(sorted(students, key=lambda s: (s[1], -s[2])))



# min/max take the same key argument
print(max(students, key=itemgetter(2)), min(students, key=itemgetter(2)))



# Practice
# Q1. Sort words by length, then alphabetically within the same length.
# Q2. Why does `x = mylist.sort()` leave x as None?
# Q3. Sort a list of dicts by a key that is missing in some of them (hint: dict.get).

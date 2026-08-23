# 09. property and __slots__ — computed attributes and lean instances
# Run: python 09_properties_and_slots.py



# start with a plain attribute; add a property only when you need logic
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.141592653589793 * self.radius**2


c = Circle(2)
print(round(c.area, 3))
try:
    c.area = 10
except AttributeError as e:
    print("AttributeError:", e)



# getter / setter / deleter — the setter is where validation belongs
class Account:
    def __init__(self, balance=0):
        self._balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("balance cannot be negative")
        self._balance = value

    @balance.deleter
    def balance(self):
        print("  resetting")
        self._balance = 0


acct = Account(100)
print(acct.balance)
acct.balance = 50
print(acct.balance)
try:
    acct.balance = -1
except ValueError as e:
    print("ValueError:", e)
del acct.balance
print(acct.balance)



# a property is a data descriptor on the CLASS (see 02_descriptors.py)
print(type(Account.__dict__["balance"]), Account.balance.fget.__name__)



# the point: you can turn a plain attribute into a property later without
# changing any calling code — so do not write Java-style getters up front



# cached_property computes once per instance and stores the result
from functools import cached_property


class Dataset:
    def __init__(self, rows):
        self.rows = rows

    @cached_property
    def summary(self):
        print("  computing")
        return sum(self.rows)


d = Dataset([1, 2, 3])
print(d.summary, d.summary, "summary" in d.__dict__)



# __slots__ replaces the instance __dict__ with fixed slots:
# less memory, faster attribute access, no ad-hoc attributes
class Slotted:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x, self.y = x, y


s = Slotted(1, 2)
print(s.x, s.y)
try:
    s.z = 3
except AttributeError as e:
    print("AttributeError:", e)
print(hasattr(s, "__dict__"))



# the memory win, measured
import sys


class Plain:
    def __init__(self, x, y):
        self.x, self.y = x, y


plain = Plain(1, 2)
print(sys.getsizeof(plain) + sys.getsizeof(plain.__dict__), sys.getsizeof(s))



# gotchas: a subclass without its own __slots__ regains a __dict__,
# and cached_property/weakref need one
class Child(Slotted):
    pass


print(hasattr(Child(1, 2), "__dict__"))


class BadCache:
    __slots__ = ("rows",)

    def __init__(self, rows):
        self.rows = rows

    @cached_property
    def total(self):
        return sum(self.rows)


try:
    BadCache([1]).total
except TypeError as e:
    print("TypeError:", e)



# dataclasses give you slots for free (3.10+)
from dataclasses import dataclass


@dataclass(slots=True)
class PointS:
    x: int
    y: int


print(PointS(1, 2), PointS.__slots__)



# Practice
# Q1. Give Circle a radius property that rejects non-positive values.
# Q2. Measure the memory of 100k slotted vs plain instances.
# Q3. Why does __slots__ + multiple inheritance often fail with a layout conflict?

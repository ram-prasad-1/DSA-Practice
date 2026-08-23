# 01. Namedtuple and dataclasses — lightweight records vs general data classes
# Run: python 01_namedtuple_and_dataclasses.py



# collections.namedtuple: a tuple whose elements also have names
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p, p.x, p[0])
x, y = p
print(x, y, len(p), isinstance(p, tuple))



# immutable — _replace returns a modified copy
print(p._replace(x=5), p)
print(p._asdict(), Point._fields)



# typing.NamedTuple is the preferred class syntax: hints, defaults, methods
from typing import NamedTuple


class Vec(NamedTuple):
    x: int
    y: int = 0

    def length2(self) -> int:
        return self.x**2 + self.y**2


v = Vec(3, 4)
print(v, v.length2(), Vec(1))



# dataclasses: auto __init__, __repr__, __eq__
from dataclasses import dataclass, field, asdict, replace


@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity: int = 0
    tags: list[str] = field(default_factory=list)

    def total_cost(self) -> float:
        return self.unit_price * self.quantity


item = InventoryItem("widget", 2.5, 4)
print(item)
print(item.total_cost(), item == InventoryItem("widget", 2.5, 4))
print(asdict(item), replace(item, quantity=10))



# mutable defaults must use default_factory — a bare [] raises at class creation
try:
    @dataclass
    class Broken:
        tags: list = []
except ValueError as e:
    print("ValueError:", e)



# frozen makes instances immutable and hashable; slots cuts memory (3.10+)
@dataclass(frozen=True, slots=True, order=True)
class Money:
    amount: int
    currency: str = "INR"


m = Money(100)
print(m, hash(m) is not None, m < Money(200))
try:
    m.amount = 5
except Exception as e:
    print(type(e).__name__, e)



# choosing: NamedTuple for small immutable records with tuple behavior,
# dataclass for behavior/mutability/many fields, plain dict only for dynamic keys
print(dict(v._asdict()), asdict(item)["name"])



# Practice
# Q1. Turn a (name, grade, age) tuple list into NamedTuples and sort by age.
# Q2. Add a __post_init__ to InventoryItem that rejects a negative quantity.
# Q3. Why is a frozen dataclass hashable but a plain one is not?

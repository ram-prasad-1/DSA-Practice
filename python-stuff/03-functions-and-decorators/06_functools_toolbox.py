# 06. functools toolbox — partial, singledispatch, total_ordering
# Run: python 06_functools_toolbox.py



# partial pre-binds arguments and returns a new callable
from functools import partial

def power(base, exponent):
    return base**exponent


square = partial(power, exponent=2)
two_to_the = partial(power, 2)
print(square(5), two_to_the(10))
print(square.func.__name__, square.keywords, two_to_the.args)



# it is the readable alternative to a lambda when you are only binding arguments
print(sorted(["10", "9"], key=partial(int, base=10)))
print(list(map(partial(round, ndigits=2), [1.234, 5.678])))



# partialmethod does the same inside a class body
from functools import partialmethod


class Cell:
    def __init__(self):
        self.alive = False

    def set_state(self, state):
        self.alive = bool(state)

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)


cell = Cell()
cell.set_alive()
print(cell.alive)



# singledispatch: one name, an implementation chosen by the first argument's type
from functools import singledispatch


@singledispatch
def describe(obj):
    return f"some {type(obj).__name__}"


@describe.register
def _(obj: int):
    return f"the integer {obj}"


@describe.register
def _(obj: list):
    return f"a list of {len(obj)}"


@describe.register(str)
def _(obj):
    return f"the string {obj!r}"


print(describe(3), describe([1, 2]), describe("hi"), describe(3.5))
print(describe.registry.keys())



# singledispatchmethod is the method version (dispatches on the 2nd argument)
from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    def render(self, value):
        return str(value)

    @render.register
    def _(self, value: bool):
        return "yes" if value else "no"


print(Formatter().render(True), Formatter().render(12))



# total_ordering fills in the missing comparison methods from __eq__ and one other
from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, major, minor):
        self.major, self.minor = major, minor

    def _key(self):
        return (self.major, self.minor)

    def __eq__(self, other):
        return self._key() == other._key()

    def __lt__(self, other):
        return self._key() < other._key()

    def __repr__(self):
        return f"Version({self.major}, {self.minor})"


v1, v2 = Version(1, 2), Version(1, 10)
print(v1 < v2, v1 <= v2, v1 > v2, v1 >= v2, v1 != v2)
print(sorted([v2, v1]), max(v1, v2))



# cheaper than total_ordering when a tuple key is enough: define __lt__ only,
# or use a dataclass with order=True



# also in functools: wraps and cache (see 03/04), reduce (see 04-iteration)
from functools import reduce, cached_property


class Report:
    def __init__(self, rows):
        self.rows = rows

    @cached_property
    def total(self):
        print("  computing once")
        return reduce(lambda a, b: a + b, self.rows)


r = Report([1, 2, 3])
print(r.total, r.total)
print("total" in r.__dict__)



# Practice
# Q1. Replace `lambda x: x.strip("#")` in a sort key with functools.partial.
# Q2. Use singledispatch to write a to_json(obj) that handles str, list and dict.
# Q3. Why does cached_property need a __dict__ (and so break with __slots__)?

# 08. Dunder protocols — making your objects behave like built-ins
# Run: python 08_dunder_protocols.py



# __eq__ and __hash__ are a contract: equal objects MUST hash equal
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))


p, q = Point(1, 2), Point(1, 2)
print(p == q, p is q, hash(p) == hash(q))
print(len({p, q}), {p: "usable as a key"}[q])



# defining __eq__ WITHOUT __hash__ makes the class unhashable
class NoHash:
    def __eq__(self, other):
        return True


try:
    {NoHash()}
except TypeError as e:
    print("TypeError:", e)



# returning NotImplemented lets Python try the reflected operation
print(p == "not a point", p.__eq__("not a point"))



# the container protocol: __len__, __getitem__, __contains__, __iter__
class Deck:
    def __init__(self, cards):
        self._cards = list(cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, key):
        return self._cards[key]

    def __contains__(self, card):
        return card in self._cards


deck = Deck(["A", "K", "Q", "J"])
print(len(deck), deck[0], deck[-1], deck[1:3], "K" in deck)
print(list(deck), [c for c in reversed(deck)])



# __getitem__ alone already makes an object iterable (the legacy protocol);
# __iter__ is the explicit, preferred way
print(iter(deck))



# __bool__ falls back to __len__, and to "always true" if neither exists
class Empty:
    def __len__(self):
        return 0


print(bool(Empty()), bool(Deck([])), bool(object()))



# operator overloading, with the reflected (__r*__) and in-place (__i*__) forms
class Vec:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __mul__(self, k):
        return Vec(self.x * k, self.y * k)

    __rmul__ = __mul__

    def __neg__(self):
        return self * -1

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5


v = Vec(3, 4)
print(v + Vec(1, 1), v * 2, 2 * v, -v, abs(v))



# ordering: define __lt__ (plus __eq__) and sorting works; @total_ordering fills the rest
class Version:
    def __init__(self, s):
        self.parts = tuple(int(n) for n in s.split("."))

    def __repr__(self):
        return ".".join(map(str, self.parts))

    def __lt__(self, other):
        return self.parts < other.parts


print(sorted([Version("1.10"), Version("1.2")]))



# __call__ makes an instance callable
class Adder:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        return x + self.n


add5 = Adder(5)
print(add5(10), callable(add5))



# __format__ powers f-string format specs
class Temp:
    def __init__(self, c):
        self.c = c

    def __format__(self, spec):
        return f"{self.c:{spec or 'g'}}°C"


print(f"{Temp(21.456)}", f"{Temp(21.456):.1f}")



# __enter__/__exit__ (context managers) and __get__/__set__ (descriptors)
# are the same idea — see files 05 and 02 in this folder



# Practice
# Q1. Add __sub__ and __eq__ to Vec, and make it hashable.
# Q2. Why must __hash__ never change over an object's lifetime?
# Q3. Implement __getitem__ on a class so that both obj[2] and obj[1:3] work.

# 10. Duck typing, ABCs and Protocols — three ways to say "behaves like"
# Run: python 10_abcs_and_protocols.py



# duck typing: if it quacks, it is a duck — no declared relationship needed
class Duck:
    def quack(self):
        return "quack"


class Person:
    def quack(self):
        return "I'm quacking"


def make_it_quack(thing):
    return thing.quack()


print(make_it_quack(Duck()), make_it_quack(Person()))



# EAFP (easier to ask forgiveness than permission) is the idiomatic style
def length_of(thing):
    try:
        return len(thing)
    except TypeError:
        return None


print(length_of("abc"), length_of(5))



# abc: an explicit contract, enforced at instantiation
from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def read(self, key): ...

    @abstractmethod
    def write(self, key, value): ...

    def copy(self, src, dst):
        self.write(dst, self.read(src))


try:
    Storage()
except TypeError as e:
    print("TypeError:", e)


class MemoryStore(Storage):
    def __init__(self):
        self.data = {}

    def read(self, key):
        return self.data.get(key)

    def write(self, key, value):
        self.data[key] = value


store = MemoryStore()
store.write("a", 1)
store.copy("a", "b")
print(store.data, isinstance(store, Storage))



# a half-implemented subclass still fails at instantiation, not at import
class Partial(Storage):
    def read(self, key):
        return None


try:
    Partial()
except TypeError as e:
    print("TypeError:", e)



# collections.abc gives ready-made contracts and free mixin methods
from collections.abc import Sequence, Iterable, Hashable


class Deck(Sequence):
    def __init__(self, cards):
        self._cards = list(cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, i):
        return self._cards[i]


deck = Deck("AKQJ")
print(len(deck), deck.index("Q"), deck.count("A"), list(reversed(deck)))
print(isinstance(deck, Sequence), isinstance([], Sequence), isinstance("s", Iterable))



# structural checks without inheriting anything
print(isinstance(5, Hashable), isinstance([], Hashable))



# typing.Protocol: static duck typing — the checker verifies the shape
from typing import Protocol, runtime_checkable


class Quacker(Protocol):
    def quack(self) -> str: ...


def quack_twice(thing: Quacker) -> str:
    return thing.quack() * 2


print(quack_twice(Duck()))



# a Protocol is not checkable at runtime unless you opt in
@runtime_checkable
class Closable(Protocol):
    def close(self) -> None: ...


class Handle:
    def close(self) -> None:
        pass


print(isinstance(Handle(), Closable), isinstance(5, Closable))



# runtime_checkable only checks that the METHOD NAMES exist, not signatures
class Liar:
    def close(self, extra_required_arg):
        pass


print(isinstance(Liar(), Closable))



# choosing: duck typing by default; Protocol when you want type-checker help
# without coupling; ABC when you own the hierarchy and want enforced structure
# plus shared implementation



# Practice
# Q1. Turn Storage into a Protocol and note what stops being enforced.
# Q2. Subclass collections.abc.Mapping with only 3 methods — what do you get free?
# Q3. Why is @runtime_checkable's isinstance check weaker than a static one?

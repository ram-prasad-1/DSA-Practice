# 02. Generics — one implementation, many types (PEP 695 syntax, 3.12+)
# Run: python 02_generics.py



# a generic function: the T links the parameter and the return type
def first[T](items: list[T]) -> T:
    return items[0]


print(first([1, 2, 3]), first(["a", "b"]))



# the pre-3.12 spelling, still everywhere in existing code
from typing import TypeVar

U = TypeVar("U")


def last(items: list[U]) -> U:
    return items[-1]


print(last([1, 2]), last("ab"))



# two type variables, and a constrained one
def pair[K, V](key: K, value: V) -> tuple[K, V]:
    return (key, value)


def concat[S: (str, bytes)](a: S, b: S) -> S:
    return a + b


print(pair("k", 1), concat("a", "b"), concat(b"a", b"b"))



# a bound: T must be a subtype of the bound
from decimal import Decimal


def total[N: (int, float, Decimal)](values: list[N]) -> N:
    result = values[0]
    for v in values[1:]:
        result += v
    return result


print(total([1, 2, 3]), total([Decimal("1.1"), Decimal("2.2")]))



# a generic class
class Stack[T]:
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T | None:
        return self._items[-1] if self._items else None


s: Stack[int] = Stack()
s.push(1)
s.push(2)
print(s.pop(), s.peek())



# the pre-3.12 class spelling
from typing import Generic

class Box(Generic[U]):
    def __init__(self, value: U) -> None:
        self.value = value


print(Box("wrapped").value)



# Self: a method that returns "the same class", subclasses included
from typing import Self


class Builder:
    def __init__(self) -> None:
        self.parts: list[str] = []

    def add(self, part: str) -> Self:
        self.parts.append(part)
        return self

    def build(self) -> str:
        return " ".join(self.parts)


print(Builder().add("hello").add("world").build())



# a generic alias, and a generic protocol
type Pair[T] = tuple[T, T]


def swap[T](p: Pair[T]) -> Pair[T]:
    a, b = p
    return (b, a)


print(swap((1, 2)), swap(("a", "b")))


from typing import Protocol


class Comparable(Protocol):
    def __lt__(self, other: Self, /) -> bool: ...


def smallest[C: Comparable](items: list[C]) -> C:
    result = items[0]
    for item in items[1:]:
        if item < result:
            result = item
    return result


print(smallest([3, 1, 2]), smallest(["b", "a"]))



# ParamSpec forwards a whole signature — this is how decorators stay typed
from collections.abc import Callable
import functools


def logged[**P, R](fn: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(fn)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print("  calling", fn.__name__)
        return fn(*args, **kwargs)

    return wrapper


@logged
def multiply(a: int, b: int) -> int:
    return a * b


print(multiply(3, 4))



# without ParamSpec you would have to fall back to Callable[..., Any]
# and lose every argument check at the call site



# runtime introspection of the type parameters
print(first.__type_params__, Stack.__type_params__)



# Practice
# Q1. Write a generic Cache[K, V] class with get/set and a typed default.
# Q2. When is a TypeVar bound better than a constrained TypeVar (a: (x, y))?
# Q3. Type a @retry decorator so the wrapped function keeps its signature.

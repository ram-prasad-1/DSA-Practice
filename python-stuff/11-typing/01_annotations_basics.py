# 01. Type hints — annotations are documentation the checker enforces, not the runtime
# Run: python 01_annotations_basics.py
# Check:  mypy 01_annotations_basics.py    or    pyright 01_annotations_basics.py



# annotate parameters and the return type
def greet(name: str, excited: bool = False) -> str:
    return f"Hello {name}" + ("!" if excited else "")


print(greet("ram", excited=True))



# nothing is enforced at runtime — this runs fine and a checker flags it
print(greet(42))



# variable annotations, with or without a value
count: int = 0
label: str
totals: list[float] = []
print(count, totals, "label" in dir())



# built-in generics since 3.9: list[int], dict[str, int], tuple[...], set[...]
def summarise(scores: dict[str, list[int]]) -> tuple[int, float]:
    flat = [n for values in scores.values() for n in values]
    return len(flat), sum(flat) / len(flat)


print(summarise({"a": [1, 2], "b": [3]}))



# tuple is special: fixed length vs homogeneous variable length
def fixed(pair: tuple[str, int]) -> str:
    return f"{pair[0]}={pair[1]}"


def variable(row: tuple[int, ...]) -> int:
    return sum(row)


print(fixed(("x", 1)), variable((1, 2, 3)))



# optional values: X | None (3.10+) replaces Optional[X]
def find(name: str) -> str | None:
    return name if name else None


print(find("x"), find(""))



# a union of several types
def render(value: int | float | str) -> str:
    return str(value)


print(render(1), render(1.5), render("a"))



# None as a return type means "returns nothing useful"
def log(message: str) -> None:
    print("  log:", message)


log("annotated")



# type aliases — the `type` statement (3.12+) or a plain assignment
type Matrix = list[list[float]]
Vector = list[float]


def scale(m: Matrix, k: float) -> Matrix:
    return [[cell * k for cell in row] for row in m]


print(scale([[1.0, 2.0]], 3))



# annotations are stored, and readable at runtime
print(greet.__annotations__)
print(summarise.__annotations__["return"])

from typing import get_type_hints

print(get_type_hints(greet))



# a string annotation ("forward reference") lets you name a class not yet defined
class Node:
    def __init__(self, value: int, next: "Node | None" = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value})"


print(Node(1, Node(2)).next)



# from __future__ import annotations makes ALL annotations lazy strings —
# useful for forward references, but get_type_hints() must resolve them



# Callable, and Any as the escape hatch that silences the checker
from collections.abc import Callable, Iterable, Sequence, Mapping
from typing import Any


def apply(fn: Callable[[int], str], values: Iterable[int]) -> list[str]:
    return [fn(n) for n in values]


print(apply(str, [1, 2]))


def anything(x: Any) -> Any:
    return x.whatever_the_checker_cannot_see if False else x


print(anything(1))



# prefer the abstract types for PARAMETERS and concrete ones for RETURNS:
# accept Iterable/Sequence/Mapping, return list/dict
def head(items: Sequence[str], meta: Mapping[str, int]) -> list[str]:
    return list(items[:1]) + sorted(meta)


print(head(["a", "b"], {"k": 1}))



# Practice
# Q1. Annotate a function that takes a list of dicts and returns a dict of lists.
# Q2. Why does `greet(42)` still run? What tool would have caught it?
# Q3. Replace Optional[list[str]] and Union[int, str] with the modern | syntax.

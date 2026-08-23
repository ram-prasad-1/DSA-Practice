# 03. TypedDict, Literal, Final, ClassVar, NewType, Annotated
# Run: python 03_typeddict_literal_final.py



# TypedDict describes the SHAPE of a plain dict
from typing import TypedDict, NotRequired, Required


class User(TypedDict):
    id: int
    name: str
    email: NotRequired[str]


u: User = {"id": 1, "name": "ram"}
print(u, u["name"])



# it is a plain dict at runtime — no validation, no instance check
print(type(u), isinstance(u, dict))
bad: User = {"id": "not an int", "name": "ram"}
print("runs anyway:", bad)



# total=False flips the default: every key optional unless marked Required
class Patch(TypedDict, total=False):
    name: str
    email: str
    id: Required[int]


print(Patch(id=1), Patch(id=1, name="x"))



# TypedDicts inherit, and expose their keys for introspection
class Admin(User):
    permissions: list[str]


print(Admin.__required_keys__, Admin.__optional_keys__)



# use TypedDict for JSON/API payloads you do not control;
# use a dataclass when you own the type and want methods and real instances
from dataclasses import dataclass


@dataclass
class UserObj:
    id: int
    name: str


print(UserObj(1, "ram"))



# Literal restricts a value to a fixed set — better than a bare str
from typing import Literal

Mode = Literal["r", "w", "a"]


def open_file(path: str, mode: Mode = "r") -> str:
    return f"opening {path} in {mode}"


print(open_file("x.txt", "w"))
print(open_file("x.txt", "z"))



# Literal is how you type a flag that changes the return type (with @overload)
from typing import overload


@overload
def parse(text: str, as_int: Literal[True]) -> int: ...
@overload
def parse(text: str, as_int: Literal[False] = False) -> str: ...
def parse(text: str, as_int: bool = False) -> int | str:
    return int(text) if as_int else text


print(parse("42", True) + 1, parse("42") + "!")



# Final: rebinding is a checker error (the value is still mutable)
from typing import Final

MAX_RETRIES: Final = 3
NAMES: Final[list[str]] = ["a"]
NAMES.append("b")
print(MAX_RETRIES, NAMES)



# ClassVar marks a class-level attribute so dataclasses skip it as a field
from typing import ClassVar
from dataclasses import fields


@dataclass
class Counter:
    count: int = 0
    instances: ClassVar[int] = 0

    def __post_init__(self) -> None:
        Counter.instances += 1


Counter(), Counter()
print(Counter.instances, Counter().count, [f.name for f in fields(Counter)])



# NewType makes a distinct type out of an existing one, with no runtime cost
from typing import NewType

UserId = NewType("UserId", int)
OrderId = NewType("OrderId", int)


def fetch_user(uid: UserId) -> str:
    return f"user {uid}"


uid = UserId(7)
print(fetch_user(uid), type(uid), uid + 1)
print(fetch_user(OrderId(7)))



# Annotated attaches metadata a library can read, without changing the type
from typing import Annotated, get_type_hints

Port = Annotated[int, "range 1-65535"]


def serve(port: Port = 8000) -> str:
    return f"serving on {port}"


print(serve())
print(get_type_hints(serve, include_extras=True)["port"])
print(get_type_hints(serve)["port"])



# Practice
# Q1. Type an API response as a TypedDict with an optional "next_page" key.
# Q2. Why does Final[list] not stop NAMES.append("b")?
# Q3. Use Literal + overload so a function returns bytes or str based on a flag.

# 04. Narrowing and running a checker
# Run: python 04_narrowing_and_checkers.py
# Check: mypy --strict 04_narrowing_and_checkers.py   /   pyright 04_narrowing_and_checkers.py



# a checker narrows a union as it reads the control flow
def length_of(value: str | list[str] | None) -> int:
    if value is None:
        return 0
    if isinstance(value, str):
        return len(value)
    return sum(len(v) for v in value)


print(length_of(None), length_of("abcd"), length_of(["a", "bb"]))



# the early-return guard is the idiomatic narrowing tool
def initial(name: str | None) -> str:
    if not name:
        return "?"
    return name[0].upper()


print(initial(None), initial("ram"))



# narrowing also happens via type(), attribute checks and truthiness
def describe(x: int | str | None) -> str:
    if type(x) is int:
        return f"int {x + 1}"
    if x:
        return f"non-empty str {x.upper()}"
    return "falsy"


print(describe(1), describe("a"), describe(None), describe(""))



# assert narrows too — but it disappears under python -O
def must(value: int | None) -> int:
    assert value is not None, "value is required"
    return value + 1


print(must(1))



# cast() tells the checker "trust me"; it does nothing at runtime
from typing import cast, Any

raw: Any = {"id": 1}
data = cast(dict[str, int], raw)
print(data["id"])
lying = cast(int, "definitely not an int")
print(type(lying))



# TypeGuard / TypeIs let YOUR predicate narrow for the checker
from typing import TypeGuard, TypeIs


def all_strings(values: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(v, str) for v in values)


def is_int(value: object) -> TypeIs[int]:
    return isinstance(value, int)


def shout(values: list[object]) -> list[str]:
    if all_strings(values):
        return [v.upper() for v in values]
    return []


print(shout(["a", "b"]), shout([1]))
print(is_int(3), is_int("3"))



# Any disables checking; object keeps it (you must narrow before using it)
def with_any(x: Any) -> int:
    return x.anything_at_all if False else 1


def with_object(x: object) -> int:
    if isinstance(x, int):
        return x
    return 0


print(with_any("s"), with_object(5), with_object("s"))



# assert_never makes an unhandled case a checker error — exhaustiveness for free
from typing import Literal, assert_never

Mode = Literal["r", "w"]


def handle(mode: Mode) -> str:
    match mode:
        case "r":
            return "reading"
        case "w":
            return "writing"
        case _:
            assert_never(mode)


print(handle("r"), handle("w"))



# reveal_type() is a checker-only builtin — it errors at runtime, so keep it
# commented out and uncomment while debugging a type
value: str | None = "x"
# reveal_type(value)



# running the checkers
#   pip install mypy         mypy --strict file.py
#   pip install pyright      pyright file.py
#   per-line escape hatch:   x = risky()  # type: ignore[arg-type]
#   whole-file opt-out:      # mypy: ignore-errors   (first line)
#   mypy config lives in pyproject.toml under [tool.mypy]
import shutil

print("mypy installed:", bool(shutil.which("mypy")), "| pyright:", bool(shutil.which("pyright")))



# start with no flags on new code, then turn on --strict per package;
# annotate signatures first — inference covers most locals for free



# Practice
# Q1. Add a "x" case to Mode and see which checker error assert_never produces.
# Q2. Why is `assert` a fragile narrowing tool in production code?
# Q3. Rewrite all_strings with TypeIs — what changes in the negative branch?

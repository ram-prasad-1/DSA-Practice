# 01. match/case — structural pattern matching (3.10+), not a switch statement
# Run: python 01_match_case.py



# literal patterns, alternatives with |, and the _ wildcard
def http_status(code):
    match code:
        case 200 | 201:
            return "ok"
        case 404:
            return "not found"
        case _:
            return "something else"


print(http_status(201), http_status(404), http_status(500))



# a bare name is a CAPTURE pattern, not a comparison — it always matches
# and REBINDS the name; adding a case after it is a SyntaxError
LIMIT = 10
match 3:
    case LIMIT:
        print("matched anything, and LIMIT is now", LIMIT)



# to compare against a constant, use a dotted name
class Limits:
    MAX = 10


def right(value):
    match value:
        case Limits.MAX:
            return "at the max"
        case _:
            return "below"


print(right(10), right(3))



# sequence patterns destructure, and *rest works
def describe(seq):
    match seq:
        case []:
            return "empty"
        case [single]:
            return f"one item: {single}"
        case [first, second]:
            return f"two: {first}, {second}"
        case [first, *rest]:
            return f"{first} then {len(rest)} more"


print(describe([]), "|", describe([1]), "|", describe([1, 2]), "|", describe([1, 2, 3]))



# a str is a sequence but is deliberately NOT matched by sequence patterns
print(describe("ab"))



# mapping patterns match a SUBSET of keys, and **rest collects the others
def route(request):
    match request:
        case {"method": "GET", "path": path}:
            return f"read {path}"
        case {"method": "POST", "body": {"name": name}}:
            return f"create {name}"
        case {"method": method, **extra}:
            return f"{method} with {sorted(extra)}"
        case _:
            return "malformed"


print(route({"method": "GET", "path": "/users", "trace": 1}))
print(route({"method": "POST", "body": {"name": "ram"}}))
print(route({"method": "DELETE", "id": 7}))



# class patterns match the type and pull out attributes
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def where(p):
    match p:
        case Point(x=0, y=0):
            return "origin"
        case Point(x=0, y=y):
            return f"on the y axis at {y}"
        case Point(x=x, y=0):
            return f"on the x axis at {x}"
        case Point():
            return "somewhere else"
        case _:
            return "not a point"


print(where(Point(0, 0)), "|", where(Point(0, 5)), "|", where(Point(2, 0)), "|", where("nope"))



# __match_args__ enables positional class patterns (dataclasses set it for you)
print(Point.__match_args__)
match Point(1, 2):
    case Point(1, y):
        print("positional pattern captured y =", y)



# guards add a condition to a matched pattern
def classify(n):
    match n:
        case int() if n < 0:
            return "negative int"
        case int() if n % 2 == 0:
            return "even int"
        case int():
            return "odd int"
        case str() | bytes():
            return "text-ish"
        case _:
            return type(n).__name__


print(classify(-2), classify(4), classify(7), classify("a"), classify(1.5))



# as-patterns keep the whole matched value while destructuring it
match {"method": "GET", "path": "/x"}:
    case {"method": "GET"} as req:
        print("captured whole:", req)



# no match and no _ case is simply a no-op, not an error
match 42:
    case "never":
        print("unreachable")
print("fell through silently")



# use match for shape-based dispatch (parsers, ASTs, messages, events);
# a dict lookup is still better for a flat value -> value mapping



# Practice
# Q1. Match a command list like ["move", "north"] / ["quit"] into actions.
# Q2. Why does `case LIMIT:` above match everything, and how many ways can you fix it?
# Q3. Rewrite the route() function as if/elif and compare readability.

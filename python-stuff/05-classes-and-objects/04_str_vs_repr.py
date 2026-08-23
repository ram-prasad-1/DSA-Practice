# 04. __str__ vs __repr__ — readable for users, unambiguous for developers
# Run: python 04_str_vs_repr.py



# repr() is for debugging, str() is for end users
import datetime

now = datetime.date(2026, 8, 23)
print(str(now), repr(now))
print(str("text"), repr("text"))



# with no __repr__ you get the default object repr
class Bare:
    pass


print(repr(Bare()))



# implement __repr__ for every class you write; add __str__ only when useful
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point(x={self.x!r}, y={self.y!r})"


p = Point(1, 2)
print(repr(p), str(p))



class Temp:
    def __init__(self, celsius):
        self.celsius = celsius

    def __repr__(self):
        return f"Temp(celsius={self.celsius!r})"

    def __str__(self):
        return f"{self.celsius}°C"


t = Temp(21)
print(t, repr(t))
print(f"{t} vs {t!r}")



# str() falls back to __repr__, never the other way round
print(str(p) == repr(p))



# containers use repr for their elements, and so does the REPL
print([t, t])
print({"here": p})



# a good __repr__ is ideally eval-able back into an equal object
back = eval(repr(p))
print(type(back).__name__, back.x, back.y)



# Practice
# Q1. Add __repr__ to a dataclass manually and compare with the generated one.
# Q2. Why does print(["a"]) show quotes but print("a") not?
# Q3. Implement __format__ on Temp so f"{t:.1f}" prints 21.0°C.

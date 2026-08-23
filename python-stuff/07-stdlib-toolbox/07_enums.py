# 07. enum — a fixed set of named constants
# Run: python 07_enums.py



from enum import Enum, IntEnum, StrEnum, Flag, auto, unique



# members are singletons: compare with is, not ==
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED, Color.RED.name, Color.RED.value, repr(Color.RED))
print(Color.RED is Color.RED, Color.RED == Color.GREEN)



# lookup by value or by name
print(Color(2), Color["BLUE"], list(Color))
try:
    Color(99)
except ValueError as e:
    print("ValueError:", e)



# auto() assigns the values for you when they carry no meaning
class Status(Enum):
    PENDING = auto()
    ACTIVE = auto()
    DONE = auto()


print([f"{s.name}={s.value}" for s in Status])



# enums are iterable, hashable and usable in dicts, sets and match statements
transitions = {Status.PENDING: Status.ACTIVE, Status.ACTIVE: Status.DONE}
print(transitions[Status.PENDING])

state = Status.ACTIVE
match state:
    case Status.ACTIVE:
        print("still running")
    case _:
        print("other")



# aliases: a duplicate value becomes an alias, @unique forbids it
class Shade(Enum):
    RED = 1
    CRIMSON = 1


print(Shade.CRIMSON is Shade.RED, list(Shade), Shade.__members__)

try:
    @unique
    class Strict(Enum):
        A = 1
        B = 1
except ValueError as e:
    print("ValueError:", e)



# plain Enum does NOT compare with its value — that is what IntEnum/StrEnum are for
print(Color.RED == 1)


class Priority(IntEnum):
    LOW = 1
    HIGH = 10


print(Priority.HIGH == 10, Priority.HIGH > Priority.LOW, sorted(Priority, reverse=True))


class Env(StrEnum):
    DEV = "dev"
    PROD = "prod"


print(Env.PROD == "prod", f"running in {Env.PROD}", "prod".upper() == Env.PROD.upper())



# methods and properties work like any class
class Planet(Enum):
    MERCURY = (3.303e23, 2.4397e6)
    EARTH = (5.976e24, 6.37814e6)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    @property
    def surface_gravity(self):
        return 6.67300e-11 * self.mass / self.radius**2


print(round(Planet.EARTH.surface_gravity, 2), round(Planet.MERCURY.surface_gravity, 2))



# Flag combines members with bitwise operators
class Perm(Flag):
    READ = auto()
    WRITE = auto()
    EXEC = auto()


mine = Perm.READ | Perm.WRITE
print(mine, Perm.READ in mine, Perm.EXEC in mine)
print(mine & Perm.WRITE, mine ^ Perm.READ, list(mine))



# functional creation, and why enums beat bare string constants:
# typos raise instead of silently passing, and the set of values is discoverable
Weekday = Enum("Weekday", "MON TUE WED")
print(list(Weekday), Weekday.MON.value)



# Practice
# Q1. Model an order lifecycle as an Enum plus a dict of legal transitions.
# Q2. When is StrEnum the right choice over Enum? (hint: JSON and DB round-trips)
# Q3. Why does `if status == "active":` survive a typo but `if status is Status.ACTIVE:` not?

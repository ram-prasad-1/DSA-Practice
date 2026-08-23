# 05. Inspection and profiling — pprint, type checks, cProfile
# Run: python 05_inspection_and_profiling.py



# pprint for nested structures
from pprint import pprint, pformat

my_dict = {"b": [1, 2, {"deep": True}], "a": {"x": 1, "y": 2}}
pprint(my_dict)
pprint(my_dict, sort_dicts=False)
pprint(sorted(dir(dict))[:6])
print(len(pformat(my_dict)))



# for JSON-shaped data, json.dumps(indent=2) is often nicer
import json

print(json.dumps(my_dict, indent=2))



# type checks: type() is the class, isinstance() respects subclasses
class Base:
    pass


class Child(Base):
    pass


c = Child()
print(type(c), type(c) is c.__class__)
print(type(c) is Base, isinstance(c, Base))
print(isinstance(Child, type), isinstance(True, int))



# prefer isinstance; accept several types with a tuple
print(isinstance(1, (int, float)), isinstance(1.0, int | float))



# useful introspection
import inspect


def add(a, b=2, *args, **kwargs):
    """Add numbers."""
    return a + b


print(inspect.signature(add))
print(add.__doc__, add.__name__, add.__module__)
print([n for n in dir(add) if n.startswith("__c")])
print(inspect.getsource(add).splitlines()[0])



# timing a snippet
import timeit

print(round(timeit.timeit("sum(range(100))", number=10000), 4))



# profiling: python -m cProfile my_script.py
#            python -m cProfile -s cumulative my_script.py
import cProfile
import io
import pstats


def work():
    return sum(x * x for x in range(20000))


profiler = cProfile.Profile()
profiler.enable()
work()
profiler.disable()
buf = io.StringIO()
pstats.Stats(profiler, stream=buf).sort_stats("cumulative").print_stats(3)
print("\n".join(buf.getvalue().splitlines()[:8]))



# Practice
# Q1. Profile a script with -s cumulative and identify the slowest call.
# Q2. Why is isinstance(True, int) True? What does that imply for `if x is True`?
# Q3. Use timeit to compare list(dict.fromkeys(xs)) against a set-based dedupe.

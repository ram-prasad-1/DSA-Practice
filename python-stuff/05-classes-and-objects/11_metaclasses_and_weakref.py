# 11. Class creation hooks and weakref — the deep end
# Run: python 11_metaclasses_and_weakref.py
# Reach for __init_subclass__ first; a metaclass is rarely the right answer



# classes are objects created at runtime — type() is the three-argument form
Dynamic = type("Dynamic", (object,), {"greet": lambda self: "hi", "version": 1})
print(Dynamic().greet(), Dynamic.version, type(Dynamic))
print(type(int), type(type))



# __init_subclass__ runs on the PARENT whenever a subclass is defined —
# it covers most of what people reach for metaclasses to do
class Plugin:
    registry = {}

    def __init_subclass__(cls, /, key=None, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry[key or cls.__name__.lower()] = cls


class JsonPlugin(Plugin, key="json"):
    pass


class CsvPlugin(Plugin):
    pass


print(Plugin.registry)



# __set_name__ is the other hook: a descriptor learns its own attribute name
class Field:
    def __set_name__(self, owner, name):
        self.name = name
        print(f"  Field bound to {owner.__name__}.{name}")


class Model:
    title = Field()



# a metaclass customises class CREATION itself (__new__/__init__ of the class)
class Uppercase(type):
    def __new__(mcls, name, bases, namespace, **kwargs):
        namespace = {
            k.upper() if not k.startswith("__") else k: v for k, v in namespace.items()
        }
        return super().__new__(mcls, name, bases, namespace, **kwargs)


class Shouty(metaclass=Uppercase):
    def speak(self):
        return "hello"


print([n for n in vars(Shouty) if not n.startswith("__")])
print(Shouty().SPEAK())



# metaclasses also let you intercept instance creation via __call__
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=Singleton):
    def __init__(self):
        self.loaded = True


print(Config() is Config())



# ABCMeta is the metaclass you already use — ABC is just a class using it
from abc import ABC, ABCMeta

print(type(ABC), isinstance(ABCMeta, type))



# weakref: a reference that does NOT keep the object alive
import weakref


class Resource:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Resource({self.name!r})"


r = Resource("db")
ref = weakref.ref(r)
print(ref(), ref() is r)
del r
print(ref())



# WeakValueDictionary: a cache that never prevents collection
cache = weakref.WeakValueDictionary()
keep = Resource("kept")
cache["kept"] = keep
cache["dropped"] = Resource("dropped")
print(sorted(cache.keys()))



# finalize registers a callback for when the object is collected
obj = Resource("temp")
weakref.finalize(obj, lambda: print("  finalized"))
del obj



# a weakref target needs __weakref__, which __slots__ removes unless listed
class NoWeak:
    __slots__ = ()


try:
    weakref.ref(NoWeak())
except TypeError as e:
    print("TypeError:", e)



# use weakref for caches, observer lists and parent back-pointers (breaking
# reference cycles); everywhere else, plain references are correct



# Practice
# Q1. Rewrite the Singleton metaclass using __new__ on the class itself.
# Q2. Replace a plugin-registry metaclass with __init_subclass__ — what shrinks?
# Q3. Why does a parent <-> child pair of strong references delay collection?

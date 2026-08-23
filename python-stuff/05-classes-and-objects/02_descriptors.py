# 02. Descriptors — objects that intercept attribute access
# Run: python 02_descriptors.py



# a class attribute is a descriptor if it defines __get__, __set__ or __delete__
class Positive:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive")
        obj.__dict__[self.name] = value


class Order:
    price = Positive()
    quantity = Positive()

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity


o = Order(10, 2)
print(o.price, o.quantity)
try:
    o.quantity = -1
except ValueError as e:
    print("ValueError:", e)



# __set_name__ (3.6+) tells the descriptor which name it was assigned to
print(Order.price.name, Order.quantity.name)



# a data descriptor defines __set__/__delete__ and wins over the instance __dict__;
# a non-data descriptor defines only __get__, so the instance __dict__ wins
class Data:
    def __get__(self, obj, objtype=None):
        return "from data descriptor"

    def __set__(self, obj, value):
        raise AttributeError("read-only")


class NonData:
    def __get__(self, obj, objtype=None):
        return "from non-data descriptor"


class Demo:
    data = Data()
    nondata = NonData()


d = Demo()
d.__dict__["data"] = "from instance dict"
d.__dict__["nondata"] = "from instance dict"
print(d.data)
print(d.nondata)



# descriptors only work as CLASS attributes
class Broken:
    def __init__(self):
        self.price = Positive()


print(type(Broken().price).__name__)



# @property is the one-off version; a descriptor is the reusable one
class Circle:
    def __init__(self, r):
        self._r = r

    @property
    def area(self):
        return 3.14159 * self._r**2


print(round(Circle(2).area, 3), type(Circle.__dict__["area"]).__name__)



# plain functions are non-data descriptors — that is how bound methods work
class Greeter:
    def hello(self):
        return "hi"


g = Greeter()
print(Greeter.hello, g.hello, g.hello.__self__ is g)
print(Greeter.__dict__["hello"].__get__(g, Greeter)())



# Practice
# Q1. Write a Typed descriptor that enforces isinstance(value, expected_type).
# Q2. Store descriptor state in obj.__dict__ vs on the descriptor itself — why does the latter break?
# Q3. Read the Descriptor HowTo and explain why __getattr__ is not part of this protocol.

# 07. Class basics — instances, inheritance, super() and the MRO
# Run: python 07_class_basics.py



# __init__ initialises an already-created instance; self is just the first argument
class Animal:
    kingdom = "Animalia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


a = Animal("generic")
print(a.name, a.speak(), a.kingdom)



# class attribute vs instance attribute — the lookup checks the instance first
b = Animal("other")
print(a.kingdom is b.kingdom, Animal.kingdom)
a.kingdom = "shadowed on a only"
print(a.kingdom, b.kingdom, a.__dict__, Animal.kingdom)



# a MUTABLE class attribute is shared by every instance — the classic bug
class Basket:
    items = []

    def add(self, item):
        self.items.append(item)


x, y = Basket(), Basket()
x.add("apple")
print(y.items, x.items is y.items)


class FixedBasket:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)


x, y = FixedBasket(), FixedBasket()
x.add("apple")
print(y.items)



# inheritance: override a method, and call the parent with super()
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{super().speak()} — woof"


d = Dog("rex", "lab")
print(d.speak(), d.breed, d.kingdom)
print(isinstance(d, Animal), issubclass(Dog, Animal), Dog.__bases__)



# super() is not "the parent" — it walks the MRO from the current class onward
class A:
    def who(self):
        return "A"


class B(A):
    def who(self):
        return "B -> " + super().who()


class C(A):
    def who(self):
        return "C -> " + super().who()


class D(B, C):
    def who(self):
        return "D -> " + super().who()


print(D().who())
print([cls.__name__ for cls in D.__mro__])



# so cooperative multiple inheritance needs every class to call super()
class Mixin:
    def greet(self):
        return "mixin"


class Combined(Mixin, Animal):
    pass


print(Combined("x").greet(), Combined("x").speak())



# an inconsistent hierarchy is rejected at class-creation time
try:
    class Bad(A, D):
        pass
except TypeError as e:
    print("TypeError:", e)



# attribute access hooks: __getattr__ runs only when normal lookup FAILS
class Lenient:
    def __init__(self):
        self.real = 1

    def __getattr__(self, name):
        return f"<no {name}>"


obj = Lenient()
print(obj.real, obj.missing)



# calling an unbound method needs an explicit instance
print(Animal.speak(a), a.speak())



# Practice
# Q1. Add a Cat(Animal) whose speak() does not call super() — what is lost?
# Q2. Draw the MRO of D by hand, then check it against D.__mro__.
# Q3. Why does `class Config: defaults = {}` bite, but `MAX = 10` not?

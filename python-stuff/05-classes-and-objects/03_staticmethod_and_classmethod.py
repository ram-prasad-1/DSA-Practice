# 03. staticmethod and classmethod — built-in descriptors that change binding
# Run: python 03_staticmethod_and_classmethod.py



class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    def describe(self):
        return f"pizza with {', '.join(self.toppings)}"

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomato"])

    @staticmethod
    def validate(topping):
        return topping in {"mozzarella", "tomato", "basil"}


p = Pizza.margherita()
print(p.describe())
print(Pizza.validate("basil"), Pizza.validate("pineapple"))



# classmethod receives the class, so alternative constructors respect subclasses
class DeepDish(Pizza):
    def describe(self):
        return "deep dish " + super().describe()


print(type(DeepDish.margherita()).__name__)
print(DeepDish.margherita().describe())



# staticmethod gets no implicit argument — a namespaced plain function
print(Pizza.validate is Pizza.__dict__["validate"].__get__(None, Pizza))
print(p.validate("tomato"))



# what each one binds to
print(Pizza.describe)
print(p.describe)
print(Pizza.margherita)
print(Pizza.validate)



# instance vs class vs static, side by side
class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1

    def one(self):
        return ("instance", self)

    @classmethod
    def two(cls):
        return ("class", cls.total)

    @staticmethod
    def three():
        return ("static", "no implicit arg")


Counter(), Counter()
c = Counter()
print(c.one()[0], Counter.two(), Counter.three())



# staticmethods are callable directly since 3.10
f = Counter.__dict__["three"]
print(f())



# Practice
# Q1. Add a from_string classmethod to Pizza that parses "mozzarella,basil".
# Q2. Why would making margherita a staticmethod break DeepDish.margherita()?
# Q3. When is a module-level function a better choice than a staticmethod?

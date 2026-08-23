# 05. Scope and closures — LEGB, nonlocal, and late binding
# Run: python 05_scope_and_closures.py



# name lookup order: Local, Enclosing, Global, Built-in
value = "global"


def outer():
    value = "enclosing"

    def inner():
        print("inner sees:", value)

    inner()


outer()
print("module sees:", value)



# assigning to a name makes it local for the WHOLE function body
def broken():
    try:
        print(value)
        value = "local"
    except UnboundLocalError as e:
        print("UnboundLocalError:", e)


broken()



# global rebinds a module-level name; nonlocal rebinds the enclosing one
counter = 0


def bump_global():
    global counter
    counter += 1


bump_global()
print("counter:", counter)


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = make_counter()
print(c(), c(), c())



# a closure is a function that remembers the enclosing names it uses
def multiplier(factor):
    def multiply(n):
        return n * factor

    return multiply


double, triple = multiplier(2), multiplier(3)
print(double(5), triple(5))
print(double.__code__.co_freevars, double.__closure__[0].cell_contents)



# the two counters are independent — each call built a fresh cell
a, b = make_counter(), make_counter()
print(a(), a(), b())



# LATE BINDING: the closure reads the variable when CALLED, not when created
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])



# fixes: a default argument captures the value now...
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])



# ...or functools.partial binds it explicitly
from functools import partial

funcs = [partial(lambda i: i, i) for i in range(3)]
print([f() for f in funcs])



# the same bug with a loop over handlers
handlers = []
for name in ("a", "b"):
    handlers.append(lambda: f"handling {name}")
print([h() for h in handlers])

handlers = []
for name in ("a", "b"):
    handlers.append(lambda name=name: f"handling {name}")
print([h() for h in handlers])



# comprehensions have their own scope, so the loop name never leaks
squares = [n * n for n in range(3)]
print("n" in dir(), "value" in dir())



# class bodies are a scope that nested functions do NOT see
class Demo:
    attr = "class attribute"

    def method(self):
        try:
            return attr
        except NameError as e:
            return f"NameError: {e}"


print(Demo().method(), Demo.attr)



# Practice
# Q1. Write make_accumulator() that returns a function summing everything it is given.
# Q2. Fix `[lambda: i * 2 for i in range(3)]` two different ways.
# Q3. Why does `global` not work for a name defined in an enclosing function?

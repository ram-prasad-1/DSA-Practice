# 03. Decorators — a callable that takes a function and returns a replacement
# Run: python 03_decorators_basics.py



# @deco is just syntax for fn = deco(fn)
def make_pretty(func):
    def wrapper():
        print("<pretty>")
        func()

    return wrapper


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()



# the equivalent longhand
def plain():
    print("I am plain")


plain = make_pretty(plain)
plain()



# deco(fn) runs once at def time; only the wrapper runs per call
def noisy(func):
    print("decorating", func.__name__)

    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@noisy
def work():
    return 1


print("--- def time is over ---")
work()
work()



# functools.wraps keeps __name__, __doc__ and introspectability
import functools


def check_positive(func):
    @functools.wraps(func)
    def wrapper(x, y):
        if x < 0 or y < 0:
            raise ValueError(f"both x and y must be positive for {func.__name__}")
        return func(x, y)

    return wrapper


@check_positive
def add(x, y):
    """Add two positive numbers."""
    return x + y


print(add(2, 3), add.__name__, add.__doc__)
try:
    add(-1, 3)
except ValueError as e:
    print("ValueError:", e)



# without wraps the metadata is lost
def bare(func):
    def wrapper(*a, **kw):
        return func(*a, **kw)

    return wrapper


@bare
def named():
    pass


print(named.__name__)



# decorators stack: the one closest to the def is applied first
def upper(func):
    return lambda: func().upper()


def exclaim(func):
    return lambda: func() + "!"


@exclaim
@upper
def greet():
    return "hi"


print(greet())



# Practice
# Q1. Write a @timed decorator that prints how long the call took.
# Q2. Swap @exclaim and @upper above — does the output change? Why not?
# Q3. Use functools.wraps and check __wrapped__ to reach the undecorated function.

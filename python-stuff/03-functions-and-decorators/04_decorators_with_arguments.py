# 04. Decorators with arguments — one extra enclosing function
# Run: python 04_decorators_with_arguments.py



# @deco(args) resolves to deco(args)(fn)(fn_args) — three layers
import functools


def check_above(threshold):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(x, y):
            if x < threshold or y < threshold:
                raise ValueError(
                    f"both x and y must be larger than {threshold} for {func.__name__}"
                )
            return func(x, y)

        return wrapper

    return decorator


@check_above(10)
def add(x, y):
    return x + y


print(add(20, 30))
try:
    add(1, 30)
except ValueError as e:
    print("ValueError:", e)



# a repeat decorator: the factory closes over its own arguments
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]

        return wrapper

    return decorator


@repeat(3)
def roll():
    return "x"


print(roll())



# optional arguments: detect whether the first argument is the function itself
def task(func=None, *, retries=1):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"{fn.__name__} with retries={retries}")
            return fn(*args, **kwargs)

        return wrapper

    return decorator(func) if callable(func) else decorator


@task
def a():
    return "a"


@task(retries=3)
def b():
    return "b"


print(a(), b())



# stdlib decorator factories worth knowing
from functools import lru_cache, cache


@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


print(fib(30), fib.cache_info())


@cache
def slow_square(n):
    return n * n


print(slow_square(9))



# Practice
# Q1. Write @retry(times=3) that swallows exceptions and retries the call.
# Q2. Explain why `@task` and `@task()` both need to work, and what breaks if callable() is dropped.
# Q3. Compare functools.cache and lru_cache(maxsize=None) — what is the difference?

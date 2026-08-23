# 01. *args and **kwargs — collecting extra positional and keyword arguments
# Run: python 01_args_and_kwargs.py



# *args is a tuple, **kwargs is a dict; the names are convention, the * does the work
def f(*args, **kwargs):
    print(args, kwargs)


f(1, 2, x=3)
f()



# they come after the named parameters
def tag(name, *children, sep="", **attrs):
    print(name, children, sep, attrs)


tag("div", "a", "b", sep="|", cls="row")



# a bare * marks every following parameter keyword-only
def connect(host, *, port=5432, timeout=None):
    print(host, port, timeout)


connect("localhost", port=6379)
try:
    connect("localhost", 6379)
except TypeError as e:
    print("TypeError:", e)



# a leading / marks every preceding parameter positional-only (3.8+)
def divide(a, b, /):
    return a / b


print(divide(6, 3))
try:
    divide(a=6, b=3)
except TypeError as e:
    print("TypeError:", e)



# forwarding: the standard wrapper signature
def logged(func):
    def wrapper(*args, **kwargs):
        print("calling", func.__name__)
        return func(*args, **kwargs)

    return wrapper


print(logged(divide)(10, 4))



# Practice
# Q1. Write sum_all(*nums) that also accepts a start= keyword-only argument.
# Q2. What happens to duplicate keys when you call f(**a, **b) with overlapping dicts?
# Q3. Why does def f(*args, x): ... force x to be passed by keyword?

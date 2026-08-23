# 01. Exceptions — surfacing details when handling errors
# Run: python 01_exceptions.py



a, b = 1, 0



# e alone gives only the message; type(e).__name__ gives the class name
try:
    c = a / b
except Exception as e:
    print(e)
    print(f"{type(e).__name__}: {e}")



# catch the specific exception you expect, not bare Exception
try:
    c = a / b
except ZeroDivisionError:
    print("caught ZeroDivisionError")
except (TypeError, ValueError):
    print("not reached")



# full traceback
import traceback

try:
    c = a / b
except Exception as e:
    traceback.print_exception(e)



# inside an except block, print_exc() takes no exception argument
try:
    c = a / b
except Exception:
    traceback.print_exc()
    print("format_exc() returns the same text as a string:", len(traceback.format_exc()))



# logging.exception attaches the traceback at ERROR level
import logging

try:
    c = a / b
except Exception:
    logging.exception("Exception occurred")



# raise from preserves the cause; a bare raise re-raises the current exception
def load(value):
    try:
        return int(value)
    except ValueError as e:
        raise RuntimeError(f"bad config value {value!r}") from e


try:
    load("x")
except RuntimeError as e:
    print(type(e).__name__, "caused by", type(e.__cause__).__name__)



# else runs when no exception was raised; finally always runs
try:
    result = 10 / 2
except ZeroDivisionError:
    print("no")
else:
    print("else:", result)
finally:
    print("finally always runs")



# custom exceptions: subclass Exception, keep the hierarchy shallow
class ConfigError(Exception):
    pass


try:
    raise ConfigError("missing key", "database")
except ConfigError as e:
    print(type(e).__name__, e.args)



# Practice
# Q1. Why is `except Exception: pass` almost always wrong?
# Q2. Show the difference in output between `raise X from e` and a plain `raise X`.
# Q3. What does a `finally` block do to a `return` value in the same try statement?

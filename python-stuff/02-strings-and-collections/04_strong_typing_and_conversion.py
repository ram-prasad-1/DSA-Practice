# 04. Strong typing — Python is dynamically AND strongly typed
# Run: python 04_strong_typing_and_conversion.py



# no silent coercion across kinds
try:
    "Python" + 101
except TypeError as e:
    print("TypeError:", e)



# convert explicitly instead
print("Python" + str(101))
print(f"Python{101}")



# strong typing (no cross-type coercion) is independent of dynamic typing
# (types are checked at runtime, and a name can be rebound to any type)
val = 5
val = "now a string"
print(type(val))



# numeric types do interoperate — they are one numeric tower
print(1 + 2.5, True + 1, 3 / 2, 3 // 2, 3 % 2)



# * with a sequence and an int is repetition, not arithmetic
print("ab" * 3, [0] * 3)



# comparisons across unordered types also refuse
try:
    1 < "2"
except TypeError as e:
    print("TypeError:", e)



# int() parsing is strict; float handles more forms
print(int("42"), float("1e3"))
try:
    int("42.0")
except ValueError as e:
    print("ValueError:", e)



# Practice
# Q1. Convert the list ["1", "2", "3"] to ints two ways (map and comprehension).
# Q2. Why does `[1] + (2,)` fail while `[1] + [2]` works?
# Q3. Find a case where int(x) loses information but float(x) does not.

# 04. Comparisons — is for identity, == for value, truthiness for neither
# Run: python 04_comparisons_is_vs_equals.py



# PEP 8: compare to singletons with is / is not
# singletons: None, True, False, NotImplemented, Ellipsis
value = None
print(value is None, value is not None)



# == compares values, is compares identity — equal is not the same as identical
a = [1, 2]
b = [1, 2]
print(a == b, a is b)


# PEP 8 still prefers truthiness for booleans: `if flag:` over `if flag is True:`
flag = True
if flag:
    print("idiomatic")



# Practice
# Q1. Which falsy values would a `if not count:` guard wrongly reject for count=0?
# Q2. Write a function that distinguishes "argument omitted" from "argument was None".
# Q3. Why does `1 == True` return True, but `1 is True` return False?

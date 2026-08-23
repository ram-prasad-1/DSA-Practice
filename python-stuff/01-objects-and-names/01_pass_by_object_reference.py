# 01. Pass by object reference — neither pass-by-value nor pass-by-reference
# Run: python 01_pass_by_object_reference.py



# names are bound to objects; assignment rebinds a name, it never copies
a = [1, 2, 3]
b = a
print(a is b, id(a) == id(b))



# calling a function binds the caller's objects to the parameter names,
# so mutating a shared object is visible to the caller
def mutate(lst):
    lst.append(4)


nums = [1, 2, 3]
mutate(nums)
print(nums)



# rebinding the parameter only touches the local name
def rebind(lst):
    lst = [9, 9]


nums = [1, 2, 3]
rebind(nums)
print(nums)



# immutables can never be changed through a parameter — any "change" is a rebind
def bump(n):
    n += 1
    return n


count = 10
print(bump(count), count)



# += blurs the line: in-place extend for lists, rebind for immutables
lst = [1, 2]
before = lst
lst += [3]
print(lst is before)

tup = (1, 2)
before = tup
tup += (3,)
print(tup is before)



# Practice
# Q1. Write a function that empties a caller's list in place (two ways: clear() and [:] = []).
# Q2. Predict, then run: does `d = {}; f(d)` see changes if f does `d["k"] = 1`? What about `d = {"k": 1}`?
# Q3. Why does `s += "x"` inside a function never affect the caller's string?

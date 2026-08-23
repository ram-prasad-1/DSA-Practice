# 03. Multiple assignment — "tuple unpacking" works with any iterable
# Run: python 03_multiple_assignment.py



# basics: pack on the right, unpack on the left
point = 10, 20, 30
x, y, z = point
print(x, y, z)

x, y = 10, 20
y, x = x, y
print(x, y)



# any iterable unpacks, not just tuples
a, b, c = range(3)
p, q = "hi"
print(a, b, c, p, q)



# loops unpack each item
person = {"name": "ram", "city": "pune"}
for k, v in person.items():
    print(k, v)

for color, ratio in zip(["red", "blue"], [0.6, 0.4]):
    print(f"It's {ratio * 100}% {color}.")



# star unpacking (PEP 3132): one starred name absorbs the rest as a list
numbers = [1, 2, 3, 4, 5, 6]
first, *rest = numbers
head, *middle, tail = numbers
print(first, rest)
print(head, middle, tail)



# shallow vs deep: nesting in the target mirrors nesting in the value
color, pt = ("red", (1, 2, 3))
color, (i, j, k) = ("red", (1, 2, 3))
print(pt, i, j, k)

items = [1, 2, 3, 4, 2, 1]
for idx, (front, back) in enumerate(zip(items, reversed(items))):
    print(idx, front, back)



# gotchas: counts must match, and a single-element target needs a trailing comma
try:
    m, n = (1, 2, 3)
except ValueError as e:
    print("ValueError:", e)

(only,) = [42]
print(only)



# Practice
# Q1. Swap three variables in one statement so a->b, b->c, c->a.
# Q2. Split [1,2,3,4,5] into first, last, and everything between, in one assignment.
# Q3. Predict: `a, b = b, a = 1, 2` — what do a and b end up as, and why?

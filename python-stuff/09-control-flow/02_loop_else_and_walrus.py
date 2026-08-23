# 02. for/else, while/else and the walrus operator
# Run: python 02_loop_else_and_walrus.py



# for/else: the else block runs only if the loop was NOT broken out of
def find(items, target):
    for item in items:
        if item == target:
            print(f"  found {target}")
            break
    else:
        print(f"  {target} is not here")


find([1, 2, 3], 2)
find([1, 2, 3], 9)



# read it as "for ... else no-break" — it replaces a found = False flag
items, target = [1, 2, 3], 9
found = False
for item in items:
    if item == target:
        found = True
        break
if not found:
    print("flag version needed an extra variable")



# the classic use: nested search for a prime / a divisor
for n in range(2, 10):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        print(n, "is prime")



# an empty loop body still runs else (there was no break)
for x in []:
    pass
else:
    print("else runs even for an empty iterable")



# while/else works the same way
attempts = 3
while attempts:
    attempts -= 1
else:
    print("while/else: ran to exhaustion, never broke")

attempts = 3
while attempts:
    break
else:
    print("not printed")



# try/else is the same idea for exceptions (see 06-errors-logging-debugging)



# the walrus := assigns inside an expression
values = [1, 2, 3, 4, 5]
if (count := len(values)) > 3:
    print(f"{count} values is a lot")



# it shines in while loops that would otherwise duplicate the read
import io

stream = io.StringIO("a\nb\n\nc\n")
while (line := stream.readline()):
    print("  line:", line.strip() or "<blank>")



# and in comprehensions, to compute a value once and both filter and use it
words = ["alpha", "be", "gamma", "hi"]
print([length for w in words if (length := len(w)) > 3])
print([(w, n) for w in words if (n := len(w)) > 3])



# it avoids calling an expensive function twice
def expensive(n):
    print("  computing", n)
    return n * 2


print([doubled for n in (1, 2) if (doubled := expensive(n)) > 2])



# parentheses are required in most statement positions
try:
    eval("x := 5")
except SyntaxError:
    print("SyntaxError: bare walrus in an expression statement")
print((y := 5), y)



# do NOT use it where a plain assignment reads better
n = len(values)
print(n)



# Practice
# Q1. Rewrite find() to return the index, using for/else.
# Q2. Use the walrus to read a file in fixed-size chunks until it is exhausted.
# Q3. Why does for/else confuse people, and when would you prefer a helper function?

# 06. Small idioms worth keeping at hand
# Run: python 06_small_idioms.py



# membership instead of a chained or
t = 14
if t == 6 or t == 14:
    print("chained or")
if t in (6, 14):
    print("membership")



# enumerate gives the index
stooges = ["Larry", "Moe", "Curly"]
for index, element in enumerate(stooges):
    print(f"{index} {element}")

for index, element in enumerate(stooges, start=1):
    print(f"{index}. {element}")



# unpack a range
a, b, c = range(3)
print(a, b, c)



# any / all instead of a manual loop-and-flag
nums = [2, 4, 6]
print(all(n % 2 == 0 for n in nums), any(n > 5 for n in nums))



# a sentinel object for "missing" when None is a legitimate value
MISSING = object()


def values_of(d: dict) -> dict:
    return {k: v for k, v in d.items() if v is not MISSING}


print(values_of({"a": 1, "b": None, "c": MISSING}))



# compare sentinels with is / is not — identity is the whole point
print(MISSING is not None, MISSING == object())



# run a shell command from a script
import subprocess


def show_version():
    return subprocess.run(
        ["python3", "--version"], check=True, capture_output=True, text=True
    ).stdout.strip()


print(show_version())



# prefer a list of args without shell=True when the command is fixed;
# shell=True is only for shell features (pipes, globs) and needs trusted input
print(subprocess.run("echo piped | tr a-z A-Z", shell=True, capture_output=True, text=True).stdout.strip())



# str.join over manual concatenation, and str methods over slicing tricks
print(", ".join(stooges))
print("prefix_name".removeprefix("prefix_"), "a-b-c".rsplit("-", 1))



# zip two lists into a dict
print(dict(zip("abc", range(3))))



# the main guard: code that should only run when the file is executed directly
if __name__ == "__main__":
    print("running as a script:", __name__)



# Practice
# Q1. Rewrite a for-loop-with-flag as a single any()/all() call.
# Q2. Why does capture_output=True need text=True to get str instead of bytes?
# Q3. Use a sentinel to distinguish "no default given" in a get_or(d, key, default) helper.

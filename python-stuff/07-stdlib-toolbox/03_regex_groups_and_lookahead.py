# 03. Regex grouping and lookaheads
# Run: python 03_regex_groups_and_lookahead.py



import re



# (...) creates a group; group numbers count opening parens left to right
m = re.match(r"(a(b)c)d", "abcd")
print(m.group(0), m.group(1), m.group(2))
print(m.group(2, 1, 2), m.groups())



# repeat a group with * + ? {m,n}
print(re.findall(r"(?:ab)+", "ababab ab"))
print(re.match(r"(ab)*", "ababab").group())



# named groups are far more readable
m = re.match(r"(?P<user>\w+)@(?P<host>[\w.]+)", "ram@example.com")
print(m.group("user"), m["host"], m.groupdict())



# non-capturing groups (?:...) keep the grouping without a number
print(re.match(r"(?:ab)(c)", "abc").groups())



# findall returns the groups, not the whole match, when groups are present
print(re.findall(r"(\w+)@(\w+)", "a@b c@d"))
print([m.group() for m in re.finditer(r"(\w+)@(\w+)", "a@b c@d")])



# backreferences: \1 in the pattern, \1 or \g<name> in the replacement
print(re.findall(r"\b(\w+) \1\b", "the the cat sat sat"))
print(re.sub(r"(?P<a>\w+) (?P<b>\w+)", r"\g<b> \g<a>", "hello world"))



# lookaheads are ZERO-WIDTH: they test what follows without consuming it
print(re.findall(r"\w+(?=,)", "a, b, c"))
print(re.findall(r"\b\w+\b(?!,)", "a, b, c"))
print(re.sub(r"(?=\d)", "#", "a1b2"))



# a classic use: filenames not ending in .bat
names = ["a.txt", "b.bat", "c.batch"]
print([n for n in names if re.fullmatch(r".*[.](?!bat$)[^.]*$", n)])



# lookbehinds must be fixed width
print(re.findall(r"(?<=INR )\d+", "INR 500 and USD 20"))
try:
    re.compile(r"(?<=a+)b")
except re.error as e:
    print("re.error:", e)



# snippet: highlight matches in terminal output
YELLOW, RESET = "\033[43m\033[1m", "\033[0m"


def highlight_regex_matches(pattern, text):
    return pattern.sub(lambda m: f"{YELLOW}{m.group()}{RESET}", text)


print(highlight_regex_matches(re.compile(r"\d+"), "order 12 shipped on 2026-08-23"))



# Practice
# Q1. Parse "2026-08-23" into named year/month/day groups.
# Q2. Why does findall with two groups return tuples? How do you get whole matches instead?
# Q3. Use a lookahead to find words followed by "px" without capturing "px".

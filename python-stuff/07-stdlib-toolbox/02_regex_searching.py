# 02. Regular expressions — patterns, repetition, and the search functions
# Run: python 02_regex_searching.py



import re



# most characters match themselves; ALWAYS use raw strings for patterns
print(re.search(r"\bword\b", "a word here"))
print("\\b" == r"\b", len("\b"), len(r"\b"))



# metacharacters: . ^ $ * + ? \ | ( ) { } [ ]
# they are not active inside [...] — elsewhere escape them
print(re.findall(r"[+.*]", "a+b.c*d"))
print(re.findall(r"\+", "a+b"), re.findall(r"[+]", "a+b"))



# A|B alternates whole branches, not single characters
print(re.findall(r"Crow|Servo", "Crow and Servo"))



# character classes and anchors
print(re.findall(r"\d+", "a1 bb22 c333"))
print(re.findall(r"^\w+", "first second"))
print(re.findall(r"\w+$", "first second"))



# repetition: ? (0 or 1)  * (0+)  + (1+)  {m,n}
print(re.findall(r"ab?", "a ab"))
print(re.findall(r"\d{2,3}", "1 22 333 4444"))



# repetition is GREEDY by default; append ? for non-greedy
html = "<a><b>"
print(re.findall(r"<.*>", html), re.findall(r"<.*?>", html))



# the four search functions
text = "cat bat rat"
print(re.match(r"cat", text))
print(re.match(r"bat", text))
print(re.search(r"bat", text))
print(re.findall(r"\wat", text))
print([m.span() for m in re.finditer(r"\wat", text)])



# match/search return a match object or None — always check
m = re.search(r"[a-z]+", "tempo")
if m:
    print(m.group(), m.span(), m.start(), m.end())



# compile explicitly when reusing a pattern in a loop
p = re.compile(r"[a-z]+", re.IGNORECASE)
print(p.search("TEMPO").group())



# flags work on both the module functions and compiled patterns
print(re.findall(r"^b", "a\nb", re.MULTILINE), re.findall(r"a.b", "a\nb", re.DOTALL))



# modifying strings: split, sub, subn
print(re.split(r"[\s,]+", "a, b  c,d"))
print(re.sub(r"\s+", "_", "a  b c"))
print(re.subn(r"a", "A", "banana"))



# sub with a function receives each match object
print(re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "1 and 20"))



# Practice
# Q1. Match an Indian mobile number: optional +91, then 10 digits starting 6-9.
# Q2. Why does re.match(r"bat", "cat bat") return None but re.search find it?
# Q3. Replace every double space with a single one without touching newlines.

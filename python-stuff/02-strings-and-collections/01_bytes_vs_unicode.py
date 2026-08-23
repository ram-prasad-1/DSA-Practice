# 01. Bytes vs unicode — str is text, bytes is raw binary, they never mix
# Run: python 01_bytes_vs_unicode.py



# the two types
text = "hello ✓"
data = b"hello"
print(type(text), type(data))



# conversion is always explicit
encoded = text.encode("utf-8")
print(encoded, len(text), len(encoded))
print(encoded.decode("utf-8"))



# mixing raises TypeError — no implicit coercion
try:
    "a" + b"b"
except TypeError as e:
    print("TypeError:", e)



# indexing bytes gives ints; slicing gives bytes
print(data[0], data[0:2])



# a wrong codec either mangles or raises
latin = "café".encode("latin-1")
print(latin)
try:
    latin.decode("utf-8")
except UnicodeDecodeError as e:
    print("UnicodeDecodeError:", e)
print(latin.decode("utf-8", errors="replace"))



# Python 2 had it backwards (str was bytes); the u'' prefix is a 3.x no-op
print(u"still just str" == "still just str")



# Practice
# Q1. Read a file as bytes and as text — which one needs an encoding argument?
# Q2. Predict len() for "🐍" as str and as utf-8 bytes.
# Q3. Round-trip "naïve" through latin-1 and through ascii — which fails and why?

# 02. String prefixes and f-strings — r, b, f and the format spec
# Run: python 02_string_prefixes_and_fstrings.py



# raw strings: backslash is literal, no escape sequences
print(len("\t"), len(r"\t"))
print(r"C:\new\table")



# prefixes combine: rb'' is a raw bytes literal
print(rb"\d+", type(rb"\d+"))



# f-strings (3.6+) are the standard way to format
tmp = 44
x = 11
print(f"The temperature is {tmp} Celsius")
print(f"square of {x} is {x * x}")



# the debug form (3.8+) prints the expression source too
print(f"{tmp=}")
print(f"{x * x = }")



# format specs: precision, width, alignment, thousands separators
value = 1234.5678
print(f"{value:.2f}")
print(f"{value:>12,.1f}")
print(f"{42:04d}  {255:#x}  {0.75:.0%}")



# conversions: !r for repr, !s for str
name = "ram"
print(f"{name!r} vs {name!s}")



# nested braces and expressions
width = 8
print(f"{name:>{width}}|")



# string.Template — safer substitution for user-supplied format strings
from string import Template

print(Template("Hi $name").substitute(name="Bob"))



# Practice
# Q1. Format 0.123456 as a percentage with one decimal place.
# Q2. Why is r'...' essential for regex patterns and Windows paths?
# Q3. Build a right-aligned two-column table from a list of (name, score) pairs.

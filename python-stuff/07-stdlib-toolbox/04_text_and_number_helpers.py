# 04. Text and number helpers — dedent, dedupe, gcd, randint
# Run: python 04_text_and_number_helpers.py



# textwrap.dedent strips the common leading whitespace from every line
import textwrap


def create_snippet():
    code = textwrap.dedent("""\
        int main(int argc, char* argv[]) {
            return 0;
        }
    """)
    return code


print(create_snippet())
print(textwrap.fill("a long sentence that will be wrapped at a narrow width", width=20))
print(textwrap.indent("one\ntwo", "> "))



# the backslash after the opening quotes avoids a leading blank line
print(repr(textwrap.dedent("""
    x
""")))



# deduplicate a list while preserving order (dicts keep insertion order, 3.7+)
array = ["b", "a", "b", "c", "a"]
print(list(dict.fromkeys(array)))
print(sorted(set(array)))



# the old array.index()-based one-liner is O(n squared) — avoid it
print([x for i, x in enumerate(array) if array.index(x) == i])



# random.randint is inclusive on BOTH ends, unlike almost everything else
import random

random.seed(0)
print(random.randint(1, 3), random.randrange(1, 3), random.choice("abc"))
print(sorted({random.randint(1, 3) for _ in range(50)}))
print(sorted({random.randrange(1, 3) for _ in range(50)}))



# math.gcd takes any number of arguments since 3.9; math.lcm too
import math

print(math.gcd(24, 108, 90))
numbers = [24, 108, 90]
print(math.gcd(*numbers), math.lcm(4, 6))



# rounding gotcha: round() uses banker's rounding
print(round(0.5), round(1.5), round(2.5))
from decimal import Decimal, ROUND_HALF_UP

print(Decimal("2.5").quantize(Decimal("1"), rounding=ROUND_HALF_UP))



# float arithmetic is binary — compare with math.isclose
print(0.1 + 0.2 == 0.3, math.isclose(0.1 + 0.2, 0.3))



# Practice
# Q1. Dedupe a list of dicts by one key while preserving order.
# Q2. Write inclusive_range(a, b) that behaves like randint's bounds.
# Q3. Why does sum([0.1] * 10) != 1.0, and what does math.fsum give?

# 08. Decimal and Fraction — when binary floats are the wrong tool
# Run: python 08_precise_numbers.py



# floats are binary, so most decimal fractions are not representable exactly
print(0.1 + 0.2, 0.1 + 0.2 == 0.3)
print(f"{0.1:.20f}")
print(sum([0.1] * 10) == 1.0)



import math

print(math.isclose(0.1 + 0.2, 0.3), math.fsum([0.1] * 10))



# Decimal is exact decimal arithmetic — the right tool for money
from decimal import Decimal, getcontext, ROUND_HALF_UP, ROUND_HALF_EVEN, localcontext

print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
print(Decimal("1.10") * 3)



# ALWAYS build a Decimal from a string (or int) — from a float inherits the error
print(Decimal(0.1))
print(Decimal("0.1"))



# quantize rounds to a fixed number of places, with an explicit rounding mode
price = Decimal("2.665")
cents = Decimal("0.01")
print(price.quantize(cents, rounding=ROUND_HALF_UP))
print(price.quantize(cents, rounding=ROUND_HALF_EVEN))
print(round(2.675, 2))



# round() on floats uses banker's rounding, which surprises people
print(round(0.5), round(1.5), round(2.5), round(3.5))
print([Decimal(str(n)).quantize(Decimal("1"), rounding=ROUND_HALF_UP) for n in (0.5, 1.5, 2.5)])



# precision is context-wide (28 significant digits by default)
print(getcontext().prec, Decimal(1) / Decimal(7))
with localcontext() as ctx:
    ctx.prec = 5
    print(Decimal(1) / Decimal(7))
print(Decimal(1) / Decimal(7))



# Decimal keeps significant trailing zeros — useful for reporting
print(Decimal("1.50"), Decimal("1.50") + Decimal("0.50"), Decimal("1.5") == Decimal("1.50"))
print(Decimal("1.500").normalize())



# Fraction is exact rational arithmetic
from fractions import Fraction

print(Fraction(1, 3) + Fraction(1, 6), Fraction("2/4"), Fraction(0.25))
print(Fraction(1, 3) * 3 == 1, 1 / 3 * 3 == 1)
print(Fraction(0.1).limit_denominator(100))



# converting out
f = Fraction(22, 7)
print(float(f), f.numerator, f.denominator, round(float(f), 4))



# choosing: float for measurement and science (fast, hardware-backed),
# Decimal for money and anything a human will audit,
# Fraction for exact ratios and symbolic-ish work
from decimal import InvalidOperation

try:
    Decimal("1") / Decimal("0")
except Exception as e:
    print(type(e).__name__)
print(1 / 3, float(Decimal(1) / Decimal(3)), float(Fraction(1, 3)))



# mixing Decimal with float is refused; with int it is fine
print(Decimal("1.5") + 1)
try:
    Decimal("1.5") + 1.5
except TypeError as e:
    print("TypeError:", e)



# Practice
# Q1. Total a cart of prices with Decimal and round to paise, half-up.
# Q2. Why is Decimal(0.1) != Decimal("0.1")?
# Q3. Show a case where float loses a rupee across 10,000 additions.

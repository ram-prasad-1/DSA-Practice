# 11. Sum of Two Integers — add without + or -
# Run: python 11_sum_of_two_integers.py
# Time: O(1), at most 32 iterations. Space: O(1).



# Python ints are arbitrary precision, so mask to 32 bits and sign-extend at the end
def getSum(a, b):
    MASK, INT_MAX = 0xFFFFFFFF, 0x7FFFFFFF
    a, b = a & MASK, b & MASK
    while b:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    return a if a <= INT_MAX else ~(a ^ MASK)



print(getSum(2, 3))
print(getSum(-2, 3))
print(getSum(-5, -7))

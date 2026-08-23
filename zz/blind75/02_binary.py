# 02. Binary — bit tricks, masking, and fixed-width iteration
# Run: python 02_binary.py



# 11. Sum of Two Integers — add without + or -
# Python ints are arbitrary precision, so mask to 32 bits and sign-extend at the end
# O(1) time (<= 32 iterations), O(1) space
def getSum(a, b):
    MASK, INT_MAX = 0xFFFFFFFF, 0x7FFFFFFF
    a, b = a & MASK, b & MASK
    while b:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    return a if a <= INT_MAX else ~(a ^ MASK)


print(getSum(2, 3), getSum(-2, 3), getSum(-5, -7))



# 12. Number of 1 Bits — n & (n - 1) clears the lowest set bit
# O(k) time for k set bits, O(1) space
def hammingWeight(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


print(hammingWeight(0b1011), hammingWeight(0xFFFFFFFF))



# 13. Counting Bits — bits[i] = bits[i >> 1] + (i & 1)
# O(n) time, O(n) space
def countBits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp


print(countBits(8))



# 14. Missing Number — Gauss sum minus actual sum
# O(n) time, O(1) space
def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


# XOR variant: no overflow concern in fixed-width languages
def missingNumberXor(nums):
    res = len(nums)
    for i, n in enumerate(nums):
        res ^= i ^ n
    return res


print(missingNumber([3, 0, 1]), missingNumberXor([9, 6, 4, 2, 3, 5, 7, 0, 1]))



# 15. Reverse Bits — shift out of n, shift into res
# O(1) time (fixed 32 iterations), O(1) space
def reverseBits(n):
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res


print(reverseBits(0b00000010100101000001111010011100))

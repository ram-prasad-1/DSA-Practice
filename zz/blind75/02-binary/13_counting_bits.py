# 13. Counting Bits — bits[i] = bits[i >> 1] + (i & 1)
# Run: python 13_counting_bits.py
# Time: O(n). Space: O(n) for the output.



def countBits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp



print(countBits(5))
print(countBits(8))

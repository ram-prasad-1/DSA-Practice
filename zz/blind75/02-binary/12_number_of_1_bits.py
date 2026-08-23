# 12. Number of 1 Bits — n & (n - 1) clears the lowest set bit
# Run: python 12_number_of_1_bits.py
# Time: O(k) for k set bits (<= 32). Space: O(1).



def hammingWeight(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count



print(hammingWeight(0b1011))
print(hammingWeight(0xFFFFFFFF))

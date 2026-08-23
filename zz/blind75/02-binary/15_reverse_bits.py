# 15. Reverse Bits — shift out of n, shift into res
# Run: python 15_reverse_bits.py
# Time: O(1), fixed 32 iterations. Space: O(1).



def reverseBits(n):
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res



print(reverseBits(0b00000010100101000001111010011100))
print(reverseBits(0b11111111111111111111111111111101))

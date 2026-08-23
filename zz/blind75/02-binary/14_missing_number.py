# 14. Missing Number — Gauss sum minus the actual sum
# Run: python 14_missing_number.py
# Time: O(n). Space: O(1).



def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)



# XOR variant — avoids any overflow concern in fixed-width languages
def missingNumberXor(nums):
    res = len(nums)
    for i, n in enumerate(nums):
        res ^= i ^ n
    return res



print(missingNumber([3, 0, 1]))
print(missingNumberXor([9, 6, 4, 2, 3, 5, 7, 0, 1]))

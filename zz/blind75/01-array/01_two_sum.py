# 01. Two Sum — indices of the two numbers that add to target
# Run: python 01_two_sum.py
# Time: O(n). Space: O(n).



def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []



print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 3], 6))

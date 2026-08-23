# 05. Maximum Subarray — Kadane's algorithm
# Run: python 05_maximum_subarray.py
# Time: O(n). Space: O(1).



def maxSubArray(nums):
    best = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
    return best



print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([-3, -1, -2]))

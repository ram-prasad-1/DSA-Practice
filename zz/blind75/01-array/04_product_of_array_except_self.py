# 04. Product of Array Except Self — no division, O(n) time
# Run: python 04_product_of_array_except_self.py
# Time: O(n) in two passes. Space: O(1) extra, output excluded.



def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res



print(productExceptSelf([1, 2, 3, 4]))
print(productExceptSelf([-1, 1, 0, -3, 3]))

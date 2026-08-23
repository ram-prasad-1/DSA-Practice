# 06. Maximum Product Subarray — track max and min, since a negative flips them
# Run: python 06_maximum_product_subarray.py
# Time: O(n). Space: O(1).



def maxProduct(nums):
    best = hi = lo = nums[0]
    for n in nums[1:]:
        cands = (n, hi * n, lo * n)
        hi, lo = max(cands), min(cands)
        best = max(best, hi)
    return best



print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 3, -4]))

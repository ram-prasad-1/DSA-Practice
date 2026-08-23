# 01. Array — hash maps, running extremes, two pointers, binary search on rotated input
# Run: python 01_array.py



# 1. Two Sum — indices of the two numbers adding to target
# O(n) time, O(n) space
def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []


print(twoSum([2, 7, 11, 15], 9))



# 2. Best Time to Buy and Sell Stock — one buy, one later sell
# O(n) time, O(1) space
def maxProfit(prices):
    best, low = 0, float('inf')
    for p in prices:
        low = min(low, p)
        best = max(best, p - low)
    return best


print(maxProfit([7, 1, 5, 3, 6, 4]))



# 3. Contains Duplicate
# O(n) time, O(n) space
def containsDuplicate(nums):
    return len(set(nums)) < len(nums)


print(containsDuplicate([1, 2, 3, 1]), containsDuplicate([1, 2, 3]))



# 4. Product of Array Except Self — no division
# O(n) time, O(1) extra space (output excluded)
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



# 5. Maximum Subarray — Kadane's algorithm
# O(n) time, O(1) space
def maxSubArray(nums):
    best = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
    return best


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



# 6. Maximum Product Subarray — track max and min, a negative flips them
# O(n) time, O(1) space
def maxProduct(nums):
    best = hi = lo = nums[0]
    for n in nums[1:]:
        cands = (n, hi * n, lo * n)
        hi, lo = max(cands), min(cands)
        best = max(best, hi)
    return best


print(maxProduct([2, 3, -2, 4]), maxProduct([-2, 3, -4]))



# 7. Find Minimum in Rotated Sorted Array
# O(log n) time, O(1) space
def findMin(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]


print(findMin([4, 5, 6, 7, 0, 1, 2]))



# 8. Search in Rotated Sorted Array
# O(log n) time, O(1) space
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0), search([4, 5, 6, 7, 0, 1, 2], 3))



# 9. 3Sum — sort, fix one element, two-pointer the rest
# O(n^2) time, O(log n) space for the sort
def threeSum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i and nums[i] == nums[i - 1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                hi -= 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))



# 10. Container With Most Water
# O(n) time, O(1) space
def maxArea(height):
    lo, hi, best = 0, len(height) - 1, 0
    while lo < hi:
        best = max(best, (hi - lo) * min(height[lo], height[hi]))
        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1
    return best


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

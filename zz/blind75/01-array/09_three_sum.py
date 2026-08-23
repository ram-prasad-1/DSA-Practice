# 09. 3Sum — sort, then fix one element and two-pointer the rest
# Run: python 09_three_sum.py
# Time: O(n^2). Space: O(log n) for the sort, output excluded.



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
print(threeSum([0, 0, 0, 0]))

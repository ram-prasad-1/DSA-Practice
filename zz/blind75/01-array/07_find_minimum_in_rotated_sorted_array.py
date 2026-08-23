# 07. Find Minimum in Rotated Sorted Array — binary search against the right end
# Run: python 07_find_minimum_in_rotated_sorted_array.py
# Time: O(log n). Space: O(1).



def findMin(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]



print(findMin([3, 4, 5, 1, 2]))
print(findMin([4, 5, 6, 7, 0, 1, 2]))

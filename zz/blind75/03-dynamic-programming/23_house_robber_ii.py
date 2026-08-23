# 23. House Robber II — houses in a circle, so first and last are adjacent
# Run: python 23_house_robber_ii.py
# Time: O(n). Space: O(n) for the slices, O(1) if index ranges are used instead.



def rob(nums):
    if len(nums) == 1:
        return nums[0]

    def line(arr):
        prev = cur = 0
        for n in arr:
            prev, cur = cur, max(cur, prev + n)
        return cur

    return max(line(nums[:-1]), line(nums[1:]))



print(rob([2, 3, 2]))
print(rob([1, 2, 3, 1]))

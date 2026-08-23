# 22. House Robber — no two adjacent houses
# Run: python 22_house_robber.py
# Time: O(n). Space: O(1).



def rob(nums):
    prev = cur = 0
    for n in nums:
        prev, cur = cur, max(cur, prev + n)
    return cur



print(rob([1, 2, 3, 1]))
print(rob([2, 7, 9, 3, 1]))

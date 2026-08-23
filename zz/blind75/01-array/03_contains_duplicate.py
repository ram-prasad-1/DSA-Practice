# 03. Contains Duplicate — does any value appear twice?
# Run: python 03_contains_duplicate.py
# Time: O(n). Space: O(n).



def containsDuplicate(nums):
    return len(set(nums)) < len(nums)



print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))

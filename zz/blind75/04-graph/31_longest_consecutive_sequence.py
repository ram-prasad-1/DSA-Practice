# 31. Longest Consecutive Sequence
# Run: python 31_longest_consecutive_sequence.py
# Time: O(n). Space: O(n).



# only start counting from a number with no predecessor, so total work stays linear
def longestConsecutive(nums):
    s = set(nums)
    best = 0
    for n in s:
        if n - 1 in s:
            continue
        length = 1
        while n + length in s:
            length += 1
        best = max(best, length)
    return best



print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

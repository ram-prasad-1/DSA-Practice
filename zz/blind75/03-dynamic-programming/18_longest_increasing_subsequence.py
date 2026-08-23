# 18. Longest Increasing Subsequence — patience sorting
# Run: python 18_longest_increasing_subsequence.py
# Time: O(n log n). Space: O(n).



from bisect import bisect_left



# tails[i] = smallest tail of an increasing subsequence of length i+1
def lengthOfLIS(nums):
    tails = []
    for n in nums:
        i = bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)



print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
print(lengthOfLIS([7, 7, 7, 7]))

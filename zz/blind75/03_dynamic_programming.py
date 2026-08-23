# 03. Dynamic Programming — rolling state, tabulation, and one greedy
# Run: python 03_dynamic_programming.py



from bisect import bisect_left
from math import comb



# 16. Climbing Stairs — Fibonacci in disguise
# O(n) time, O(1) space
def climbStairs(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


print(climbStairs(5))



# 17. Coin Change — fewest coins to make amount
# O(amount * len(coins)) time, O(amount) space
def coinChange(coins, amount):
    dp = [0] + [float('inf')] * amount
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return -1 if dp[amount] == float('inf') else dp[amount]


print(coinChange([1, 2, 5], 11), coinChange([2], 3))



# 18. Longest Increasing Subsequence — patience sorting
# tails[i] = smallest tail of an increasing subsequence of length i+1
# O(n log n) time, O(n) space
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



# 19. Longest Common Subsequence — rolling row over the shorter string
# O(m*n) time, O(min(m, n)) space
def longestCommonSubsequence(text1, text2):
    if len(text1) < len(text2):
        text1, text2 = text2, text1
    prev = [0] * (len(text2) + 1)
    for a in text1:
        cur = [0] * (len(text2) + 1)
        for j, b in enumerate(text2, 1):
            cur[j] = prev[j - 1] + 1 if a == b else max(prev[j], cur[j - 1])
        prev = cur
    return prev[-1]


print(longestCommonSubsequence("abcde", "ace"))



# 20. Word Break
# O(n^2 * L) time, O(n + dict) space
def wordBreak(s, wordDict):
    words = set(wordDict)
    n = len(s)
    dp = [True] + [False] * n
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]


print(wordBreak("leetcode", ["leet", "code"]), wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))



# 21. Combination Sum IV — counts permutations, so target is the outer loop
# O(target * len(nums)) time, O(target) space
def combinationSum4(nums, target):
    dp = [1] + [0] * target
    for t in range(1, target + 1):
        for n in nums:
            if n <= t:
                dp[t] += dp[t - n]
    return dp[target]


print(combinationSum4([1, 2, 3], 4))



# 22. House Robber
# O(n) time, O(1) space
def rob(nums):
    prev = cur = 0
    for n in nums:
        prev, cur = cur, max(cur, prev + n)
    return cur


print(rob([2, 7, 9, 3, 1]))



# 23. House Robber II — circle, so first and last are adjacent
# O(n) time, O(n) for the slices (O(1) with index ranges)
def robCircular(nums):
    if len(nums) == 1:
        return nums[0]

    def line(arr):
        prev = cur = 0
        for n in arr:
            prev, cur = cur, max(cur, prev + n)
        return cur

    return max(line(nums[:-1]), line(nums[1:]))


print(robCircular([2, 3, 2]), robCircular([1, 2, 3, 1]))



# 24. Decode Ways
# O(n) time, O(1) space
def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    prev, cur = 1, 1
    for i in range(1, len(s)):
        nxt = 0
        if s[i] != '0':
            nxt += cur
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            nxt += prev
        if nxt == 0:
            return 0
        prev, cur = cur, nxt
    return cur


print(numDecodings("226"), numDecodings("06"))



# 25. Unique Paths — combinatorics: choose which of the m+n-2 moves go down
# O(min(m, n)) time, O(1) space
def uniquePaths(m, n):
    return comb(m + n - 2, m - 1)


# DP alternative: O(m*n) time, O(n) space
def uniquePathsDp(m, n):
    row = [1] * n
    for _ in range(m - 1):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]


print(uniquePaths(3, 7), uniquePathsDp(3, 7))



# 26. Jump Game — greedy furthest reach
# O(n) time, O(1) space
def canJump(nums):
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + n)
    return True


print(canJump([2, 3, 1, 1, 4]), canJump([3, 2, 1, 0, 4]))

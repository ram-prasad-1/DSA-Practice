# 21. Combination Sum IV — counts permutations, so the target loop is outermost
# Run: python 21_combination_sum_iv.py
# Time: O(target * len(nums)). Space: O(target).



def combinationSum4(nums, target):
    dp = [1] + [0] * target
    for t in range(1, target + 1):
        for n in nums:
            if n <= t:
                dp[t] += dp[t - n]
    return dp[target]



print(combinationSum4([1, 2, 3], 4))
print(combinationSum4([9], 3))

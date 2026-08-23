# 20. Word Break — dp[i] = some split point j leaves a dictionary word in s[j:i]
# Run: python 20_word_break.py
# Time: O(n^2 * L) for average substring length L. Space: O(n + dictionary size).



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



print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

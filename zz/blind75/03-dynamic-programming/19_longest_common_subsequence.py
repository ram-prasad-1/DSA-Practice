# 19. Longest Common Subsequence — rolling row over the shorter string
# Run: python 19_longest_common_subsequence.py
# Time: O(m*n). Space: O(min(m, n)).



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
print(longestCommonSubsequence("abc", "def"))

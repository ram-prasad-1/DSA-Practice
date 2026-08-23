# 57. Longest Palindromic Substring — expand around each of the 2n-1 centers
# Run: python 57_longest_palindromic_substring.py
# Time: O(n^2). Space: O(1) extra. Manacher's gives O(n) but is rarely expected.



def longestPalindrome(s):
    best = ""
    for i in range(len(s)):
        for lo, hi in ((i, i), (i, i + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            if hi - lo - 1 > len(best):
                best = s[lo + 1:hi]
    return best



print(longestPalindrome("babad"))
print(longestPalindrome("cbbd"))

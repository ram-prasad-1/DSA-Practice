# 58. Palindromic Substrings — same centers as #57, counting instead of measuring
# Run: python 58_palindromic_substrings.py
# Time: O(n^2). Space: O(1).



def countSubstrings(s):
    total = 0
    for i in range(len(s)):
        for lo, hi in ((i, i), (i, i + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                total += 1
                lo -= 1
                hi += 1
    return total



print(countSubstrings("abc"))
print(countSubstrings("aaa"))

# 56. Valid Palindrome — skip non-alphanumerics from both ends
# Run: python 56_valid_palindrome.py
# Time: O(n). Space: O(1).



def isPalindrome(s):
    lo, hi = 0, len(s) - 1
    while lo < hi:
        while lo < hi and not s[lo].isalnum():
            lo += 1
        while lo < hi and not s[hi].isalnum():
            hi -= 1
        if s[lo].lower() != s[hi].lower():
            return False
        lo, hi = lo + 1, hi - 1
    return True



print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))

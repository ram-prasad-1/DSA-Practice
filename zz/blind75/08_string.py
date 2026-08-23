# 08. String — sliding windows, counters, palindromic centers, framing
# Run: python 08_string.py



from collections import Counter, defaultdict



# 50. Longest Substring Without Repeating Characters — jump the left edge past the repeat
# O(n) time, O(min(n, alphabet)) space
def lengthOfLongestSubstring(s):
    last = {}
    best = start = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        best = max(best, i - start + 1)
    return best


print(lengthOfLongestSubstring("abcabcbb"), lengthOfLongestSubstring("bbbbb"))



# 51. Longest Repeating Character Replacement
# the window never shrinks, so maxf need not be exact for the answer to be right
# O(n) time, O(1) space
def characterReplacement(s, k):
    count = Counter()
    left = maxf = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        maxf = max(maxf, count[ch])
        if right - left + 1 - maxf > k:
            count[s[left]] -= 1
            left += 1
    return len(s) - left


print(characterReplacement("ABAB", 2), characterReplacement("AABABBA", 1))



# 52. Minimum Window Substring — expand right, contract left while the window is valid
# O(n + m) time, O(m) space
def minWindow(s, t):
    if not s or not t:
        return ""
    need = Counter(t)
    missing = len(t)
    best_len, best_l = float('inf'), 0
    left = 0
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best_len:
                best_len, best_l = right - left + 1, left
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return "" if best_len == float('inf') else s[best_l:best_l + best_len]


print(minWindow("ADOBECODEBANC", "ABC"), repr(minWindow("a", "aa")))



# 53. Valid Anagram
# O(n) time, O(1) space
def isAnagram(s, t):
    return Counter(s) == Counter(t)


print(isAnagram("anagram", "nagaram"), isAnagram("rat", "car"))



# 54. Group Anagrams — a 26-slot count tuple beats sorting each word when words are long
# O(N*K) time, O(N*K) space
def groupAnagrams(strs):
    groups = defaultdict(list)
    for w in strs:
        key = [0] * 26
        for ch in w:
            key[ord(ch) - 97] += 1
        groups[tuple(key)].append(w)
    return list(groups.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))



# 55. Valid Parentheses
# O(n) time, O(n) space
def isValid(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


print(isValid("()[]{}"), isValid("(]"))



# 56. Valid Palindrome — skip non-alphanumerics from both ends
# O(n) time, O(1) space
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


print(isPalindrome("A man, a plan, a canal: Panama"), isPalindrome("race a car"))



# 57. Longest Palindromic Substring — expand around each of the 2n-1 centers
# O(n^2) time, O(1) extra space (Manacher's is O(n) but rarely expected)
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


print(longestPalindrome("babad"), longestPalindrome("cbbd"))



# 58. Palindromic Substrings — same centers, counting instead of measuring
# O(n^2) time, O(1) space
def countSubstrings(s):
    total = 0
    for i in range(len(s)):
        for lo, hi in ((i, i), (i, i + 1)):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                total += 1
                lo -= 1
                hi += 1
    return total


print(countSubstrings("abc"), countSubstrings("aaa"))



# 59. Encode and Decode Strings (premium)
# length-prefix framing survives any delimiter appearing in the payload
# O(N) time both ways, O(N) space
class Codec:
    def encode(self, strs):
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        res, i = [], 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            res.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return res


codec = Codec()
wire = codec.encode(["lint", "co#de", "love#4#you"])
print(wire, codec.decode(wire))

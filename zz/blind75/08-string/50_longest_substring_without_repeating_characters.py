# 50. Longest Substring Without Repeating Characters — jump the left edge past the repeat
# Run: python 50_longest_substring_without_repeating_characters.py
# Time: O(n). Space: O(min(n, alphabet)).



def lengthOfLongestSubstring(s):
    last = {}
    best = start = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        best = max(best, i - start + 1)
    return best



print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("pwwkew"))

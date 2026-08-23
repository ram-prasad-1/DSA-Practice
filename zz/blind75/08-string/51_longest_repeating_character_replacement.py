# 51. Longest Repeating Character Replacement — window of one letter plus k edits
# Run: python 51_longest_repeating_character_replacement.py
# Time: O(n). Space: O(alphabet) = O(1).



from collections import Counter



# the window never shrinks, so maxf need not be exact for the answer to be right
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



print(characterReplacement("ABAB", 2))
print(characterReplacement("AABABBA", 1))

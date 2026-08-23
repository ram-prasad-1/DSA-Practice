# 52. Minimum Window Substring — expand right, contract left while the window is valid
# Run: python 52_minimum_window_substring.py
# Time: O(n + m). Space: O(m) for the need map.



from collections import Counter



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



print(minWindow("ADOBECODEBANC", "ABC"))
print(repr(minWindow("a", "aa")))

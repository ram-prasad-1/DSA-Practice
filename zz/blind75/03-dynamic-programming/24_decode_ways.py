# 24. Decode Ways — count letter mappings for a digit string
# Run: python 24_decode_ways.py
# Time: O(n). Space: O(1).



def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    prev, cur = 1, 1
    for i in range(1, len(s)):
        nxt = 0
        if s[i] != '0':
            nxt += cur
        if 10 <= int(s[i - 1:i + 1]) <= 26:
            nxt += prev
        if nxt == 0:
            return 0
        prev, cur = cur, nxt
    return cur



print(numDecodings("226"))
print(numDecodings("06"))

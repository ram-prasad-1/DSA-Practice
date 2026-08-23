# 54. Group Anagrams — a 26-slot count tuple beats sorting each word when words are long
# Run: python 54_group_anagrams.py
# Time: O(N*K) for N words of average length K. Space: O(N*K).



from collections import defaultdict



def groupAnagrams(strs):
    groups = defaultdict(list)
    for w in strs:
        key = [0] * 26
        for ch in w:
            key[ord(ch) - 97] += 1
        groups[tuple(key)].append(w)
    return list(groups.values())



print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))

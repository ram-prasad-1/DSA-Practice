# 53. Valid Anagram
# Run: python 53_valid_anagram.py
# Time: O(n). Space: O(alphabet) = O(1).



from collections import Counter



def isAnagram(s, t):
    return Counter(s) == Counter(t)



print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))

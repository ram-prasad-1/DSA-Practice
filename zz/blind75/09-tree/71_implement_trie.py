# 71. Implement Trie (Prefix Tree) — nested dicts, '$' marks a complete word
# Run: python 71_implement_trie.py
# Time: O(L) per operation. Space: O(total characters inserted).



class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True

    def search(self, word):
        node = self._find(word)
        return node is not None and '$' in node

    def startsWith(self, prefix):
        return self._find(prefix) is not None

    def _find(self, s):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node



trie = Trie()
trie.insert("apple")
print(trie.search("apple"), trie.search("app"))
print(trie.startsWith("app"), trie.startsWith("bpp"))

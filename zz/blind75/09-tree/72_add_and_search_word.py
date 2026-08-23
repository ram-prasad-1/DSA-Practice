# 72. Add and Search Word (wildcard '.') — trie plus DFS when the pattern branches
# Run: python 72_add_and_search_word.py
# Time: O(L) to add; search O(L) with no wildcards, O(26^L) worst case with them.
# Space: O(total characters).



class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return '$' in node
            ch = word[i]
            if ch == '.':
                return any(dfs(child, i + 1)
                           for k, child in node.items() if k != '$')
            return ch in node and dfs(node[ch], i + 1)

        return dfs(self.root, 0)



wd = WordDictionary()
for w in ("bad", "dad", "mad"):
    wd.addWord(w)
print(wd.search("pad"), wd.search("bad"))
print(wd.search(".ad"), wd.search("b.."))

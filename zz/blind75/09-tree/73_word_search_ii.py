# 73. Word Search II — trie + DFS; pruning empty branches keeps the scan from degenerating
# Run: python 73_word_search_ii.py
# Time: O(m*n*3^(L-1)) for max word length L. Space: O(total characters in words).



def findWords(board, words):
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node['$'] = w

    m, n = len(board), len(board[0])
    res = []

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node:
            return
        nxt = node[ch]
        word = nxt.pop('$', None)
        if word:
            res.append(word)
        board[r][c] = '#'
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#':
                dfs(nr, nc, nxt)
        board[r][c] = ch
        if not nxt:
            node.pop(ch)

    for i in range(m):
        for j in range(n):
            dfs(i, j, root)
    return res



board = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
print(sorted(findWords(board, ["oath", "pea", "eat", "rain"])))
print(findWords([list("ab")], ["abc"]))

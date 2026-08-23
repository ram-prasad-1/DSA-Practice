# 49. Word Search — DFS with the current cell blanked out and restored on the way back
# Run: python 49_word_search.py
# Time: O(m*n*3^L) for word length L. Space: O(L) recursion depth.



def exist(board, word):
    m, n = len(board), len(board[0])

    def dfs(r, c, k):
        if k == len(word):
            return True
        if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[k]:
            return False
        board[r][c] = '#'
        found = (dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1)
                 or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1))
        board[r][c] = word[k]
        return found

    return any(dfs(i, j, 0) for i in range(m) for j in range(n))



board = [list("ABCE"), list("SFCS"), list("ADEE")]
print(exist(board, "ABCCED"))
print(exist(board, "ABCB"))

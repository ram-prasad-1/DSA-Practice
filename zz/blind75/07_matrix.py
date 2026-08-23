# 07. Matrix — in-place marking, boundary shrinking, and grid DFS
# Run: python 07_matrix.py



# 46. Set Matrix Zeroes — row 0 and column 0 hold the markers, so no extra space
# O(m*n) time, O(1) space
def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_col = any(matrix[i][0] == 0 for i in range(m))
    for i in range(m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if first_col:
            matrix[i][0] = 0


grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
setZeroes(grid)
print(grid)



# 47. Spiral Matrix
# O(m*n) time, O(1) extra space
def spiralOrder(matrix):
    if not matrix:
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    res = []
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            res.append(matrix[top][j])
        top += 1
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                res.append(matrix[bottom][j])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
    return res


print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))



# 48. Rotate Image — reverse rows, then transpose = 90 degrees clockwise
# O(n^2) time, O(1) space
def rotate(matrix):
    matrix.reverse()
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(square)
print(square)



# 49. Word Search — DFS with the visited cell blanked out and restored on the way back
# O(m*n*3^L) time, O(L) recursion depth
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
print(exist(board, "ABCCED"), exist(board, "ABCB"))

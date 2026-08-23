# 46. Set Matrix Zeroes — row 0 and column 0 hold the markers, so no extra space
# Run: python 46_set_matrix_zeroes.py
# Time: O(m*n). Space: O(1).



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

grid = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
setZeroes(grid)
print(grid)

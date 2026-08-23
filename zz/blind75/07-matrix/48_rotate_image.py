# 48. Rotate Image — reverse rows, then transpose = rotate 90 degrees clockwise
# Run: python 48_rotate_image.py
# Time: O(n^2). Space: O(1).



def rotate(matrix):
    matrix.reverse()
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



square = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(square)
print(square)

square = [[1, 2], [3, 4]]
rotate(square)
print(square)

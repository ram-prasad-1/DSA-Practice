# 30. Number of Islands — flood fill from each unvisited land cell
# Run: python 30_number_of_islands.py
# Time: O(m*n). Space: O(min(m, n)) typical, O(m*n) worst case for the stack.



def numIslands(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                stack = [(i, j)]
                grid[i][j] = '0'
                while stack:
                    r, c = stack.pop()
                    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'
                            stack.append((nr, nc))
    return count



print(numIslands([list("11110"), list("11010"), list("11000"), list("00000")]))
print(numIslands([list("11000"), list("11000"), list("00100"), list("00011")]))

# 29. Pacific Atlantic Water Flow — BFS inward from each ocean's border, then intersect
# Run: python 29_pacific_atlantic_water_flow.py
# Time: O(m*n). Space: O(m*n).



from collections import deque



def pacificAtlantic(heights):
    if not heights:
        return []
    m, n = len(heights), len(heights[0])

    def bfs(starts):
        q = deque(starts)
        seen = set(starts)
        while q:
            r, c = q.popleft()
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if (0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen
                        and heights[nr][nc] >= heights[r][c]):
                    seen.add((nr, nc))
                    q.append((nr, nc))
        return seen

    pac = bfs([(0, c) for c in range(n)] + [(r, 0) for r in range(m)])
    atl = bfs([(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)])
    return [list(cell) for cell in pac & atl]



grid = [[1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]]
print(sorted(pacificAtlantic(grid)))
print(pacificAtlantic([[1]]))

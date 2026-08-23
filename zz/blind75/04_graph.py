# 04. Graph — BFS/DFS on grids, topological sort, and union-find
# Run: python 04_graph.py



from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val, self.neighbors = val, neighbors or []



# 27. Clone Graph — map original node -> clone, then copy edges
# O(V + E) time, O(V) space
def cloneGraph(node):
    if not node:
        return None
    clones = {node: Node(node.val)}
    stack = [node]
    while stack:
        cur = stack.pop()
        for nei in cur.neighbors:
            if nei not in clones:
                clones[nei] = Node(nei.val)
                stack.append(nei)
            clones[cur].neighbors.append(clones[nei])
    return clones[node]


n1, n2 = Node(1), Node(2)
n1.neighbors, n2.neighbors = [n2], [n1]
copy = cloneGraph(n1)
print(copy.val, [n.val for n in copy.neighbors], copy is n1)



# 28. Course Schedule — cycle detection via Kahn's topological sort
# O(V + E) time, O(V + E) space
def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indeg = [0] * numCourses
    for a, b in prerequisites:
        graph[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(numCourses) if indeg[i] == 0)
    done = 0
    while q:
        c = q.popleft()
        done += 1
        for nxt in graph[c]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return done == numCourses


print(canFinish(2, [[1, 0]]), canFinish(2, [[1, 0], [0, 1]]))



# 29. Pacific Atlantic Water Flow — BFS inward from each ocean's border, then intersect
# O(m*n) time, O(m*n) space
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


print(sorted(pacificAtlantic([[1, 2, 2, 3, 5],
                              [3, 2, 3, 4, 4],
                              [2, 4, 5, 3, 1],
                              [6, 7, 1, 4, 5],
                              [5, 1, 1, 2, 4]])))



# 30. Number of Islands — flood fill each unvisited land cell
# O(m*n) time, O(m*n) worst-case stack
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


print(numIslands([list("11000"), list("11000"), list("00100"), list("00011")]))



# 31. Longest Consecutive Sequence
# only start counting from a number with no predecessor, so total work stays linear
# O(n) time, O(n) space
def longestConsecutive(nums):
    s = set(nums)
    best = 0
    for n in s:
        if n - 1 in s:
            continue
        length = 1
        while n + length in s:
            length += 1
        best = max(best, length)
    return best


print(longestConsecutive([100, 4, 200, 1, 3, 2]))



# 32. Alien Dictionary (premium) — topological sort over first differing characters
# O(C) time for C total characters, O(1) space (alphabet-bounded)
def alienOrder(words):
    graph = {c: set() for w in words for c in w}
    indeg = {c: 0 for c in graph}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in graph[x]:
                    graph[x].add(y)
                    indeg[y] += 1
                break
        else:
            if len(a) > len(b):
                return ""
    q = deque(c for c in indeg if indeg[c] == 0)
    out = []
    while q:
        c = q.popleft()
        out.append(c)
        for nxt in graph[c]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return "".join(out) if len(out) == len(indeg) else ""


print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), repr(alienOrder(["abc", "ab"])))



# 33. Graph Valid Tree (premium) — n-1 edges and no cycle
# O(n * alpha(n)) time, O(n) space
def validTree(n, edges):
    if len(edges) != n - 1:
        return False
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
    return True


print(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]),
      validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))



# 34. Number of Connected Components (premium) — union-find, one merge per new edge
# O((n + E) * alpha(n)) time, O(n) space
def countComponents(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    count = n
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            count -= 1
    return count


print(countComponents(5, [[0, 1], [1, 2], [3, 4]]))

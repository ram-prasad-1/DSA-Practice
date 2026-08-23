# 33. Graph Valid Tree (premium) — a tree on n nodes has exactly n-1 edges and no cycle
# Run: python 33_graph_valid_tree.py
# Time: O(n * alpha(n)) ~ O(n). Space: O(n).



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



print(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))

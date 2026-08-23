# 34. Number of Connected Components (premium) — union-find, one merge per joining edge
# Run: python 34_number_of_connected_components.py
# Time: O((n + E) * alpha(n)) ~ O(n + E). Space: O(n).



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
print(countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))

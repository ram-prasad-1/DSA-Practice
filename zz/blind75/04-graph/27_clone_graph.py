# 27. Clone Graph — map original node to clone, then copy the edges
# Run: python 27_clone_graph.py
# Time: O(V + E). Space: O(V).



class Node:
    def __init__(self, val=0, neighbors=None):
        self.val, self.neighbors = val, neighbors or []



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
print(copy.val, [n.val for n in copy.neighbors])
print(copy is n1, copy.neighbors[0] is n2)

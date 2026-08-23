# 61. Same Tree — structure and values must both match
# Run: python 61_same_tree.py
# Time: O(n). Space: O(h).



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right



def isSameTree(p, q):
    if not p or not q:
        return p is q
    return (p.val == q.val and isSameTree(p.left, q.left)
            and isSameTree(p.right, q.right))



print(isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)),
                 TreeNode(1, TreeNode(2), TreeNode(3))))
print(isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))))

# 64. Binary Tree Level Order Traversal — build each level from the previous one
# Run: python 64_binary_tree_level_order_traversal.py
# Time: O(n). Space: O(w) for the widest level.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right



def levelOrder(root):
    if not root:
        return []
    res, level = [], [root]
    while level:
        res.append([n.val for n in level])
        level = [c for n in level for c in (n.left, n.right) if c]
    return res



print(levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(levelOrder(None))

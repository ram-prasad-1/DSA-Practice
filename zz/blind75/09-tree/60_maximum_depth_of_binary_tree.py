# 60. Maximum Depth of Binary Tree
# Run: python 60_maximum_depth_of_binary_tree.py
# Time: O(n). Space: O(h) — O(log n) balanced, O(n) worst case.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right



def maxDepth(root):
    return 1 + max(maxDepth(root.left), maxDepth(root.right)) if root else 0



print(maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
print(maxDepth(None))

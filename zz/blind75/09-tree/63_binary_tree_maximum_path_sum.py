# 63. Binary Tree Maximum Path Sum
# Run: python 63_binary_tree_maximum_path_sum.py
# Time: O(n). Space: O(h).



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right



# gain returns the best downward path; best records the best path bending at this node
def maxPathSum(root):
    best = float('-inf')

    def gain(node):
        nonlocal best
        if not node:
            return 0
        l = max(gain(node.left), 0)
        r = max(gain(node.right), 0)
        best = max(best, node.val + l + r)
        return node.val + max(l, r)

    gain(root)
    return best



print(maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))))
print(maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

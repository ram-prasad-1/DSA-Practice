# 68. Validate Binary Search Tree — carry the open interval down, not just the parent
# Run: python 68_validate_binary_search_tree.py
# Time: O(n). Space: O(h).



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right



def isValidBST(root):
    def check(node, lo, hi):
        if not node:
            return True
        if not lo < node.val < hi:
            return False
        return check(node.left, lo, node.val) and check(node.right, node.val, hi)

    return check(root, float('-inf'), float('inf'))



print(isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))
print(isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))))

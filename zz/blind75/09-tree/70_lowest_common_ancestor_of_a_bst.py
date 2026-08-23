# 70. Lowest Common Ancestor of a BST — descend while both targets sit on one side
# Run: python 70_lowest_common_ancestor_of_a_bst.py
# Time: O(h). Space: O(1).



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right



def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val > q.val:
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        else:
            return root



two = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
eight = TreeNode(8, TreeNode(7), TreeNode(9))
root = TreeNode(6, two, eight)
print(lowestCommonAncestor(root, two, eight).val)
print(lowestCommonAncestor(root, two.right.left, two.right.right).val)

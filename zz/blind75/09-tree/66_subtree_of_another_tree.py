# 66. Subtree of Another Tree
# Run: python 66_subtree_of_another_tree.py
# Time: O(m*n). Space: O(h). Serializing both trees and running KMP gives O(m + n).



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def isSameTree(p, q):
    if not p or not q:
        return p is q
    return (p.val == q.val and isSameTree(p.left, q.left)
            and isSameTree(p.right, q.right))



def isSubtree(root, subRoot):
    if not root:
        return False
    return (isSameTree(root, subRoot)
            or isSubtree(root.left, subRoot)
            or isSubtree(root.right, subRoot))



tree = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
print(isSubtree(tree, TreeNode(4, TreeNode(1), TreeNode(2))))
print(isSubtree(tree, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0)))))

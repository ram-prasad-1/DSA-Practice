# 62. Invert Binary Tree — swap children on the way back up
# Run: python 62_invert_binary_tree.py
# Time: O(n). Space: O(h).



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def preorder(node):
    return [node.val] + preorder(node.left) + preorder(node.right) if node else []



def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root



tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9)))
print(preorder(tree))
print(preorder(invertTree(tree)))

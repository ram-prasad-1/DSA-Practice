# 67. Construct Binary Tree from Preorder and Inorder Traversal
# Run: python 67_construct_binary_tree_from_preorder_and_inorder.py
# Time: O(n). Space: O(n).



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def levels(root):
    res, level = [], [root] if root else []
    while level:
        res.append([n.val for n in level])
        level = [c for n in level for c in (n.left, n.right) if c]
    return res



def buildTree(preorder, inorder):
    idx = {v: i for i, v in enumerate(inorder)}
    pre = iter(preorder)

    def build(lo, hi):
        if lo > hi:
            return None
        val = next(pre)
        node = TreeNode(val)
        mid = idx[val]
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(inorder) - 1)



print(levels(buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
print(levels(buildTree([-1], [-1])))

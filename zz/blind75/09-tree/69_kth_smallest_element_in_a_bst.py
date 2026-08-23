# 69. Kth Smallest Element in a BST — iterative in-order stops as soon as the kth pops
# Run: python 69_kth_smallest_element_in_a_bst.py
# Time: O(h + k). Space: O(h).



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right



def kthSmallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right



bst = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print(kthSmallest(bst, 1))
print(kthSmallest(bst, 3))

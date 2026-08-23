# 65. Serialize and Deserialize Binary Tree — preorder with '#' for null
# Run: python 65_serialize_and_deserialize_binary_tree.py
# Time: O(n) each way. Space: O(n).



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right



class Codec:
    def serialize(self, root):
        out = []

        def dfs(node):
            if not node:
                out.append('#')
                return
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ','.join(out)

    def deserialize(self, data):
        vals = iter(data.split(','))

        def build():
            v = next(vals)
            if v == '#':
                return None
            node = TreeNode(int(v))
            node.left = build()
            node.right = build()
            return node

        return build()



codec = Codec()
wire = codec.serialize(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))))
print(wire)
print(codec.serialize(codec.deserialize(wire)) == wire)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def dfs(node):
            if node is None:
                return "#"

            return str(node.val) + "," + dfs(node.left) + "," + dfs(node.right)

        return dfs(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def dfs(value):
            val = next(value)

            if val == "#":
                return None

            node = TreeNode(int(val))
            node.left = dfs(value)
            node.right = dfs(value)

            return node
        

        values = iter(data.split(","))

        return dfs(values)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
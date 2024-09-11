# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first_anomaly = None
        self.second_anomaly = None
        self.prev_node = TreeNode(float("-inf"))

        def inorderTraversal(root):
            if not root:
                return
            inorderTraversal(root.left)

            if self.prev_node.val >= root.val:
                self.second_anomaly = root
                if not self.first_anomaly:
                    self.first_anomaly = self.prev_node
            
            self.prev_node = root
            inorderTraversal(root.right)

            return

        inorderTraversal(root)

        if self.first_anomaly and self.second_anomaly:
            self.first_anomaly.val, self.second_anomaly.val = self.second_anomaly.val, self.first_anomaly.val
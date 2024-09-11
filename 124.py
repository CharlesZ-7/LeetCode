# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")

        def maxGain(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_gain = max(maxGain(node.left), 0)
            right_gain = max(maxGain(node.right), 0)

            cur_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, cur_sum)

            return node.val + max(left_gain, right_gain)

        maxGain(root)

        return self.max_sum 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        max_width = 0

        while queue:
            length = len(queue)
            _, start_idx = queue[0]
            for _ in range(length):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * idx))
                if node.right:
                    queue.append((node.right, 2 * idx + 1))
                
            max_width = max(max_width, idx - start_idx + 1)
        
        return max_width
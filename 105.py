# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(val=root_val)

        root_index_inorder = inorder.index(root_val)

        left_inorder = inorder[:root_index_inorder]
        right_inorder = inorder[root_index_inorder + 1:]

        left_len = len(left_inorder)
        # right_len = len(right_inorder)

        left_preorder = preorder[1: left_len + 1]
        right_preorder = preorder[left_len + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, state):
            if not node:
                return False

            state += node.val

            if not node.left and not node.right:
                return state == targetSum

            return dfs(node.left, state) or dfs(node.right, state)

        return dfs(root, 0)
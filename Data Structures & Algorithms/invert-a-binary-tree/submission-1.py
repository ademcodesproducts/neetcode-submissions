class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None

            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)

            return root

        return dfs(root)
        
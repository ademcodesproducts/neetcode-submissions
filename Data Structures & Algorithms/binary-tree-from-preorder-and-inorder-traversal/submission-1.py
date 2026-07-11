# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map, self.preorder_idx = {}, 0

        for i, val in enumerate(inorder):
            index_map[val] = i
        
        def build(l, r):
            if l > r:
                return None

            root_val = preorder[self.preorder_idx]
            self.preorder_idx += 1

            at_index = index_map[root_val]
            root = TreeNode(root_val)

            root.left = build(l, at_index - 1)
            root.right = build(at_index + 1, r)

            return root

        return build(0, len(inorder) - 1)
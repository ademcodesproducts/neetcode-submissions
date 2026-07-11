# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder[0]

        for i in range(len(inorder)):
            if root_val == inorder[i]:
                at_index = i
        
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:at_index+1], inorder[:at_index])
        root.right = self.buildTree(preorder[at_index+1:], inorder[at_index+1:])

        return root
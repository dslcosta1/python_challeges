# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(inorder) == 0: return None
        root = None
        for i in range(len(preorder)):
            if preorder[i] in inorder:
                root = TreeNode(preorder[i])
                index = inorder.index(preorder[i])

                root.left = self.buildTree(preorder[i+1:], inorder[:index])
                root.right = self.buildTree(preorder[i+1:], inorder[index+1:])
                
                return root

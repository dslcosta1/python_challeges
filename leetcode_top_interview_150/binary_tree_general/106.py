# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    post = []

    def buildSubTree(self, inorder):

        if len(inorder) == 0 or len(self.post) == 0:
            return None
        
        v = self.post.pop()
        root = TreeNode(val=v)

        index_inorder = inorder.index(v)
        inorder_left = inorder[:index_inorder]
        inorder_right = inorder[index_inorder+1:]
        root.right = self.buildSubTree(inorder_right)
        root.left = self.buildSubTree(inorder_left)
        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.post = postorder.copy()
        return self.buildSubTree(inorder)

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def falttenSubTree(self, root):
        if root == None: return root
        if root.left == None and root.right == None:
            return root

        right = root.right
        tail_left = None
        tail_right = None
        if root.left != None:
            tail_left = self.falttenSubTree(root.left)
            root.right = root.left
            root.left = None
        
        if right != None:
            tail_right = self.falttenSubTree(right)
            if tail_left != None:
                tail_left.right = right

        if  tail_right != None:
            return tail_right

        if tail_left != None:
            return tail_left  

        return root


    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        tail_final = self.falttenSubTree(root)

        return root
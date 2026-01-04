# https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None:
            if q == None: return True
            else: return False
        elif q == None:
            return False

        
        if p.val != q.val: return False

        return (self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left))

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None: return True

        return self.isSameTree(root.left, root.right)
        
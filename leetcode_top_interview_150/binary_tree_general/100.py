#https://leetcode.com/problems/same-tree/description/?envType=study-plan-v2&envId=top-interview-150

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

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
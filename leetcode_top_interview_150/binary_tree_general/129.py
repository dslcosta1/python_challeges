# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    total_sum = 0

    def foundSums(self, root, val):
        if root.left == None and root.right == None:
            self.total_sum += val + root.val
            return
        
        if root.left != None:
            self.foundSums(root.left, (val + root.val) * 10)

        if root.right != None:
            self.foundSums(root.right, (val + root.val) * 10)

        return

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0
        self.foundSums(root, 0)
        return self.total_sum
        
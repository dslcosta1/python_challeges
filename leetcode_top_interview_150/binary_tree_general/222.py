# https://leetcode.com/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0

        left = root
        right = root

        hl = 0
        hr = 0

        while left != None:
            left = left.left
            if left != None:
                hl += 1
        
        while right != None:
            right = right.right
            if right != None:
                hr += 1

        if hl != 0 and hr != 0 and hl == hr:
            return 2**(hr+1)-1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
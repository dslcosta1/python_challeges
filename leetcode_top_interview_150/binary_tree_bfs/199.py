# https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        stack_old = [root]
        stack_new = []
        rights = []

        while len(stack_old) > 0:
            e = stack_old[0]
            stack_old = stack_old[1:]
            if e != None:
                if e.left != None: stack_new.append(e.left)
                if e.right != None: stack_new.append(e.right)

                if len(stack_old) == 0:
                    rights.append(e.val)
                    stack_old = stack_new
                    stack_new = [] 

        return rights
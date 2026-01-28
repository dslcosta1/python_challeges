# https://leetcode.com/problems/binary-tree-level-order-traversal/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        stack = []
        stack_child = []
        vals_stack_child = []
        final = []
        stack.append(root)

        while len(stack) > 0:
            node = stack.pop(0)
            vals_stack_child.append(node.val)

            if node.left != None:
                stack_child.append(node.left)
            
            if node.right != None:
                stack_child.append(node.right)
            
            if len(stack) <= 0:
                stack = stack_child
                stack_child = []
                final.append(vals_stack_child)
                vals_stack_child = []


        return final    
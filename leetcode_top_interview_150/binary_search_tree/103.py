# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        stack = []
        stack_child = []
        vals_stack_child = []
        final = []
        stack.append(root)

        flag_reverse = -1

        while len(stack) > 0:
            node = stack.pop()
            vals_stack_child.append(node.val)

            if flag_reverse == -1:
                if node.left != None:
                    stack_child.append(node.left)
                
                if node.right != None:
                    stack_child.append(node.right)
            else:
                if node.right != None:
                    stack_child.append(node.right)

                if node.left != None:
                    stack_child.append(node.left)
            
            if len(stack) <= 0:
                stack = stack_child
                stack_child = []
                final.append(vals_stack_child)
                vals_stack_child = []
                flag_reverse *= -1


        return final
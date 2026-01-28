# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/?envType=study-plan-v2&envId=top-interview-150

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ## BFS
        if root == None: return root
        stack = []

        child_stack = []
        right_node = None
        stack.append(root)

        while len(stack) > 0:
            node = stack.pop(0)
            node.next = right_node
            
            if node.right != None:
                child_stack.append(node.right)

            if node.left != None:
                child_stack.append(node.left)
            
            if len(stack) == 0:
                stack = child_stack
                right_node = None
                child_stack = []
            else:
                right_node = node
        
        return root


# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    path = {}
    lca = None

    def foundPath(self, root, p):
        if root == None:
            return False

        if root.val == p or self.foundPath(root.left, p) or self.foundPath(root.right, p):
            if self.lca == None and (root.val in self.path):
                self.lca = root
            else:
                self.path[root.val] = root
            return True
        
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.path = {}
        t = self.foundPath(root, p.val)
        s = self.foundPath(root, q.val)

        return self.lca
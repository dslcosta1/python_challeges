

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isValidSubTree(self, root, min_val, max_val):
        if root == None: return True
        eval_left = True
        eval_right = True

        if root.left != None:
            if root.left.val <= min_val:
                return False
            if root.left.val >= root.val:
                return False
            
            eval_left = self.isValidSubTree(root.left, min_val, root.val)
        
        if root.right != None:
            if root.right.val >= max_val:
                return False
            if root.right.val <= root.val:
                return False

            eval_right = self.isValidSubTree(root.right, root.val, max_val)

        if root.left != None:
            min_val = min(min_val, root.left.val)

        return eval_left and eval_right

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None: return True
        return self.isValidSubTree(root, -(2**31) -1, (2**31 + 1))
        
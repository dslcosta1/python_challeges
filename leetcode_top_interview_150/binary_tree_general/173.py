
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    order_list = []
    pointer = 0

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.order_list = []
        self.pointer = 0

        def flatList(root):
            if root == None:
                return

            if root.left != None:
                flatList(root.left)
            
            self.order_list.append(root.val)

            if root.right != None:
                flatList(root.right)
            
            return
        
        flatList(root)
 
    def next(self) -> int:
        # print(self.order_list)
        if self.pointer >= len(self.order_list):
            return -1
        val = self.order_list[self.pointer]

        self.pointer += 1

        return val

    def hasNext(self) -> bool:
        return not self.pointer >= len(self.order_list)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
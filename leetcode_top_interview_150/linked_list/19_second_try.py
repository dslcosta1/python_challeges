# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class Solution:
    def removeNth(self, ant, head, n):
        if head == None:
            return 0

        count = self.removeNth(head, head.next, n) + 1

        if count == n:                
            if head == None:
                ant.next = None
            ant.next = head.next

        return count


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        init_node = ListNode()
        init_node.val = 0
        init_node.next = head
        
        c = self.removeNth(init_node, head, n)
        return init_node.next 

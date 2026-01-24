# https://leetcode.com/problems/rotate-list/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def findNth(self, ant, head, k, size):
        if head == None:
            if k > size:
                k = k % size
            return 0, ant, k, None

        
        count_ant, last_node, k, init_node = self.findNth(head, head.next, k, size+1)
        count = count_ant + 1

        if count == k:
            ant.next = None
            init_node = head

        return count, last_node, k, init_node

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or  head.next == None or k == 0: return head
        dummy_node = ListNode()
        dummy_node.next = head


        _, last_node, k, init_node = self.findNth(dummy_node, head, k, 0)
        if k == 0: return dummy_node.next
        last_node.next = dummy_node.next
        return init_node
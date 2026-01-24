# https://leetcode.com/problems/partition-list/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def part(self, prev, curr, x):
        if curr == None:
            return
        
        self.part(curr, curr.next, x)
        if curr.val >= x:
          while curr.next != None and curr.next.val < x:
            next = curr.next
            prev.next = next
            aux = next.next
            next.next = curr
            curr.next = aux

            prev = next

        return
             

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        dummy.val = -1

        prev = dummy
        curr = head

        self.part(prev, curr, x)
        return dummy.next 

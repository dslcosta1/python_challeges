# https://leetcode.com/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, prev, head, right, val):
        if head == None or val == right:
            return prev, head

        next = head.next
        head.next = prev

        newhead, newtail = self.reverse(head, next, right, val + 1)        
        return newhead, newtail

    def parReverse(self, prev, head, left, right, val):
        if head == None: return

        if val == left-1:
            newhead, newtail = self.reverse(prev, head, right, val)
            prev.next = newhead
            head.next = newtail
            return
        
        
        return self.parReverse(head, head.next, left, right, val+1)
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        self.parReverse(dummy, head, left, right, 0)
        return dummy.next
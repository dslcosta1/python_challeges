# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:



    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        next = head
        count = 0
        while next:
            count += 1
            next = next.next
        
        mid = count // 2
        print(mid)
        if mid == 0:
            return True
            

        prev = head
        curr = head.next

        for _ in range(mid-1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        if count % 2 != 0:
            curr = curr.next
        
        while curr:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next

        return True
        
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Go over counting and retunr removing
class Solution:
    elements = {}

    def removeElement(self, ant, curr):
        if curr == None:
            return 
        
        v = curr.val

        if v in self.elements:
            self.elements[curr.val] += 1
        else:
            self.elements[curr.val] = 1
        
        self.removeElement(curr, curr.next)
        v = curr.val
        if self.elements[v] > 1:
            next = curr.next
            ant.next = next
  
        return 



    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.elements = {}
        dummy = ListNode()
        dummy.next = head
        self.removeElement(dummy, head)


        return dummy.next
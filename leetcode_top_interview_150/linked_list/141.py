# https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mov(self, head):
        return head.next

    def mov_fast(self, head):
        new_head = self.mov(head)

        if new_head == None: return new_head

        return self.mov(new_head)

    def check_cycle(self, head, head_fast):
        if head_fast == None: return False
        if head == None: return False
        if head == head_fast: return True

        return self.check_cycle(self.mov(head), self.mov_fast(head_fast))
        
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False

        return self.check_cycle(self.mov(head), self.mov_fast(head))

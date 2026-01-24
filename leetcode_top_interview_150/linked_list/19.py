# https://leetcode.com/problems/remove-nth-node-from-end-of-list/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        init_node = ListNode()
        init_node.val = 0
        init_node.next = head
        dic = {}
        next = head
        count = 1
        while next != None:
            dic[count] = next
            next = next.next
            count += 1

        
        point = count - n
        if point +1 not in dic:
            if point -1 not in dic:
                return None
            else:
                dic[point-1].next = None
        else:
            if point -1 in dic:
                dic[point-1].next = dic[point+1]
            else:
                return dic[point +1]

        return init_node.next 
            
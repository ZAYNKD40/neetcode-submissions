# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #empty case
        if not head:
            return None
        #start with a new none at the start
        prev, curr = None, head
        while curr: #trying tto get curr to the old none and prev is the new head
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt # true next
            
        
        return prev
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start with null, prev = null, curr = head , current point using .next to prev
        # while changing .next, dont want the number to be lost, so you store nxt
        # and just shift downward. end when current reach the old null and prev is the new head so return prev
        if not head:
            return None
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
        # go through the problem using solution step by step            
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #fast and slow pointer, fast go faster but start same as slow and the only 
        # reason they would meet is that there is a cycle within the linked list

        slow,fast = head, head

        while fast and fast.next:  #because fast is going 2 steps not 1
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

        
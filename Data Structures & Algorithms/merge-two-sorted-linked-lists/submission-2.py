# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while l1 and l2: #while not empty
            if l1.val < l2.val: #this if else loop is the main incrementer
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next #updating tail to keep forming the resulting linked list
        if l1: #after that while loop, either l1 or l2 remains, and just stick what ever left to the resulting linked list
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next

        
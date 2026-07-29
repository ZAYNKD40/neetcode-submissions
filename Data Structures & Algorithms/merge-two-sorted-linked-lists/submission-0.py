# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #have two list
        output = ListNode() #calling class ListNode and make this a node
        tail = output

        while l1 and l2:
            if l1.val< l2.val:
                tail.next = l1 #update output pointer
                l1 = l1.next #update l1 pointer
            else:
                tail.next = l2
                l2 = l2.next 
            tail = tail.next #updating tail pointer to next node
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return  output.next


        
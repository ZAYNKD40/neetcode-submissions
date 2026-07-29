# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers because need to know end of list to know where to slice
        # offset is n = 2
        dummy = ListNode(0,head) #listnode value 0 and pointing to the head of the list we have
        left = dummy
        right = head #need right = head + n
        while n>0 and right:
            right = right.next #shift right by 1
            n -=1
        while right: #go until right is end of list
            left = left.next #.next only go to the next node, that is all you can traverse while in a node, so left is storing that next to be used to go next again, can not go two spaces in a node. 
            right = right.next
        #delete, we are at the spot where the node next to the current left is the one that need delete or rewired
        left.next = left.next.next # we start at dummy so instead of starting at first node it is the node before so left.next is the one that needs to be removed
        return dummy.next #this is at the head of the list, the dummy node is dummy

        


        
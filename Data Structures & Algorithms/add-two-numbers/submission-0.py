# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #extract the number from each with a loop then add them together, x1,x10,x100 etc x10**i
        curr1, curr2 = l1,l2
        count1,count2 = 0,0
        number1,number2= 0,0
        while curr1:
            number1 += curr1.val * 10**count1
            curr1 = curr1.next
            count1 +=1
        while curr2:
            number2 += curr2.val * 10**count2
            curr2 = curr2.next
            count2 +=1
        n = number1 + number2
        dummy = ListNode()
        curr = dummy
        for d in str(n)[::-1]:
            curr.next = ListNode(int(d))
            curr = curr.next
        return dummy.next
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        headAns = ListNode(9999)
        cur = headAns

        cur1 = l1
        cur2 = l2

        carry = 0
        while cur1 and cur2:
            total = cur1.val + cur2.val + carry
            if total >= 10:
                carry = 1
                total = total - 10
            else: 
                carry = 0
            
            cur.next = ListNode(total)
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            total = cur1.val + carry
            if total >= 10:
                carry = 1
                total = total - 10
            else: 
                carry = 0

            cur.next = ListNode(total) #how to remove this node?
            
            cur = cur.next
            cur1 = cur1.next
        
        while cur2:
            total = cur2.val + carry
            if total >= 10:
                carry = 1
                total = total - 10
            else: 
                carry = 0

            cur.next = ListNode(total)
            
            cur = cur.next
            cur2 = cur2.next


        if carry == 1:
            cur.next = ListNode(1)
        
        return headAns.next
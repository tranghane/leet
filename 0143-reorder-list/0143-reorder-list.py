# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse l2
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            nextCur = cur.next
            cur.next = prev
            prev = cur
            cur = nextCur
        l2 = prev
        l1 = head
        
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            l2.next = l1_next
            l1, l2 = l1_next, l2_next

        
            

        
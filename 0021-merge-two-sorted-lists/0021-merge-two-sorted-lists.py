# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        ans = ListNode(99)
        curAns = ans

        while curr1:
            if curr2:
                if curr1.val < curr2.val:
                    curAns.next = curr1
                    curr1 = curr1.next
                    curAns = curAns.next
                else:
                    curAns.next = curr2
                    curr2 = curr2.next
                    curAns = curAns.next
            else:
                curAns.next = curr1
                curr1 = curr1.next
                curAns = curAns.next
        while curr2:
            if curr1:
                if curr1.val < curr2.val:
                    curAns.next = curr1
                    curr1 = curr1.next
                    curAns = curAns.next
                else:
                    curAns.next = curr2
                    curr2 = curr2.next
                    curAns = curAns.next
            else:
                curAns.next = curr2
                curr2 = curr2.next
                curAns = curAns.next
        
        return ans.next
                

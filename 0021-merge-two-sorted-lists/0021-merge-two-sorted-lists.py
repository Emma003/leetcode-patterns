# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1,p2 = list1, list2
        newHead = ListNode()
        tail = newHead


        while p1 and p2:
            if p1.val > p2.val:
                tail.next = p2
                p2 = p2.next
            else:
                tail.next = p1
                p1 = p1.next
            tail = tail.next

        if p1:
            tail.next = p1
        if p2:
            tail.next = p2

        return newHead.next

        
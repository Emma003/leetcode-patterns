# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head, prev):
    if not head.next:
        head.next = prev
        return head
    
    newHead = reverse(head.next, head)
    head.next = prev
    return newHead

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        return reverse(head, None)
    
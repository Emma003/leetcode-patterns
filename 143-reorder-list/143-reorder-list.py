# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    prv, curr, nxt = None, head, None
    while curr:
        nxt = curr.next
        curr.next = prv
        prv = curr
        curr = nxt
    return prv

        
    
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next== None:
            return
        
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = reverse(slow)
        
        p1 = head
        p2 = tail
        while p1 and p2:
            tmp = p1.next
            p1.next = p2 
            p1 = tmp
            
            tmp = p2.next
            p2.next = p1
            p2 = tmp
        
        if p1:
            p1.next = None
            
        
        
        
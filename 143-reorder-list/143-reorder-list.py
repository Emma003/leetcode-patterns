# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next\

def reverse(head):
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
    
        p1 = head
        p2 = reverse(slow)
        
        
        while p1 and p2:
            tmp1 = p1.next
            tmp2 = p2.next
            
            p1.next = p2
            p2.next = tmp1
            
            p1 = tmp1
            p2 = tmp2
            
        #break link btw end of first half and second
        if p1:
            p1.next = None
            
        
        
            
        
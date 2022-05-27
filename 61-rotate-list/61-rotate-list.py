# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k==0:
            return head
        
        tail = head
        
        # find length of linked list
        l = 1
        while tail.next:
            tail = tail.next
            l += 1
        
        
        # if k>l, wrap around
        k = k % l
        
        # if k == len, don't change anything
        if k == 0:
            return head
        
        # find pivot point
        pivot = head
        for i in range(l-k-1):
            pivot = pivot.next
        
        # connect
        new_head = pivot.next 
        tail.next = head
        pivot.next = None
        
        return new_head
        
            
            
            
        
        
            
        
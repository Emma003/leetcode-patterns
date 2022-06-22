# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        #if len(list) < 2
        if not head or not head.next: 
            return head
        
        
        # two pointers: one at the start of the list, the other one node before the start
        dummy = ListNode(-1, head)
        start = head
        left_bridge = dummy
        
        # positioning the start pointer (tail of the reverse linked list) right before the start of the sublist
        i = 0
        while start and i < left-1:
            start = start.next
            left_bridge = left_bridge.next
            i += 1
            
        
        
        # reversing sublist
        curr = start
        prv = nxt = None
        while curr and left <= right:
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt
            
            left += 1
                
        # reattaching the ends
        left_bridge.next.next = curr
        left_bridge.next = prv
        
        return dummy.next
    

        
        
        
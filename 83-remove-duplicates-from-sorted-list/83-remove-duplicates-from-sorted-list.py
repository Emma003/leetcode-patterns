# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        curr, nxt = head, head.next
        
        while nxt:
            if nxt.val != curr.val:
                curr.next = nxt
                curr = nxt
                
            nxt = nxt.next
            
        curr.next = None
        return head
            
        
# 1 1 1 1 

# 1

# 

# 1 2 3 4 4 4 
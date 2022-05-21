# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None:
#             return head
        
#         curr, nxt = head, head.next
        
#         while nxt:
#             if nxt.val != curr.val:
#                 curr.next = nxt
#                 curr = nxt
                
#             nxt = nxt.next
            
#         curr.next = None
#         return head

        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head
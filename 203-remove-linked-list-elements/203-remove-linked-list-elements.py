# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         if head == None:
#             return None
#         prv, nxt = head, head.next
        
#         # if its the first element
#         while prv.val == val:
#             prv.next = None
#             prv = nxt
#             nxt = nxt.next
#             if nxt == None or prv == None:
#                 return None
        
#         while prv and nxt:
#             while nxt and nxt.val == val:
#                 nxt = nxt.next
#                 prv.next = nxt
            
#             if nxt == None or prv == None:
#                 break
#             nxt = nxt.next
#             prv = prv.next

        
        dummy = ListNode(-1) #dummy sentinel node
        dummy.next = head #set its pointer to start of list, will return this
        prv, curr = dummy, head
        
        while curr:
            nxt = curr.next
            if curr.val == val:
                prv.next = nxt
            else:
                prv = curr
                
            curr = nxt

        
        return dummy.next
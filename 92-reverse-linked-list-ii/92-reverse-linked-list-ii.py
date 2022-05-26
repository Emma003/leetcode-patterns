# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], p: int, q: int) -> Optional[ListNode]:
        # three steps
            # place two pointers at p and p-1
            # reverse the sublist
            # connect the head and tail of the new sublist to the left and right                    #ends
            
        dummy = ListNode(-1,head)
        lprv, curr = dummy, head
        
        # place two pointers at p and p-1
        i = 0
        while i < (p-1) and curr != None:
            curr = curr.next
            lprv = lprv.next
            i+=1
        
        #reverse sublist
        prev = nxt = None
        j = p
        while curr and j < (q+1): # after this loop curr = next = q+1 and prv=q
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            j+=1
        
        #connect
        lprv.next.next = curr
        lprv.next = prev
        
        return dummy.next
        
            

        
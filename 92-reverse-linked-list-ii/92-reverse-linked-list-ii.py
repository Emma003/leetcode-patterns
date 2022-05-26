# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], p: int, q: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        front_end = dummy
        curr = head

        # get to the start of the sublist
        i = 1
        while i<p:
            curr = curr.next
            front_end = front_end.next
            i+=1

        # reverse the sublist
        j = p
        prv, nxt = None, None
        while curr and j<=q:
            nxt = curr.next
            curr.next = prv
            prv = curr
            curr = nxt
            j+=1

        # connect the start and end of the sublist
        front_end.next.next = nxt
        front_end.next = prv

        return dummy.next

        
            

        
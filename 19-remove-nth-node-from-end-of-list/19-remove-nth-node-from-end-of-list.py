# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#.         i
#  2 3 4 5 6 7 8 n = 3
#  1 3 4 n = 3
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        slow = fast = head
        while n>0:
            fast = fast.next
            n -= 1
            
            # if n is == lenght of Llist
            if fast == None:
                return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #edge cases
            #only one node
            #k == len(list)
        
        
        #dummy node
        dummy = ListNode()
        dummy.next = head
        
        
        slow, fast = dummy, head
        
        #give fast pointer head start
        i=0
        while fast and i<n:
            fast = fast.next
            i+=1
            
            
            
        #iterate until fast reaches last pointer
        while fast:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return dummy.next
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    curr, prv = head, None
    
    while curr:
        nxt = curr.next
        curr.next = prv
        prv = curr
        curr = nxt
        
    return prv
    
    
    
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True
        
        #find middle of list
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        #reverse second half
        tail = reverse(slow)
        
        
        #compare
        p1, p2 = head, tail
        
        while p1 and p2:
            if p1.val != p2.val:
                break
            p1 = p1.next
            p2 = p2.next
            
            
        #undo reverse
        reverse(tail)
        if p1 == None or p2 == None:
            return True
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #find cycle
        slow, fast = head, head
        isCycle = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                isCycle = True
                break
            
        if not isCycle:
            return None
        
        #find length of cycle
        counter = 0
        pLen = slow
        
        while True:
            pLen = pLen.next
            counter += 1
            if pLen == slow:
                break
                
        
        #move second pointer ahead by length
        slow, fast = head, head
        while counter > 0:
            fast = fast.next
            counter -= 1
        
        #keep iterating until they meet -> start of cycle
        while fast != slow:
            slow = slow.next
            fast = fast.next
            
        
        return slow
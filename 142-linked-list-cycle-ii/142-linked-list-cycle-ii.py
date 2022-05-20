# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def len_cycle(slow):
    curr = slow 
    length = 0
    while True:
        curr = curr.next
        length += 1
        if curr == slow:
            return length
    return length
        
def cycle_start(head, l):
        p1, p2 = head, head
        while l > 0:
            p2 = p2.next
            l -= 1
            
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
    


class Solution:
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        length = 0
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                length = len_cycle(slow)
                break
        
        if fast == None or fast.next == None:
            return None
        return cycle_start(head, length)

    
    
    
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        stack = deque()
        
        current = head
        while current:
            stack.append(current)
            current = current.next
            
        
        newHead = stack[-1]
        current = stack.pop()
        while stack:
            current.next = stack[-1]
            current = stack.pop() 
            
        current.next = None
        return newHead
            
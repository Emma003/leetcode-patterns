# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getNum(head):
    num = 0
    dec_pos = 1 #decimal position
    
    curr = head
    while curr:
        n = curr.val
        num += n*dec_pos
        curr = curr.next
        dec_pos *= 10 #shift decimal position every iteration (1 -> 10 -> 100)
    return num
    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1 = getNum(l1) 
        n2 = getNum(l2)
        sum = n1 + n2
        
        if sum == 0:
            return ListNode(0)
        
        # make new linked list
        head = ListNode(-1) #dummy node
        curr = head
        while sum > 0:
            last_digit = sum % 10
            curr.next = ListNode(last_digit)
            curr = curr.next
            sum //= 10
            
        return head.next
            
            
            
            
            
            
        
        
        
        
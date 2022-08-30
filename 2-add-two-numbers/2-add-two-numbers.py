# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def readNumber(head, radix):
    if not head:
        return 0
    
    return head.val*radix + readNumber(head.next, radix*10)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #read the numbers from the list
        num1 = readNumber(l1, 1)
        num2 = readNumber(l2, 1)
            
        #add them 
        totalNum = num1 + num2
        
        #convert the result to a linked list
        #dummy front node
        lastDigit = totalNum % 10
        totalNum //= 10
        
        resHead = ListNode(lastDigit)
        p = resHead
        
        while totalNum > 0:
            lastDigit = totalNum % 10
            totalNum //= 10
            p.next = ListNode(lastDigit)
            p = p.next
            
        return resHead
        
        
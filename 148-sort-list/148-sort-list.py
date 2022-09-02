# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeSort(head):
    if not head or not head.next:
        return head
    
    #find middle of list, set prev right before start of second half
    slow = fast = head
    prev= None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    #cut off first half of list
    prev.next = None
        
    #recurse each half
    L = mergeSort(head)
    R = mergeSort(slow)
    
    #merge halves
    return merge(L,R)
    
    
def merge(h1, h2):
    p1 = h1
    p2 = h2
    
    #dummy
    tail = ListNode()
    dummy = tail
    
    #merge two sorted linked lists
    while p1 and p2:
        if p1.val < p2.val:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
            
        tail = tail.next
        
    #add the remainder to end of tail
    if p1:
        tail.next = p1
    if p2:
        tail.next = p2
    
    #return merged list
    return dummy.next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return mergeSort(head)
        
        
    
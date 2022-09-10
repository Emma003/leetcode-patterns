# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#merge two lists at a time
def mergeTwoLists(head1, head2):
    p1 = head1
    p2 = head2
    dummy = ListNode(0)
    tail = dummy

    while p1 and p2:
        if p1.val < p2.val:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    if p1:
        tail.next = p1
    if p2:
        tail.next = p2

    return dummy.next
        
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #edge cases
        if not lists or len(lists) == 0:
            return None
        
        #combine two lists add save in temp array until it's all merged to a single list (len(lists) == 1)
        while len(lists) > 1:
            merged = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                merged.append(mergeTwoLists(l1,l2))
                
            lists = merged
            
        return lists[0]
        


        
        
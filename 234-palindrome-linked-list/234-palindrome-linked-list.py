# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
  prv, curr, nxt = None, head, None
  while curr:
    nxt = curr.next
    curr.next = prv
    prv = curr
    curr = nxt
  return prv


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # empty list or list with one element
        if head == None or head.next == None:
            return True

        # finding middle of list
        slow, fast = head, head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 

        # reverse second half
        tail = reverse(slow)

        # check for palindrome
        start, end = head, tail
        while start and end:
            if start.val != end.val:
                break

            start = start.next
            end = end.next

        reverse(tail)
        if start == None or end == None:
            return True
        return False


        
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        oldToNew = {}
        
        #1st pass -> create new nodes
        p = head
        while p:
            cloneP = Node(p.val)
            oldToNew[p] = cloneP
            p = p.next
        
        
        #2nd pass -> copy pointers
        p = head
        while p:
            #copy next
            
            #check null pointer
            if p.next == None:
                oldToNew[p].next = None
            else:
                oldToNew[p].next = oldToNew[p.next]
            
            #copy random
            
            #check null pointer
            if p.random == None:
                oldToNew[p].random = None
            else:
                oldToNew[p].random = oldToNew[p.random]
                
            p = p.next
                
        return oldToNew[head]
        
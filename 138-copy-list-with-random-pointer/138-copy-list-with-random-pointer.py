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
        
        
        #first pass 
        #mapping old node to new node
        map = {}
        p = head
        while p:
            map[p] = Node(p.val)
            p = p.next
            
        
        #second pass
        #linking
        p = head
        while p:
            newNode = map[p]
            
            #populatinng next pointer
            if p.next == None:
                newNode.next = None
            else:
                newNode.next = map[p.next]
                
            #population random pointer
            if p.random == None:
                newNode.random = None
            else:
                newNode.random = map[p.random]
            
            p = p.next
            
        return map[head]
            
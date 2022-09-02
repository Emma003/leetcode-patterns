"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #empty graph
        if not node:
            return None
        
        oldToNew = {}
        
        def clone(node):
            #if already visited, return the copy of the node
            if node in oldToNew:
                return oldToNew[node]
            
            #create copy of the node and add to dict
            copy = Node(node.val)
            oldToNew[node] = copy
            
            #iterate over node's neighbors and add their clones to copy's neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            
            return copy
            
        return clone(node)
        
        
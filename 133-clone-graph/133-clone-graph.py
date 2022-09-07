"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# {1:1, 2:2, 3:3, 4:4}
#
#
#
    
    

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        #dict: old node -> new node
        oldToNew = {}
        
        
        def dfs(node):
            #node in dict
            if node in oldToNew:
                return oldToNew[node]

            #else
            newNode = Node(node.val)
            oldToNew[node] = newNode

            #iterate over the node's neighbors
            for n in node.neighbors:
                newNode.neighbors.append(dfs(n))
            
            return newNode
        
        #create a node, map the old node to the new node (same value, NOT SAME NEIGHBOURS)
        return dfs(node)
        
       
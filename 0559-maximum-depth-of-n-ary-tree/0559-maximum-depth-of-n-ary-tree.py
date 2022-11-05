"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        def dfs(root):
            if not root.children:
                return 1
            
            maxDepth = -1
            
            for child in root.children:
                maxDepth = max(dfs(child), maxDepth)
                
            return 1 + maxDepth
        
        return dfs(root)
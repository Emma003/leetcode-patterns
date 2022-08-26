# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        count[0] = 0
        
        def dfs(root, maxSoFar):
            
            if not root:
                return
            
            #good node
            if root.val >= maxSoFar:
                count[0] += 1
            
            #update maxSoFar
            maxSoFar = max(maxSoFar, root.val)
            
            #send to children
            dfs(root.left, maxSoFar)
            dfs(root.right, maxSoFar)
            
        dfs(root, -math.inf)
        return count[0]
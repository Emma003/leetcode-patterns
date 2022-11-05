# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.maxDiameter = -1
        
        def dfs(root):
            if not root:
                return 0
            
            L = dfs(root.left)
            R = dfs(root.right)
            
            self.maxDiameter = max(self.maxDiameter, L + R)
            
            return 1 + max(L,R)
        
        dfs(root)
        return self.maxDiameter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = []
        
        def dfs(root):
            if not root:
                return False
            
            
            if dfs(root.left):
                return True
            
            self.count.append(root.val)
            if len(self.count) == k:
                return True
            
            if dfs(root.right):
                return True
            
        if dfs(root):
            return self.count[k-1]
            
            
            
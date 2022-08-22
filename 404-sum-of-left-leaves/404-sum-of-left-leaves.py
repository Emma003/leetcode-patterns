# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = [0]
        sum[0] = 0
        
        def dfs(root):
            if not root:
                return 0
            
            if root.left is not None and root.left.left is None and root.left.right is None:
                sum[0] += root.left.val
                
            dfs(root.left)
            dfs(root.right)
            
            
        dfs(root)
        return sum[0]
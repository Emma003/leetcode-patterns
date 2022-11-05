# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            L = dfs(root.left)
            R = dfs(root.right)
            depth = 1 + max(L[1], R[1])

            if not L[0] or not R[0]:
                return [False, depth]

            if abs(L[1] - R[1]) > 1:
                return [False, depth]

            return [True, depth]
    
        return dfs(root)[0]
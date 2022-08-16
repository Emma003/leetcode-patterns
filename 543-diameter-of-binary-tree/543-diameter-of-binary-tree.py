# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [0];
        
        def dfs(root):
            if not root:
                return 0
            
            lHeight = dfs(root.left)
            rHeight = dfs(root.right)
            
            maxDiameter[0] = max(maxDiameter[0], lHeight + rHeight)
            
            return max(lHeight,rHeight) + 1
        
        
        dfs(root)
        return maxDiameter[0]
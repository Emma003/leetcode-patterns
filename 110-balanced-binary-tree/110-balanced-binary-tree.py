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

            left = dfs(root.left)
            right = dfs(root.right)


            if (not left[0] or not right[0]):
                balanced = False
            else:
                balanced = abs(left[1] - right[1]) <= 1

            height = max(left[1], right[1]) + 1

            return [balanced, height]
        
        return dfs(root)[0]
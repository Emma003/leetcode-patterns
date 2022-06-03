# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root, sum):
    if not root:
        return 0
    
    sum += root.val
    
    if not root.left and not root.right:
        return sum
    
    return dfs(root.left, sum*10) + dfs(root.right, sum*10)

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return dfs(root, 0)
        
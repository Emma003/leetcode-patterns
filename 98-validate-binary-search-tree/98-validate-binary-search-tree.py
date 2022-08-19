# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bst(root, lo, hi):
            if not root:
                return True
            
            if root.val >= hi or root.val <= lo:
                return False
            
            return bst(root.left, lo, root.val) and bst(root.right, root.val, hi)
        
        return bst(root, -math.inf, math.inf)
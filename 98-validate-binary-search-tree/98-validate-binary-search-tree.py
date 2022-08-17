# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        #inorder traversal [l -> curr -> r]
        def inorder(root, left, right):
            if not root:
                return True
            
            if not root.val > left or not root.val < right:
                return False
            
            return inorder(root.left, left, root.val) and inorder(root.right, root.val, right)

        
        return inorder(root, -math.inf, math.inf)
        
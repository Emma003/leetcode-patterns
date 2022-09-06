# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = 0
        self.count = k
        
        def dfs(root):
            if not root:
                return
            
            #inorder traversal (left -> curr -> right)
            dfs(root.left)
            
            self.count -= 1
            if self.count == 0:
                self.result = root.val
                
            dfs(root.right)
            
        
        dfs(root)
        return self.result
            
        
            
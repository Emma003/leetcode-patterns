# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        '''
            inorder traversal of the tree -> sorted array
            traverse array and make sure arr[i+1] > arr[i]
        
        '''
        
        arr = []
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            
            arr.append(root.val)
            
            inorder(root.right)
            
            
        inorder(root)
        
        #check arr is sorted
        for i,n in enumerate(arr):
            if i == 0:
                continue
                
            if arr[i] <= arr[i-1]:
                return False
            
        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def pairwiseCheck(l, r):
    if not l and not r:
        return True
    
    if not l or not r:
        return False
    
    if l.val != r.val:
        return False
    
    return pairwiseCheck(l.left, r.right) and pairwiseCheck(l.right, r.left)

    
    
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return pairwiseCheck(root.left, root.right)
        
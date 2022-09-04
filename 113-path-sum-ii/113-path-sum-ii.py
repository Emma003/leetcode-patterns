# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#currPath [5,]

#allPath []

#currSum = 0

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        allPaths = []
        
        def dfs(root, currSum, currPath, allPaths):
            if not root:
                return 
            
            currPath.append(root.val)
            
            if not root.left and not root.right and root.val+currSum == targetSum:
                allPaths.append(list(currPath))
            
                
            dfs(root.left, currSum+root.val, currPath, allPaths)
            dfs(root.right, currSum+root.val, currPath, allPaths)
            
            del currPath[-1]
            
        dfs(root, 0, [], allPaths)
    
        return allPaths
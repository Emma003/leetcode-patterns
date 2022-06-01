# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root == None:
            return []
        
        avg_array = []
        q = deque()
        q.append(root)
        
        while q: 
            level_sum = 0
            level_length = len(q)
            
            for i in range(level_length):
                curr = q.popleft()
                level_sum += curr.val
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            avg_array.append(level_sum / level_length)
        
        return avg_array
            
        
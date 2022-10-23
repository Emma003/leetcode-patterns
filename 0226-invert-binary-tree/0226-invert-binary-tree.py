# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs(root):
            if not root:
                return
            
            q = deque()
            q.append(root)
            
            while q:
                
                l = len(q)
                
                for _ in range(l):
                    
                    curr = q.popleft()
                    curr.left, curr.right = curr.right, curr.left
                    
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            
        bfs(root)
        return root
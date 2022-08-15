# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #init queue
        q = deque()
        q.append(root)
        
        #bfs
        while q:
            l = len(q)
            
            for i in range(l):
                curr = q.popleft()
                
                #swapping nodes
                tmpNode = curr.left
                curr.left = curr.right
                curr.right = tmpNode
                
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
        return root
                
    # q = [4]
    # curr_level = [4]
    # depth = 1
    # l = 1
    # i = 0
    #curr.val = 4
    
    
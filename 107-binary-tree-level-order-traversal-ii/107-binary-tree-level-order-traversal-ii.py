# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        stack = deque()
        res, q = [], deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                level.append(curr.val)

            stack.append(level)

        for _ in range(len(stack)):
            res.append(stack.pop())

        return res
        
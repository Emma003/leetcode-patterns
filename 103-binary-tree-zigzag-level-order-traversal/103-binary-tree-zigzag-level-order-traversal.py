# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        res = []
        q = deque()
        q.append(root)
        l_to_r = True

        while q:
            level = deque()
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

                if l_to_r:
                    level.append(curr.val)
                else:
                    level.appendleft(curr.val)

            res.append(list(level))
            l_to_r = not l_to_r

        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        depth = 1
        q = deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left == None and curr.right == None:
                    return depth

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            depth +=1

        return depth
        
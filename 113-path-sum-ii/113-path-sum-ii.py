# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def has_path(root, sum, path, paths):
    if not root:
        return 

    path.append(root.val)

    if not root.left and not root.right and sum == root.val:
        paths.append(list(path))
    else: 
        has_path(root.left, sum-root.val, path, paths)
        has_path(root.right, sum-root.val, path, paths)

    del path[-1]

class Solution:
    def pathSum(self, root: Optional[TreeNode], k: int) -> List[List[int]]:
        paths = []
        has_path(root, k, [], paths)
        return paths
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sortedArr = []

        def inorder(root, sortedArr):
            if not root:
                return

            inorder(root.left, sortedArr)
            sortedArr.append(root.val)
            inorder(root.right, sortedArr)

            
            
        inorder(root, sortedArr)

        left, right = 0, len(sortedArr)-1

        while left<right:
            currentSum = sortedArr[left] + sortedArr[right]
            
            if currentSum == k:
                return True
            
            elif currentSum > k:
                right -= 1

            else:
                left += 1

        return False

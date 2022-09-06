
def reverse(arr, l, r):
    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """
        #test input: [1,2,3,4,5,6,7] k=3
        
        reverse(nums, 0, len(nums)-1) #nums = [7,6,5,4,3,2,1]
        
        #reverse both halves
        reverseIndex = k % len(nums)
        reverse(nums, 0, reverseIndex-1) #nums = [5,6,7,4,3,2,1]
        reverse(nums, reverseIndex, len(nums)-1) #nums = [5,6,7,1,2,3,4]
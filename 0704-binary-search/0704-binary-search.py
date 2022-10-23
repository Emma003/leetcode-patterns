class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binsearch(nums, target, l, r):
            if l > r:
                return -1
            
            mid = (l+r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binsearch(nums, target, mid+1, r)
            else:
                return binsearch(nums, target, l, mid-1)
            
        return binsearch(nums, target, 0, len(nums)-1)
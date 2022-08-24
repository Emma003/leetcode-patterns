class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        l,r = 0, len(nums)-1
        
        while l<r:
            sum = nums[l] + nums[r]
            
            if sum == t:
                return [l+1,r+1]
            if sum > t:
                r-=1
                continue
            if sum < t:
                l+=1
                continue
                
       
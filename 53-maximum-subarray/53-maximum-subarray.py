class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = 0, -math.inf
        start = 0
        
        for end in range(len(nums)):
            currSum += nums[end]
            maxSum = max(maxSum, currSum)
            
            if currSum < 0:
                currSum = 0
                start = end
                
            
            
            
        return maxSum
                
            
            
        
            
        
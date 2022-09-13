class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, start = -math.inf, 0
        currSum = 0
        
        for end in range(len(nums)):
            n = nums[end]
            currSum += n
            maxSum = max(maxSum, currSum)
            
            if currSum < 0:
                currSum = 0
                start = end
                
            
            
        return maxSum
            
#max 1
#start 0
#end 1
#currSum 1
#n -2
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #RECURSIVELY WITH ANY NUMBER-SUM
        
        nums.sort()
        res, quad = [], []
        k = 4 #4sum
        
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums)-(k-1)):
                    if i > start  and nums[i] == nums[i-1]:
                        continue
                
                    quad.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    quad.pop()
                    

            # base case (k = 2)
            else: 
                l,r = start, len(nums)-1
                while l<r:
                    sum = nums[l] + nums[r]
                    if sum == target:
                      res.append(quad + [nums[l], nums[r]])
                      l+=1 
                      while l<r and nums[l] == nums[l-1]:
                        l+=1
                    elif sum > target:
                      r-=1
                    else:
                      l+=1
                    
                    
        kSum(k, 0, target)
        return res
        
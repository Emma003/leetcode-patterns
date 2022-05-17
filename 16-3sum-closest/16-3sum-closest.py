class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #  i l   r   sum: 1
        # -4 1 3 4 7 target:2
        nums.sort() #time compl O(nlogn)
        min_diff = math.inf
        for i,n in enumerate(nums):
            l,r = i+1, len(nums)-1
            while l<r:
                curr_diff = target - (n + nums[l]+nums[r])
                
                # triplet sum = target
                if curr_diff == 0:
                    return target
                
                if abs(curr_diff) < abs(min_diff):
                    min_diff = curr_diff
                
                if curr_diff < 0:
                    r -= 1
                else: 
                    l += 1
                    
        return target - min_diff
                
            
            
        
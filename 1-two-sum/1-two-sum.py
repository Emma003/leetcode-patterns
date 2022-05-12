class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        set = {}
        for i, n in enumerate(nums):
            if (target - n) in set:
                return [set[target - n], i]
            set[n] = i
        
        
        
        
        
        
        
        
        map = {}
        for i in range(len(nums)):
            y = target - nums[i]
            if y in map:
                return [map[y], i]
            map[nums[i]] = i
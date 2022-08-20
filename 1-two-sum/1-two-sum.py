class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        set = {}
        res = []
        
        for i,n in enumerate(nums):
            targSum = target - n
            if targSum in set:
                return [set[targSum], i]
            
            set[n] = i
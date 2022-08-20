class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set = {}
        
        for n in nums:
            if n in set:
                return True
            
            set[n] = 1
            
        return False
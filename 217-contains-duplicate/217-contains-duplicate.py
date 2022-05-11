class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set = {}
        
        for c in nums:
            if c in set:
                return True
            set[c] = 1
        return False
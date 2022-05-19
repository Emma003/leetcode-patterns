class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        floor = math.floor(n/2)
        set = {}
        
        for num in nums:
            if num not in set:
                set[num] = 0
            set[num] += 1
            if set[num] > floor:
                return num
        
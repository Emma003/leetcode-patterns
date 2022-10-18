class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        map = {}

        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1

        count = 0
        res = 0
        for c in map.values():
            res += (c*(c-1))/2

        return int(res)

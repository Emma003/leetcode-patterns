class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, res, one_count = 0, 0, 0
        set = {}

        for r in range(len(nums)):
            if nums[r] == 1:
                one_count += 1

            if (r-l + 1) - one_count > k:
                if nums[l] == 1:
                    one_count -= 1
                l += 1

            res = max(res, r-l+1)

        return res

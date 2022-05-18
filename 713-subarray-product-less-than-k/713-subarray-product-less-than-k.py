class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, pdt, count = 0, 1, 0
        for r in range(len(nums)):
            pdt *= nums[r]
            # shrink window while pdt>=k
            while pdt>=k and l<=r:
                pdt /= nums[l]
                l += 1
            # increase count (account for subarrays with one member)
            count += r-l+1
            
        return count
        
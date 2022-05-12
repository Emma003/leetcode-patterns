class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, count = 0, 1
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                l = r
                nums[count] = nums[r]
                count += 1
        return count
        
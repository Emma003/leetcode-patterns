class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, high, i = 0, len(nums)-1, 0

        # quick sort
        while i <= high:
            if nums[i] == 0:
                nums[i] = nums[low]
                nums[low] = 0
                low += 1
                
            # dont increment i if you swap the high value (continue)
            elif nums[i] == 2:
                nums[i] = nums[high]
                nums[high] = 2
                high -= 1
                continue

            i += 1

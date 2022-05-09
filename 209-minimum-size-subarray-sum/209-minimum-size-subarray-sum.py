class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size, window_start, window_sum = math.inf, 0, 0.0

        for window_end in range(len(nums)):
            window_sum += nums[window_end]

            while window_sum >= target:
              min_size = min(min_size, (window_end+1) - window_start)
              window_sum -= nums[window_start]
              window_start += 1

        if min_size == math.inf:
            return 0

        return min_size
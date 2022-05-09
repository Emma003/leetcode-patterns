class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        set = {}
        window_start, max_size = 0, 0

        for window_end in range(len(s)):
            right_char = s[window_end]

            if right_char in set:
                window_start = max(window_start, set[right_char] + 1)

            set[right_char] = window_end
            max_size = max(max_size, window_end - window_start + 1)

        return max_size
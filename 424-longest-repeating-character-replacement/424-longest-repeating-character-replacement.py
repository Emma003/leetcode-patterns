class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, result, max_repeat = 0, 0, 0
        set = {}

        for r in range(len(s)):
            # increment if it exists, return 0 if it doesnt
            set[s[r]] = 1 + set.get(s[r], 0)
            max_repeat = max(max_repeat, set[s[r]])

            if (r - l + 1) - max_repeat > k:
                set[s[l]] -= 1
                if set[s[l]] == 0:
                    del set[s[l]]
                l += 1
            result= max(result, r - l + 1)


        return result
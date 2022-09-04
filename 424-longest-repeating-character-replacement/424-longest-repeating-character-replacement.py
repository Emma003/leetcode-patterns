class Solution:
    def characterReplacement(self, str1: str, k: int) -> int:
        l, result, max_repeat = 0, 0, 0
        set = {}

        for r in range(len(str1)):
            # increment if it exists, return 0 if it doesnt
            set[str1[r]] = 1 + set.get(str1[r], 0)
            max_repeat = max(max_repeat, set[str1[r]])

            if (r - l + 1) - max_repeat > k:
                set[str1[l]] -= 1
                if set[str1[l]] == 0:
                    del set[str1[l]]
                l += 1
            result= max(result, r - l + 1)


        return result
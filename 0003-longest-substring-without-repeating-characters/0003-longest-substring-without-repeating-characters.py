# dict = 
# [,]
# [b,1]
# [c,1]

# maxW = 3

class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        start = 0
        maxWindow = 0
        chars = set()

        for end in range(len(str)):

            while str[end] in chars:
                if str[start] in chars:
                    chars.remove(str[start])
                start += 1

            chars.add(str[end])
            maxWindow = max(maxWindow, end-start+1)

        return maxWindow
    
    
    
    
    
    
    
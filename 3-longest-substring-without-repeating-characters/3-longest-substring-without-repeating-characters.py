# dict = 
# [,]
# [b,1]
# [c,1]

# maxW = 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxWindow = 0
        dict = {}
        
        for right in range(len(s)):
            
            while s[right] in dict and left<=right:
                del dict[s[left]]
                left += 1
                
            dict[s[right]] = 1
            
            maxWindow = max(maxWindow, right - left + 1)
            
        return maxWindow
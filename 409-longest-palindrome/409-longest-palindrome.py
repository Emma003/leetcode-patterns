class Solution:
    def longestPalindrome(self, str1: str) -> int:
        map = set()
        count = 0
        
        for s in str1:
            if s not in map:
                map.add(s)
            else:
                count += 2
                map.remove(s)
                    
        if len(map) > 0:
            return count + 1
        
        return count
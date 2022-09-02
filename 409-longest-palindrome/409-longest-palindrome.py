class Solution:
    def longestPalindrome(self, str1: str) -> int:
        map = {}
        count = 0
        
        for s in str1:
            if s not in map:
                map[s] = 1
            else:
                map[s] -= 1
                if map[s] % 2 == 0:
                    count += 2
                    if map[s] == 0:
                        del map[s]
                    
        if len(map) > 0:
            return count + 1
        
        return count
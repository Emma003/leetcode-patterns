class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #load map
        chars = {}
        for c in s1:
            if c not in chars:
                chars[c] = 0
            chars[c] += 1
            
        #check s2 (sliding window)
        l, matches = 0, 0
        
        for r in range(len(s2)):
            if s2[r] in chars:
                chars[s2[r]] -= 1
                if chars[s2[r]] == 0:
                    matches += 1
                    
            if matches == len(chars):
                return True
            
            if r >= len(s1)-1:
                if s2[l] in chars:
                    if chars[s2[l]] == 0:
                        matches -= 1
                    chars[s2[l]] += 1
                l+= 1
                
                
        return False
                    

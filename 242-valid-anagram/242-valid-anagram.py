class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        set = {}
        for c in s: 
            if c not in set:
                set[c] = 0
            set[c] += 1
        
        matches = 0
        
        for r in range(len(t)):
            if t[r] in set:
                set[t[r]] -= 1
                if set[t[r]] == 0:
                    matches += 1
                    
            if matches == len(set):
                return True
            
        return False
            
        
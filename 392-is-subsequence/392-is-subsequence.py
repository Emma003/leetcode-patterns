class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if both strings are empty
        if len(s) == 0 and len(t) == 0:
            return True
        # if one string is empty while he other isn't
        elif len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        
        
        matches = 0
        sPointer = 0
        for char in t:
            if char == s[sPointer]:
                sPointer += 1
                matches += 1
                
            if matches == len(s):
                return True
            
        
        return False
    
            
            
        
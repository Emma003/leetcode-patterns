class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: 
            return True
        if len(t) == 0:
            return False
        
        
        
        sPointer = 0
        for char in t:
            if char == s[sPointer]:
                sPointer += 1
                
            if sPointer == len(s):
                return True
            
        
        return False
    
            
            
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #load t in dict
        dictT = {}
        for char in t:
            if char not in dictT:
                dictT[char] = 0
            dictT[char] += 1
            
        
        matches = 0
        for char in s:
            if char in dictT:
                dictT[char] -= 1
                if dictT[char] == 0:
                    matches += 1
                    
        if matches == len(dictT):
            return True
        
        return False
            
        
        
        
        
        
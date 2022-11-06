'''
s = anagram

t = nagaram



sDict = { 'a': 3,
            'n': 1,
            'g': 1,
            'r': 1,
            'm': 1
}

load every char of s in a dict
matches = number of k

iterate over chars in t:
    if char not in sDict: FALSE
    else: decrement its value by 1
        if the value becomes 0: increment number of matches
    



'''



class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMap = {}
        
        for character in s:
            if character not in sMap:
                sMap[character] = 0
            sMap[character] += 1
            
        for character in t:
            if character not in sMap:
                return False
            
            sMap[character] -= 1
            if sMap[character] == 0:
                del sMap[character] 
                
        if len(sMap) != 0:
            return False
        return True
        
        
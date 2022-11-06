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
        if not s and not t:
            return True
        if not s or not t:
            return False
        
        sDict = {}
        
        for character in s:
            if character not in sDict:
                sDict[character] = 0
            sDict[character] += 1
            
        
        matches = 0
        for character in t:
            if character not in sDict:
                return False
            
            sDict[character] -= 1
            if sDict[character] == 0:
                matches += 1
                
        if matches == len(sDict):
            return True
        
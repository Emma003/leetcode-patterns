class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}
        
        for char in ransomNote:
            if char not in map:
                map[char] = 0
            map[char] += 1
            
            
        matches = 0
        for char in magazine:
            if char in map:
                map[char] -= 1
                if map[char] == 0:
                    matches += 1
                    
            if matches == len(map):
                return True
            
        return False
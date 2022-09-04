class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        map = {}
        
        #load p in map
        for c in p:
            if c not in map:
                map[c] = 0
            map[c] += 1
            
        #iterate over p
        l = 0
        matches = 0
        for end in range(len(s)):
            r = s[end]
            
            if r in map:
                map[r] -= 1
                if map[r] == 0:
                    matches += 1
                    
            if matches == len(map):
                res.append(l)
                
            if end >= len(p)-1:
                if s[l] in map:
                    if map[s[l]] == 0:
                        matches -= 1
                    map[s[l]] += 1
                    
                l += 1
                
        return res
class Solution:
    def characterReplacement(self, str1: str, k: int) -> int:
        l, maxRepeat, res = 0, 0, 0
        map = {}
        
        
        for r in range(len(str1)):
            rightChar = str1[r]
            
            if rightChar not in map:
                map[rightChar] = 0
            map[rightChar] += 1
            
            maxRepeat = max(maxRepeat, map[rightChar])
            
            #if we exceed k, slide window forward
            if (r-l+1) - maxRepeat > k:
                leftChar = str1[l]
                
                map[leftChar] -= 1
                if map[leftChar] == 0:
                    del map[leftChar]
                    
                l+=1
                
            res = max(res, r-l+1)
        return res

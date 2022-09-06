class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        res = []
        
        #count all letters per word 
        for word in strs:
            count = [0] * 26
            
            for char in word:
                charIndex = ord(char) - ord('a')
                count[charIndex] += 1
                
            #create map with countArray:list of words
            if tuple(count) not in map:
                map[tuple(count)] = []
            map[tuple(count)].append(word)
            
        
        #iterate through map and lists of words to result array
        for anagrams in map.values():
            res.append(list(anagrams))
            
            
        return res
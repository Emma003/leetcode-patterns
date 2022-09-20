class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        res = []
        
        #keep track of the number of letters in each word
        
        
        
        #populate the array for each word
        for string in strs:
            
            #initialize count array to 26 elements
            count = [0] * 26 
            
            
            for char in string:
                charNum = ord('a') - ord(char)
                count[charNum] += 1
                
            #create entry in map
            if tuple(count) not in map:
                map[tuple(count)] = []
            map[tuple(count)].append(string)
            
        
        #iterate over values of map and add to result
        for group in map.values():
            res.append(group)
            
        return res
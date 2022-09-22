class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        #go over every char of every string 
        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return res
                
            res += string[i]
            
        return res
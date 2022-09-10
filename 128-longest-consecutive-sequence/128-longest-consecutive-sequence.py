class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        map = set(nums)
        maxLength = 0
        
        for n in map:
            currSeq = 1
            
            #check for beginning of conseq sequence
            if (n - 1) not in map:
                nextNum = n + 1
                
                while nextNum in map:
                    currSeq += 1
                    nextNum += 1
            maxLength = max(maxLength, currSeq)
            
        return maxLength
            
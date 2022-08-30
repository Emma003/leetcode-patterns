class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxSeq = 0
        
        #turn array into hashset for faster look up:
        numSet = set(nums)
        
        for n in numSet:
            currSeq = 1
            
            #check if n is the start of a sequence
            if n-1 not in numSet:
                nextNum = n+1
                while nextNum in numSet:
                    currSeq += 1
                    nextNum += 1
                    
            maxSeq = max(currSeq, maxSeq)
            
        return maxSeq
                
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in numSet:
            seqLength = 1
            
            #check for start of seq
            if num-1 not in numSet:
                next = num+1 
                while next in numSet:
                    seqLength += 1
                    next += 1
            
            longest = max(longest, seqLength)
            
        
        return longest
            
                
                
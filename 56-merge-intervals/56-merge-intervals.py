class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        merged = []
        
        #sort 
        intervals.sort(key = lambda l:l[0])
        
        #set start & end of first interval
        start = intervals[0][0]
        end = intervals[0][1]
        
        #iterate through intervals
        for i in range(1, len(intervals)):
            curr = intervals[i]
            
            #checking for overlaps
            if curr[0] <= end:
                end = max(curr[1], end)
            else:
                merged.append([start,end])
                start = curr[0]
                end = curr[1]
                
        merged.append([start,end])
        return merged
        
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0])
        count = 0
        
        #iterate over intervals and count overlaps
        start, end = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            
            #if overlap
            if curr[0] < end:
                count += 1
                
                #update start and end with the overlapping interval that has the earlier end time (get rid of the wider interval)
                if curr[1] < end:
                    start = curr[0]
                    end = curr[1]
                    
            #if no overlap: update start and end to next interval
            else:
                start = curr[0]
                end = curr[1]
                    
        return count
    
    
    
            
                    
                
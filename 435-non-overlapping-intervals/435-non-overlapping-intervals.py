class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort
        intervals.sort(key = lambda l:l[0])
        
        start = intervals[0][0]
        end = intervals[0][1]
        
        min_removals = 0
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            # if overlap
            if curr[0] < end:
                min_removals += 1
                end = min(end, curr[1])
            else:
                start = curr[0]
                end = curr[1]
                
        return min_removals
            
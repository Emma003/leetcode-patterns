class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #will split intervals into left, insert then right
        l,r = [], []
        start, end = newInterval[0], newInterval[1]
        
        for curr in intervals:
            #newInterval is after curr
            if start > curr[1]:
                l.append(curr)
                
            #newInterval is before curr
            elif end < curr[0]:
                r.append(curr)
                
            #newInterval and curr overlap
            else:
                start = min(curr[0], start)
                end = max(curr[1], end)
                
        #add all intervals together
        return l + [[start,end]] + r
            
        
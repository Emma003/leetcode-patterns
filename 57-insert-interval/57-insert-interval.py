class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = [], []
        
        start = newInterval[0]
        end = newInterval[1]
        
        for curr in intervals:
            # interval is to the left of target
            if start > curr[1]:
                l.append(curr)
                
            # interval is to the right of target
            elif end < curr[0]:
                r.append(curr)
                
            # overlap
            else: 
                start = min(start, curr[0])
                end = max(end, curr[1])
        
        return l + [[start,end]] + r
            
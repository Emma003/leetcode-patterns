class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        res = [intervals[0]]
        
        for start, end in intervals:
            latestEnd = res[-1][1]
            if start <= latestEnd:
                res[-1][1] = max(end, latestEnd)
            else:
                res.append([start,end])
            
        return res
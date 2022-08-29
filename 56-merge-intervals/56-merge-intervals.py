class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            latestEnd = merged[-1][1]
            
            if start <= latestEnd:
                merged[-1][1] = max(end, latestEnd)
                
            else:
                merged.append([start,end])
                
                
        return merged
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key = lambda i:i[0])
        
        #the heap will only hold end times
        minRooms = []
        heapq.heapify(minRooms)
        heapq.heappush(minRooms, intervals[0][1])
        
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            #room is free
            if start >= minRooms[0]:
                heapq.heappop(minRooms)
                
            heapq.heappush(minRooms, end)
                
        return len(minRooms)
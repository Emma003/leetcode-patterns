

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(-stone) #O(N)
            
        heapq.heapify(heap) #O(N)
        
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            
            diff = stone1 - stone2
            
            if diff != 0:
                heapq.heappush(heap, -diff)
            
            
        return -heap[0] if len(heap)==1 else 0
    
#time: O(NlogN)
#space:O(N)
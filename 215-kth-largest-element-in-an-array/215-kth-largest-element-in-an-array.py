class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap) #O(n)
        
        for num in nums:
            heapq.heappush(maxHeap, -num) #O(n)
        
        
        for i in range(k-1):
            heapq.heappop(maxHeap)
            
        return -heapq.heappop(maxHeap)
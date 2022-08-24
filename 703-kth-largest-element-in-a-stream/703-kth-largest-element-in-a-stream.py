# EDGE CASES: k < nums or k > nums

class KthLargest:

    def __init__(self, k: int, nums: List[int]): #O(NlogN)
        #keep a min heap of size k
        self.minHeap, self.k = nums, k
        
        heapq.heapify(self.minHeap) #n
        
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) #logn
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val) #logn * number of function calls
        
        #only pop IF the minHeap is of size greater than k!!!
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) #logn
        
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
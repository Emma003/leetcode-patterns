

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #make min heap
        self.heap = nums
        heapq.heapify(self.heap)
        self.k = k
        
        #maintain the min heap size to k by removing the msmallest until its only the k largest elements left in the heap
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        return self.heap[0]


#time :
    # constructor (heapify + pop n-k times): O(N + Nlog(N)) = O(NlogN)
    # add (push&pop in heap of size k max once * number of fct calls (M)): O(2*log(k)* M) = O(MlogK)
    
    # total: O(NlogN + Mlogk)
    
    
#space: O(N) -- heap
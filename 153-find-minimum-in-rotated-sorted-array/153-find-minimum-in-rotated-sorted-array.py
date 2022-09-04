class Solution:
    def findMin(self, nums: List[int]) -> int:
        #find whether left or right side is strictly increasing
            #if left side is strictly incr, check right and vice versa
        #check if arr is fully sorted (l<r)
        #also update max with mid
        
        self.minVal = math.inf
        
        def binSearch(arr, l, r):
            #if you traversed whole array
            if l>r: 
                return
            
            #if array is already fully sorted, no need to keep traversing
            if arr[l] < arr[r]:
                self.minVal = min(self.minVal, arr[l])
                return
            
            #find strictly incr half and traverse the other half
            mid = (l+r)//2
            self.minVal = min(self.minVal, arr[mid])
            
            #left is strictly incr (MID IS GREATER THAN OR EQUAL TO!!)
            if arr[mid] >= arr[l]:
                binSearch(arr, mid+1, r)
                
            #right is strictly incr
            else: 
                binSearch(arr, l, mid-1)
                
        binSearch(nums, 0, len(nums)-1)
        return self.minVal
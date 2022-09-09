class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        self.min = math.inf
        
        def binSearch(arr, l, r):
            if l > r:
                return 
            
            #check whether the array is already fully sorted
            if arr[l] < arr[r]:
                self.min = min(self.min, arr[l])
                return
                
            mid = (l+r) // 2
            
            #check middle is minimum
            self.min = min(self.min, arr[mid])
            
            
            #check if left is strictly increasing or right is strictly increasing
            if arr[l] > arr[mid]:
                binSearch(arr, l, mid-1)
                
            else:
                binSearch(arr, mid+1, r)
                
                
                
        binSearch(nums, 0, len(nums)-1)
        return self.min
            
            
            
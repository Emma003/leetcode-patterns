


class Solution:
    def findMin(self, nums: List[int]) -> int:
        self.res = math.inf
        
        
        def binSearch(arr, l, r):
            if l > r:
                return 
            
            #array is already fully sorted (arr[0] is the min)
            if arr[l] < arr[r]:
                self.res = min(self.res, arr[l])
                return
            
            mid = (l+r) // 2
            self.res = min(self.res, arr[mid])
            #check if left is strictly increasing
            if arr[mid] >= arr[l]:
                binSearch(arr, mid+1, r)

            #right is strictly incr
            else:
                binSearch(arr, l, mid-1)
        
        
        binSearch(nums, 0, len(nums)-1)
        return self.res
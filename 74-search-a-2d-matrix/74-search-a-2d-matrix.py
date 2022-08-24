class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        totalArr = []
        
        for arr in matrix:
            totalArr += arr
            
        
        def binsearch(arr, l, r, t):
            if l>r:
                return False
            
            mid = (l+r) // 2
            
            if arr[mid] == t:
                return True
            if arr[mid] > t:
                return binsearch(arr,l,mid-1,t)
            if arr[mid] < t:
                return binsearch(arr, mid+1, r, t)
            
        return binsearch(totalArr, 0, len(totalArr)-1, target)
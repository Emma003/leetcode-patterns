
def binSearch(arr, l, r, target):
    if l > r:
        return -1
    
    mid = (l+r) // 2
    
    #target found
    if arr[mid] == target:
        return mid
    
    #check if left strictly incr.
    if arr[mid] >= arr[l]:
        #targ > mid
        if target > arr[mid] or target < arr[l]:
            return binSearch(arr, mid+1, r, target)
        # left < targ < mid
        else:
            return binSearch(arr, l, mid-1, target)
            
    #right strictly incr.
    else:
        if target < arr[mid] or target > arr[r]:
            return binSearch(arr, l, mid-1, target)
        else:
            return binSearch(arr, mid+1, r, target)
        


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binSearch(nums, 0, len(nums)-1, target)
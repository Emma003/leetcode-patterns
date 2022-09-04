
def quickSelect(arr, k, l, r):
    if l>r:
        return
    
    targetIndex = len(arr) - k
    
    pivot = partition(arr, l, r)
    
    if pivot == targetIndex:
        return arr[pivot]
    elif pivot > targetIndex:
        return quickSelect(arr, k, l, pivot-1)
    else:
        return quickSelect(arr, k, pivot+1, r)
        
        
def partition(arr, l, r):
    i = l
    
    for j in range(l, r):
        if arr[j] <= arr[r]:
            arr[i], arr[j] = arr[j], arr[i]
            i+= 1
            
    arr[i], arr[r] = arr[r], arr[i]
    
    return i
    

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #quick select: target index is len(nums)-k
        #partition: find a pivot, move less than to left and more than to the right
        
        return quickSelect(nums, k, 0, len(nums)-1)
        
        
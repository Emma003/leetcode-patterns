
def quickSelect(arr, l, r, k):
    if l > r:
        return -1
    
    targetIndex = len(arr) - k
    
    currPartitionIndex = partition(arr, l, r)
    
    if currPartitionIndex == targetIndex:
        return arr[currPartitionIndex]
    elif currPartitionIndex > targetIndex:
        return quickSelect(arr, l, currPartitionIndex - 1,k)
    elif currPartitionIndex < targetIndex:
        return quickSelect(arr, currPartitionIndex + 1, r,k)


def partition (arr, l, r):
    #pivot == arr[r]
    
    #p = tail of less than group
    p = l
    for i in range(l,r):
        #if curr < pivot, shift to less group
        if arr[i] <= arr[r]:
            arr[p], arr[i] = arr[i], arr[p]
            p += 1
            
    #swap tail of less group (p) with pivot
    arr[p], arr[r] = arr[r], arr[p]

    return p


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quickSelect(nums, 0, len(nums)-1, k)
        
        
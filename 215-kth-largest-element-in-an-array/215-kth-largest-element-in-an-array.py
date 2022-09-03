
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
            swap(arr, p, i)
            p += 1
            
    #swap tail of less group (p) with pivot
    swap(arr, p, r)

    return p

def swap(arr, i1, i2):
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quickSelect(nums, 0, len(nums)-1, k)
        
        
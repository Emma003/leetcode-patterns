# [2,3,6,1,5,4]

def partition(arr, l, r):
    #r is pivot
    i = l #tail of small values
    
    for j in range(l, r):
        
        #if arr[i] < arr[pivot], swap i and j
        if arr[j] <= arr[r]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            
    #swap i and pivot
    arr[i], arr[r] = arr[r], arr[i]
    
    return i


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #the kth largest element in the array when sorted should be at position len(nums)-k
        target = len(nums) - k
        
        #quick select to find right position
        l,r = 0, len(nums)-1
        
        while l<r:
            #pivot is right most
            sortedIndex = partition(nums, l, r)

            #if sorted index is at k, return element
            if sortedIndex < target:
                l = sortedIndex + 1
                
            elif sortedIndex > target:
                r = sortedIndex - 1
                
            else:
                break
        return nums[target]

            
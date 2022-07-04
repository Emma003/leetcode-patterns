def find(arr, l, r, key):
        if l>r:
            return -1
        
        mid = (l+r)//2
        
        if key == arr[mid]:
            return mid
        
        if key <arr[mid]:
            return find(arr, l, mid-1, key)
        else:
            return find(arr, mid+1, r, key)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return find(nums, 0, len(nums)-1, target)
        
    
        
def binSearch(arr, l, r, t):
    if l>r:
        return -1
    
    middle = (l+r)//2
    
    if arr[middle] == t:
        return middle
    
    if arr[middle] > t:
        return binSearch(arr, l, middle-1, t)
    else:
        return binSearch(arr, middle+1, r, t)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binSearch(nums, 0, len(nums)-1, target)
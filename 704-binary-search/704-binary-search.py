def binsearch(arr, l, r, t):
    if l>r:
        return -1

    mid = (l+r) // 2

    if arr[mid] == t:
        return mid

    if arr[mid] > t:
        return binsearch(arr, l, mid-1, t)

    else:
        return binsearch(arr, mid+1, r, t)


class Solution:
    def search(self, nums: List[int], target: int) -> int:    
        return binsearch(nums, 0, len(nums)-1, target)
    

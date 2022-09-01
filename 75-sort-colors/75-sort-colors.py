
def swap(arr, p1, p2):
    tmp = arr[p1]
    arr[p1] = arr[p2]
    arr[p2] = tmp

class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        curr, lo, hi = 0, 0 , len(arr)-1
        
        while curr <= hi:
            if arr[curr] == 0:
                swap(arr, curr, lo)
                lo += 1
                curr += 1
                
            elif arr[curr] == 2:
                swap(arr, curr, hi)
                hi -= 1
                
            else:
                curr += 1
            
            
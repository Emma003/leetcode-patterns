def getArea(arr, l,r):
    lVal = arr[l]
    rVal = arr[r]
    xDiff = r-l
    
    return min(lVal,rVal) * xDiff

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height)-1
        maxArea = 0
        
        while left<right:
            
            maxArea = max(maxArea, getArea(height,left,right))
            
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
                
        return maxArea
                
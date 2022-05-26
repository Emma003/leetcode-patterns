
def container_volume(x1, x2, y1, y2):
    return (x2-x1) * min(y1,y2)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_vol = 0
        
        while l<r:
            max_vol = max(max_vol, container_volume(l+1, r+1, height[l], height[r]))
            if height[l] < height[r]:
                l+=1
            else: 
                r-=1
        return max_vol
            
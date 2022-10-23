# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:



#[g,g,g,b,b,b]

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 1, n
        
        while l <= r:
            mid = (l+r)//2
            isBad = isBadVersion(mid)
            
            if isBad:
                #make sure its not the first bad
                if (mid==1) or ((mid-1) >=1 and not isBadVersion(mid-1)):
                    return mid
                r = mid - 1
                
            else: 
                l = mid + 1
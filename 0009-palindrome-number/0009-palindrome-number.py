class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNum = str(x)
        
        l, r = 0, len(strNum) -1
        
        while l <= r:
            if strNum[l] != strNum[r]:
                return False
            
            l += 1
            r -= 1
            
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1
        
        str = s.lower()
        
        while (l<=r):
            if not str[l].isalnum():
                l += 1
                continue
             
            if not str[r].isalnum():
                r -= 1
                continue
                
            if str[l] != str[r]:
                return False
                
            l += 1
            r -= 1
            
        return True
            
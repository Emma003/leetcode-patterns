class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = s.lower()
        
        left,right = 0, len(s)-1
        while left <= right: 
            l = str[left]
            r = str[right]
            
            if not l.isalnum():
                left += 1
                continue
            if not r.isalnum():
                right -= 1
                continue
            if l != r:
                return False
            left += 1
            right -= 1
        return True
        
        
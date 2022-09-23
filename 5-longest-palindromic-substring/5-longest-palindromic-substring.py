

        



class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLength = 0
        self.res = ""
        
        def helper(s,l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > self.maxLength:
                    self.maxLength = r-l+1
                    self.res = s[l:r+1]
                
                l -= 1
                r += 1
                
        for i in range(len(s)):
            #odd
            helper(s,i,i)
            
            #even
            helper(s,i,i+1)
            
        return self.res
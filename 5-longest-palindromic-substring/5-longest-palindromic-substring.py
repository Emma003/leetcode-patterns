class Solution:
    def longestPalindrome(self, s: str) -> str:
        #for each index, search outwards 
        #check even and odd
        self.maxWindowSize = 0
        self.res = ""
        
        def outwards(arr, l, r):
            while l >= 0 and r < len(arr) and arr[l] == arr[r]:
                if (r-l)+1 > self.maxWindowSize:
                    self.res = arr[l:r+1]
                    self.maxWindowSize = (r-l)+1
                    
                l -= 1
                r += 1
                
        
        for i in range(len(s)):
            #odd
            outwards(s, i, i)
            
            #even
            outwards(s, i, i+1)
                
        return self.res
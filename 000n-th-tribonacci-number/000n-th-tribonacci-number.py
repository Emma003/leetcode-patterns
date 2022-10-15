class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        
        def trib(n):
            if n in memo:
                return memo[n]
            
            memo[n] = trib(n-1) + trib(n-2) + trib(n-3)
            return memo[n]
        
        return trib(n)
        
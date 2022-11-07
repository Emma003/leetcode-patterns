'''
n = 1 -> 1


n = 2 -> 1 > 1
         2
         
         
n = 3 -> 1 > 1 > 1
         1 > 2
         2 > 1
         
n = 4 -> 1 > 1 > 1 > 1
         1 > 2 > 1
         2 > 1 > 1
         1 > 1 > 2
         2 > 2

                            6
                5                       4
        4               3       3               2
        

'''



class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        memo[1] = 1
        memo[2] = 2
        memo[3] = 3
        
        def recursive(n):
            if n in memo:
                return memo[n]
            
            memo[n] = recursive(n-1) + recursive(n-2)
            return memo[n]
        
        recursive(n)
        return memo[n]
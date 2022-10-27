class Solution:
    def isHappy(self, n: int) -> bool:
        
        def squareSum(n):
            sum = 0
            
            while n > 0:
                lastDigit = n % 10
                n //= 10
                sum += lastDigit * lastDigit
                
            return sum
        
        fast, slow = n, n
        
        while fast != 1:
            fast = squareSum(squareSum(fast))
            slow = squareSum(slow)
            
            if fast == 1:
                break
            
            if fast == slow:
                return False
            
        return True
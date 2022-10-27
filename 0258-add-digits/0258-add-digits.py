
def digitSum(n):
    sum = 0
    
    while n > 0:
        lastDigit = n % 10
        sum += lastDigit
        n //= 10
    return sum

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        
        return self.addDigits(digitSum(num))
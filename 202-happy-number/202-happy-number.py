def sqSum(num):
    sum = 0
    while num > 0:
        c = num % 10
        sum += c*c
        num //= 10
    return sum

class Solution:
    def isHappy(self, n: int) -> bool:
        fast = slow = n
        while True:
            fast = sqSum(sqSum(fast))
            slow = sqSum(slow)
            if slow == fast:
                break
        return slow == 1
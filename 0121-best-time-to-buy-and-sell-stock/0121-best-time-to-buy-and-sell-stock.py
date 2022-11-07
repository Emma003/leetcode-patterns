# [7,1,5,3,0,4]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0
        
        for sell in range(len(prices)):
            currProfit = prices[sell] - prices[buy]
            
            if currProfit < 0:
                buy = sell
                
            profit = max(profit, currProfit)
            
        return profit
        
        
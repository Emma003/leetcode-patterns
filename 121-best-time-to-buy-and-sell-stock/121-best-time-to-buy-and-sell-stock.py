# [7,1,5,3,0,4]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit, buy = 0, 0
        
        for sell in range(1, len(prices), 1):
            currProfit = prices[sell] - prices[buy]
            
            if currProfit <= 0:
                buy = sell
                continue
                
            maxProfit = max(maxProfit, currProfit)
            
        return maxProfit
        
        
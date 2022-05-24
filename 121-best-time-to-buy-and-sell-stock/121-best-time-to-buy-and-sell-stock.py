class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, curr_profit, max_profit = 0, 0, 0
        
        for end in range(1, len(prices)):
            right = prices[end]
            left = prices[start]       
            curr_profit = right - left 
            
            if curr_profit < 0:
                start = end
            max_profit = max(max_profit, curr_profit)
            
        return max_profit
                
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 100
        max_profit = 0
        for i in prices:
            buy = min(i,buy)
            p = i-buy
            max_profit = max(max_profit,p)
        return max_profit
        
            
            



            


        
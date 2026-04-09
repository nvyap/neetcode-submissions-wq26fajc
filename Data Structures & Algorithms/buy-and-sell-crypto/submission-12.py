class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        sell = len(prices)-1
        while buy < sell:
            for sell in range(buy+1,len(prices),1):
                p = prices[sell]-prices[buy]
                max_profit = max(max_profit,p)
            buy += 1
        return max_profit
            
            



            


        
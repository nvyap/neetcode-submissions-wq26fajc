class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        buy = 100
        for i in prices:
            buy = min(i,buy)
            p = i-buy
            max_profit = max(p,max_profit)
        return max_profit
            


        
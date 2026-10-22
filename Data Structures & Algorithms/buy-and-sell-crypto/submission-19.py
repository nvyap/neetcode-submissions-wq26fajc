class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 100
        profit = 0
        for i in prices:
            buy = min(buy,i)
            p = i-buy
            profit = max(profit,p)
        return profit



        
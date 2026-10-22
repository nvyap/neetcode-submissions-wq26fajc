class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 100
        max_profit = 0
        for i in prices:
            buy = min(buy,i)
            p = i-buy
            max_profit = max(p,max_profit)
        return max_profit
        
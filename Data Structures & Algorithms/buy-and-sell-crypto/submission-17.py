class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 100

        for i in prices:
            buy = min(i,buy)
            p = i-buy
            max_profit = max(max_profit,p)
        return max_profit
        
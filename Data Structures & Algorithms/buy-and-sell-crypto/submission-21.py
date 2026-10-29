class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left,right = 0, len(prices)-1
        buy = prices[0]
        for i in prices:
            buy = min(buy,i)
            profit = i-buy
            max_profit = max(max_profit,profit)
        return max_profit

        
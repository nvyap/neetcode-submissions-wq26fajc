class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        maxP = 0
        for sell in prices:
            maxP = max(maxP,sell-min_buy)
            min_buy = min(sell,min_buy)
        return maxP
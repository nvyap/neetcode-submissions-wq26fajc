class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        if len(prices)<2:
            return 0
        for i in range(len(prices)):
            for j in range(len(prices)-1,i,-1):
                profit.append(prices[j]-prices[i])
        if max(profit)>0:
            return max(profit)
        return 0
            
            
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        max_profit=0
        min_prices=prices[0]
        for i in range(1,len(prices)):
            min_prices=min(min_prices,prices[i])
            profit=prices[i]-min_prices

            max_profit=max(max_profit,profit)
        return max_profit
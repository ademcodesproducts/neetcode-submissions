class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        for i in range(len(prices)):
            if i > 0 and prices[i] - prices[i - 1] > 0:
                diff = prices[i] - prices[i - 1]
                total_profit += diff
        return total_profit
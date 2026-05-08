class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value, min_value = 0, prices[0]

        for sell_price in prices:
            max_value = max(max_value, sell_price - min_value)
            min_value = min(min_value, sell_price)
        return max_value
            

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = 0
        pointer = 1
        max_profit = 0

        while pointer < len(prices):

            if prices[pointer] < prices[min_buy]:
                min_buy = pointer

            max_profit = max(max_profit, prices[pointer] - prices[min_buy])
            pointer += 1

        return max_profit
            

        
            

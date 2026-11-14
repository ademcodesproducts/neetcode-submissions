class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]
            
            memo[amount] = 1e9
            for c in coins:
                if amount - c >= 0:
                    memo[amount] = min(memo[amount], 1 + dfs(amount - c))
            return memo[amount]

        return dfs(amount) if dfs(amount) < 1e9 else -1
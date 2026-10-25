class Solution:
    def climbStairs(self, n: int) -> int:
        prev, all_prevs = 1, 1

        for _ in range(n - 1):
            temp = prev
            prev = prev + all_prevs
            all_prevs = temp
            
        return prev
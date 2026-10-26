class Solution:
    def longestPalindrome(self, s: str) -> str:
        reset_idx, reset_len = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

                if dp[i][j] and length > reset_len:
                    reset_idx = i
                    reset_len = length

        return s[reset_idx : reset_idx + reset_len]  
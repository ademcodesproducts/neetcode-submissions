class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = True
                    count += 1
                elif length == 2:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        count += 1
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                    if dp[i][j]:
                        count += 1
        return count
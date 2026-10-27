class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        total_1 = s.count("1")

        count_0, count_1 = 0, 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                count_0 += 1
            if s[i] == "1":
                total_1 -= 1

            max_score = max(max_score, count_0 + total_1)
            
        return max_score
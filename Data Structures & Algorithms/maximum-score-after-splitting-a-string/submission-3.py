class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        counts = {}
        for c in s:
            counts[c] = 1 + counts.get(c, 0)

        count_0, count_1 = 0, 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                count_0 += 1
            if s[i] == "1":
                counts[s[i]] -= 1

            max_score = max(max_score, count_0 + counts.get("1", 0))
            
        return max_score
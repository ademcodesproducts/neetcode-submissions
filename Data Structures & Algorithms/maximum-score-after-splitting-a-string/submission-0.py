class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            count_0, count_1 = 0, 0
            for c in left:
                if c == "0":
                    count_0 += 1
            
            for c in right:
                if c == "1":
                    count_1 += 1
            
            max_score = max(max_score, count_0 + count_1)
    
        return max_score
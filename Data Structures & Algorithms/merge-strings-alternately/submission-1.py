class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for c1, c2 in zip(word1, word2):
            merged.extend([c1, c2])
        
        start = min(len(word1), len(word2))
        end = max(len(word1), len(word2))

        for i in range(start, end):
            if len(word2) > len(word1):
                merged.append(word2[i])
            else:
                merged.append(word1[i])

        return "".join(merged) 
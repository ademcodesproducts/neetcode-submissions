class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        freq = {}
        for c in pattern:
            freq[c] = 1 + freq.get(c, 0)
        
        words = s.split()

        count = {}
        for w in words:
            count[w] = 1 + count.get(w, 0)
        
        return sorted(count.values()) == sorted(freq.values())
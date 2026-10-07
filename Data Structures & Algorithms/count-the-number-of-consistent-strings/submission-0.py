class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent = 0
        for w in words:
            length = 0
            for c in w:
                if c not in allowed:
                    break
                length += 1
            if length == len(w):
                consistent += 1
            
        return consistent
        
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for c in ransomNote:
            mag[c] -= 1
            ransom[c] -= 1
            if mag[c] < 0:
                return False
        return True
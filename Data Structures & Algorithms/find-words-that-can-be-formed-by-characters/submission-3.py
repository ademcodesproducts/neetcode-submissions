class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        available = Counter(chars)
        length = 0

        for w in words:
            need = Counter(w)
            if all(need[c] <= available[c] for c in need):
                length += len(w)
        return length
            
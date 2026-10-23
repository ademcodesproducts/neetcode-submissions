class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_string_length = 0
        freq = {}
        l = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            max_freq = max(freq.values())

            while r - l  + 1 - max_freq> k:
                freq[s[l]] -= 1
                l += 1

            max_string_length = max(max_string_length, r - l + 1)

        return max_string_length
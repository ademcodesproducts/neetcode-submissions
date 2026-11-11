class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        longest_substring, max_freq = 0, 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0) 
            max_freq = max(max_freq, freq[s[r]])
            while r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            longest_substring = max(longest_substring, r - l + 1)
        return longest_substring if len(s) > 0 else 0
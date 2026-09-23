class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l = 0
        substring_len = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            
            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1

            substring_len = max(substring_len, r - l + 1)

        return substring_len
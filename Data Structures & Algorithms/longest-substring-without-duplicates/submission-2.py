class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, max_len, seen = 0, 0, set()

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            max_len = max(max_len, i - l + 1)
        return max_len
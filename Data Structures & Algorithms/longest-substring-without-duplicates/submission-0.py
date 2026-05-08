class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = set()
        l, max_len = 0, 0

        for right in range(len(s)):
            while s[right] in dup:
                dup.remove(s[l])
                l += 1
            dup.add(s[right])
            max_len = max(max_len, right - l + 1)
        return max_len
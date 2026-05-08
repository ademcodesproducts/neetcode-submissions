class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, max_freq, length = 0, 0, 0, 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_freq = max(max_freq, count[s[right]])
            while right - left + 1 - max_freq > k:
                count[s[left]] -= 1
                left += 1
        length = right - left + 1
        return length

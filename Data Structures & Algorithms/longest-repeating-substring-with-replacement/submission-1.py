class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        state = {}
        longest_substring = 0
        
        for r in range(len(s)):
            state[s[r]] = 1 + state.get(s[r], 0)
            max_freq = max(state.values())

            while (r - l + 1) - max_freq > k:
                state[s[l]] -= 1
                l += 1

            longest_substring = max(longest_substring, r - l + 1)

        return longest_substring
        
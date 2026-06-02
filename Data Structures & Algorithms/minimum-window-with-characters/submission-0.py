class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count, window = {}, {}
        l = 0

        for r in range(len(t)):
            count[t[r]] = 1 + count.get(t[r], 0)

        have, need = 0, len(count)
        res, res_len = [-1, -1], float('inf')

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            while have == need:
                window_len = r - l + 1
                if window_len < res_len:
                    res = [l, r]
                    res_len = window_len
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r + 1]
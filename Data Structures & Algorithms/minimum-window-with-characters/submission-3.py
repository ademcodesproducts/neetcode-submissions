from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        l = 0
        min_idx, max_idx = 0, 0
        sCount = {}
        tCount = Counter(t)
        have, need = 0, len(tCount)
        found = False

        for r in range(len(s)):
            if s[r] in t:
                sCount[s[r]] = 1 + sCount.get(s[r], 0)

                if sCount[s[r]] == tCount[s[r]]:
                    have += 1

            while have == need:
                if (
                    max_idx == 0
                    and min_idx == 0
                    or r - l + 1 == min(max_idx - min_idx + 1, r - l + 1)
                ):
                    min_idx, max_idx = l, r
                    found = True
                if s[l] in tCount:
                    sCount[s[l]] -= 1
                    if sCount[s[l]] < tCount[s[l]]:
                        have -= 1

                l += 1

        return s[min_idx : max_idx + 1] if found else ""

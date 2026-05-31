class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count, window = {}, {}
        l = 0

        for r in range(len(s1)):
            count[s1[r]] = 1 + count.get(s1[r], 0)

        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    window.pop(s2[l])
                l += 1

            if window == count:
                return True
        return False
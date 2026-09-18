class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        s, t are isomorphic if characters in s can be replaced to get t.
        - preserve order of character
        - no two character map to same character
        - character -> same chracter mapping allowed

        at each iteration step is the chracter thats mapped from s to t
        same character as it was mapped previously
        """
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for s, t in zip(s, t):
            if s in s_to_t and s_to_t[s] != t:
                return False
            if t in t_to_s and t_to_s[t] != s:
                return False

            s_to_t[s] = t
            t_to_s[t] = s

        return True
        
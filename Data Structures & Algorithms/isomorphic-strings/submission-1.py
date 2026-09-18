class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        s, t are isomorphic if characters in s can be replaced to get t.
        - preserve order
        - no two characters in s can map to the same character in t
        - the same character in s must always map to the same character in t

        At each iteration, check that:
        1. If s-character was mapped before, it maps to the same t-character.
        2. If t-character was mapped before, it maps to the same s-character.

        The two hashmaps enforce a one-to-one mapping.
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
        
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        def check_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True  

        while l <= r:
            if s[l] != s[r]:
                return check_palindrome(l, r - 1) or check_palindrome(l + 1, r)
            l += 1
            r -= 1
        return True  
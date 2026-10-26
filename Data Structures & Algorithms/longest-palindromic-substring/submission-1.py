class Solution:
    def longestPalindrome(self, s: str) -> str:
        # start from the middle, since we want the longest possible palindrome
        # different while loops for odd and even length
        longest_palindrome = 0
        reset_idx = 0

        def find_palindrome(l , r):
            nonlocal longest_palindrome
            nonlocal reset_idx

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > longest_palindrome:
                    reset_idx = l
                    longest_palindrome = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd
            find_palindrome(i, i)
            # even
            find_palindrome(i, i + 1)

        return s[reset_idx : reset_idx + longest_palindrome]
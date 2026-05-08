class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(c.lower() for c in s if c.isalnum())

        return word == word[::-1]

            


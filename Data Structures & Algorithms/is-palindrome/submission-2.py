class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(word) - 1

        while l < r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
            
        return True





        

            


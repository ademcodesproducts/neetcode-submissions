class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def palindrome(text):
            l, r = 0, len(text) - 1
            while l < r:
                if text[l] != text[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(idx, path):
            if idx == len(s):
                result.append(path[::])
                return

            for i in range(idx, len(s)):
                sliced = s[idx:i+1]
                if palindrome(sliced):
                    path.append(sliced)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return result
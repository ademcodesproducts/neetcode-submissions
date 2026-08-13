class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(idx, path):
            if not digits:
                return []
                
            if idx == len(digits):
                comb = "".join(path)
                result.append(comb[:])
                return
                             
            char = digit_map[digits[idx]]
            for c in char:
                path.append(c)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])
        return result
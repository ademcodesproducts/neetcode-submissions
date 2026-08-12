class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(idx, path):
            if idx == len(s):
                result.append(path[::])
                return

            for i in range(idx, len(s)):
                sliced = s[idx:i+1]
                if sliced == sliced[::-1]:
                    path.append(sliced)
                    backtrack(i + 1, path)
                    path.pop()

        backtrack(0, [])
        return result
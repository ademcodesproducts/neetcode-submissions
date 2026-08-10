class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path, open_cnt, close_cnt):
            if open_cnt + close_cnt == 2 * n:
                path = "".join(path)
                result.append(path[:])
                return

            if open_cnt < n:
                path.append("(")
                backtrack(path, open_cnt + 1, close_cnt)
                path.pop()

            if close_cnt < open_cnt:
                path.append(")")
                backtrack(path, open_cnt, close_cnt + 1)
                path.pop()
        
        backtrack([], 0, 0)
        return result
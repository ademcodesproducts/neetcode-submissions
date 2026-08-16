class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]
        col, main_diag, sec_diag = set(), set(), set()

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            for c in range(n):
                if c in col or (r - c) in main_diag or (r + c) in sec_diag: 
                    continue
            
                col.add(c)
                main_diag.add(r - c)
                sec_diag.add(r + c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                main_diag.remove(r - c)
                sec_diag.remove(r + c)
                board[r][c] = "."

        backtrack(0)
        return result
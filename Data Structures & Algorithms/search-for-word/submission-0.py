class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        len_row, len_col = len(board), len(board[0])
        visited = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= len_row or c >= len_col or board[r][c] != word[i] or (r, c) in visited:
                return False

            visited.add((r, c))

            match = (backtrack(r + 1, c, i + 1) or
            backtrack(r - 1, c, i + 1) or 
            backtrack(r, c + 1, i + 1) or
            backtrack(r, c - 1, i + 1))

            visited.remove((r, c))
            return match
        
        for r in range(len_row):
            for c in range(len_col):
                if backtrack(r, c, 0):
                    return True
        return False
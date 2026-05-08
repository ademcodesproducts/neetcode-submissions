class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_box = [set() for box in range(9)]

        for i in range(len(board)):
            seen_row, seen_col = set(), set()
            for j in range(len(board[0])):

                if board[i][j] != '.':
                    if board[i][j] in seen_row:
                        return False
                    seen_row.add(board[i][j]) 

                if board[j][i] != '.':
                    if board[j][i] in seen_col:
                        return False
                    seen_col.add(board[j][i])

                box_idx = (i // 3) * 3 + j // 3
                if board[i][j] != '.':
                    if board[i][j] in seen_box[box_idx]:
                        return False
                    seen_box[box_idx].add(board[i][j])

        return True
        
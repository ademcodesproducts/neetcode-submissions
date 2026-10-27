class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # lucky = minimum in row and maximum in column
        res = []

        for i in range(len(matrix)):
            min_col_idx = 0
            for c in range(len(matrix[0])):
                if matrix[i][c] < matrix[i][min_col_idx]:
                    min_col_idx = c

            max_row_idx = 0
            for r in range(len(matrix)):
                if matrix[r][min_col_idx] > matrix[max_row_idx][min_col_idx]:
                    max_row_idx = r

            if max_row_idx == i:
                res.append(matrix[i][min_col_idx])

        return res
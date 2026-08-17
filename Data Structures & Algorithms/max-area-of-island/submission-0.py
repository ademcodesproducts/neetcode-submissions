class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        len_row, len_col = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0 or r >= len_row or
                c < 0 or c >= len_col or
                (r, c) in visited or
                grid[r][c] == 0
            ):
                return 0

            visited.add((r, c))
            area = 1

            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area

        for r in range(len_row):
            for c in range(len_col):
                area = dfs(r, c)
                max_area = max(max_area, area)
                
        return max_area
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        len_row, len_col = len(grid), len(grid[0])
        visited = set()
        island_cnt = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len_row or c >= len_col or (r, c) in visited or grid[r][c] == "0":
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(len_row):
            for c in range(len_col):
                if (r, c) not in visited and grid[r][c] == "1":
                    island_cnt += 1
                    dfs(r, c)
        return island_cnt 
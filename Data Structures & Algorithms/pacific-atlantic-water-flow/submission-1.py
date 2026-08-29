class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific, atlantic = set(), set()

        def dfs(r, c, ocean):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in ocean:
                return            
                            
            ocean.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, ocean)

        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS - 1, atlantic)
            
        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS - 1, c, atlantic)

        return list(pacific & atlantic)
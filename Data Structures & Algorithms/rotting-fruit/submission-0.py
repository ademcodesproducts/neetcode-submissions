class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0

        def travelGrid(r, c):
            nonlocal fresh
            
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == 0 or grid[r][c] == 2):
                return
            grid[r][c] = 2
            q.append((r, c))
            fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                travelGrid(r + 1, c)
                travelGrid(r - 1, c)
                travelGrid(r, c + 1)
                travelGrid(r, c - 1)

            time += 1
        return time if fresh == 0 else -1
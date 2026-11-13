class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh, time = 0, 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Initialization
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft() # we pop the two we're currently at
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0 or grid[nr][nc] == 2: # skip also if we go to a two
                        continue
                    if grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1
                
        return time if fresh == 0 else -1

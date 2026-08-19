class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        visited = set()
        q = deque()

        def travelGrid(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == -1 or
                (r, c) in visited):
                return
            visited.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        distance = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance

                travelGrid(r + 1, c)
                travelGrid(r - 1, c)
                travelGrid(r, c + 1)
                travelGrid(r, c - 1)

            distance += 1
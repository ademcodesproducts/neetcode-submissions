class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
        r, c = 0, 0
        visited = set()
        visited.add((r, c))

        for p in path:
            nr, nc = directions[p]
            r, c = r + nr, c + nc
            if (r, c) in visited:
                return True
            visited.add((r, c))
        return False
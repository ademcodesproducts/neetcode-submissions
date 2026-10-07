class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        r, c = 0, 0

        for p in path:
            visited.add((r, c))

            if p == "N":
                c += 1
            elif p == "S":
                c -= 1
            elif p == "E":
                r += 1
            else:
                r -= 1

            if (r, c) in visited:
                return True

        return False

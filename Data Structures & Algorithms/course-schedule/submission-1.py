class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        adj = defaultdict(list)
        for node, preq in prerequisites:
            adj[node].append(preq)

        def dfs(node):
            if node in visited:
                return False
            if adj[node] == []:
                return True

            visited.add(node)
            for preq in adj[node]:
                if not dfs(preq):
                    return False
            visited.remove(node)
            adj[node] = []
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
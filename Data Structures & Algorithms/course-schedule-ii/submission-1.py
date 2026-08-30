class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting, visited, order = set(), set(), []
        adj = defaultdict(list)

        for node, preq in prerequisites:
            adj[node].append(preq)
        
        def dfs(node):
            if node in visiting:
                return False

            if node in visited:
                return True

            visiting.add(node)

            for preq in adj[node]:
                if not dfs(preq):
                    return False

            visiting.remove(node)
            visited.add(node)
            order.append(node)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order
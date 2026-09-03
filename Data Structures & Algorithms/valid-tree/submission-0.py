class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = set()
        adj = defaultdict(list)
        for node, edge in edges:
            adj[edge].append(node)
            adj[node].append(edge)
        
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        dfs(0, -1)
        return len(visited) == n
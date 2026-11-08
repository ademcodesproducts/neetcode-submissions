class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((t, v))

        pq = [(0, k)]
        visited = set()
        min_time = 0

        while pq:
            time, nei = heapq.heappop(pq)
            if nei in visited:
                continue
            visited.add(nei)
            min_time = time

            for t, v in graph[nei]:
                if v not in visited:
                    heapq.heappush(pq, (min_time + t, v))
    
        return min_time if len(visited) == n else -1 
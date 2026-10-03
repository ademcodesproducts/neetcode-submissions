class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def euclidean_distance(x, y):
            return math.sqrt(x**2 + y**2)

        max_heap = []

        for p in points:
            distance = -euclidean_distance(p[0], p[1])
            heapq.heappush(max_heap, (distance, p))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
            
        res = []
        while max_heap:
            _, p = heapq.heappop(max_heap)
            res.append(p)
            
        return res 
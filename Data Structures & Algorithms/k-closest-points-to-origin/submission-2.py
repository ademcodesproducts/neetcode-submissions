class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def euclidean_distance(x, y):
            return math.sqrt(x**2 + y**2)

        min_heap = []
        res = []

        for p in points:
            distance = euclidean_distance(p[0], p[1])
            heapq.heappush(min_heap, (distance, p))

        for _ in range(k):
            distance, p = heapq.heappop(min_heap)
            res.append(p)

        return res
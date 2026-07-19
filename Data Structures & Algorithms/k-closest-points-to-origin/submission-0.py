class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_distance(x, y):
            return math.sqrt(x**2 + y**2)

        heap = []
        for x, y in points:
            dis = -euclidean_distance(x,y)
            heap.append((dis, [x, y]))
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        return [point for _, point in heap]
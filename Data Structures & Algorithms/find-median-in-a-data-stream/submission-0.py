class MedianFinder:

    def __init__(self):
        self.max_heap = []   
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        if self.max_heap and self.min_heap:
            if -self.max_heap[0] > self.min_heap[0]:
                x = -heapq.heappop(self.max_heap)
                y = heapq.heappop(self.min_heap)

                heapq.heappush(self.max_heap, -y)
                heapq.heappush(self.min_heap, x)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return float((-self.max_heap[0] + self.min_heap[0]) / 2)
        else:
            return float(-self.max_heap[0])
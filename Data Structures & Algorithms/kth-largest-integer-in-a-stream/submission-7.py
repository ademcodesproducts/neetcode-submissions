class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.min_heap = []
        self.nums.append(val)
        for n in self.nums:
            heapq.heappush(self.min_heap, n)
            while len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]
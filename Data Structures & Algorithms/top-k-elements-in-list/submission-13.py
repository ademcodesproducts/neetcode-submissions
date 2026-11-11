class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0) # num as key, count as value

        min_heap = []
        for n, c in freq.items():
            heapq.heappush(min_heap, (c, n))
            while len(min_heap) > k:
                _ = heapq.heappop(min_heap)

        return [min_heap[i][1] for i in range(len(min_heap))]
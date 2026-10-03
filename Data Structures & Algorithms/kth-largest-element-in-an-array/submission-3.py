class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        i = 0
        while i < k - 1:
            _ = heapq.heappop(max_heap)
            i += 1
        return -max_heap[0]
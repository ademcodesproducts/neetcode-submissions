class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 1000000007
        min_heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(min_heap)

        total = 0
        for i in range(right):
            val, idx = heapq.heappop(min_heap)

            if i >= left - 1:
                total += val

            if idx + 1 < n:
                new_sum = val + nums[idx + 1]
                heapq.heappush(min_heap, (new_sum, idx + 1))

        return total % mod
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 1000000007
        res = []
        min_heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(min_heap)

        curr_sum = 0
        while min_heap:
            val, idx = heapq.heappop(min_heap)
            res.append(val)
            if idx + 1 < n:
                curr_sum = val + nums[idx + 1]
                heapq.heappush(min_heap, (curr_sum, idx + 1))
        
        res.sort()
        return sum(res[left - 1:right]) % mod
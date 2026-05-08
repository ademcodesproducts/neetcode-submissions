class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        sorted_idx = sorted(count, key=lambda num: count[num], reverse=True)
        return sorted_idx[:k]
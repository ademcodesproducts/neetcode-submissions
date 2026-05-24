class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        min_k = 0
        
        while left <= right:
            mid = (left + right) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / mid)
            if total_time <= h:
                min_k = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_k
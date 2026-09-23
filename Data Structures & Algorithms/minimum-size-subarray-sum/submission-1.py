class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        min_sum = float("inf")

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_sum = min(min_sum, r - l + 1)
                curr_sum -= nums[l]
                l += 1

        return min_sum if min_sum != float("inf") else 0
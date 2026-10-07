class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = inc = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += nums[i]
            else:
                inc = nums[i]
            best = max(best, inc)
        return best 
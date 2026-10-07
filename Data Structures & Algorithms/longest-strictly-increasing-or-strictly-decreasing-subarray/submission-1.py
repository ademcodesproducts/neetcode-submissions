class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_increasing_len = 1
        max_decreasing_len = 1

        curr_increasing_len = 1
        for i in range(1, len(nums)):
            curr_increasing_len += 1
            if nums[i - 1] >= nums[i]:
                curr_increasing_len = 1
            max_increasing_len = max(max_increasing_len, curr_increasing_len)

        curr_decreasing_len = 1
        for i in range(1, len(nums)):
            curr_decreasing_len += 1
            if nums[i - 1] <= nums[i]:
                curr_decreasing_len = 1
            max_decreasing_len = max(max_decreasing_len, curr_decreasing_len)

        return max(max_decreasing_len, max_increasing_len)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def find_max_money(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                skip = dp[i - 1]
                rob = dp[i - 2] + nums[i]
                dp[i] = max(skip, rob)
            
            return dp[-1]

        return max(find_max_money(nums[1:]), find_max_money(nums[:-1]))
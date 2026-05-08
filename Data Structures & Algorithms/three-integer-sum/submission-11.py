class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum == 0:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1

                if three_sum < 0:
                    l += 1
                if three_sum > 0:
                    r -= 1

        return list(res)            
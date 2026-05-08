class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        for i in range(len(nums)):
            prev_map = {}
            for j in range(i+1, len(nums)):
                diff = 0 - nums[i] - nums[j]
                if diff in prev_map:
                    result.add(tuple(sorted([nums[i], nums[j], diff])))
                prev_map[nums[j]] = j

        return [list(l) for l in result]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in seen_map:
                return [seen_map[diff], i]
            seen_map[val] = i
        return []


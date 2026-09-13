class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums cannot be empty -> no edge case check 
        seen = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [seen[complement], i]
            seen[x] = i
        return []            
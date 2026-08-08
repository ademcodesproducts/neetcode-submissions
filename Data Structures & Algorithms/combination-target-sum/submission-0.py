class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(initial, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(initial, len(nums)):
                path.append(nums[i])
                backtrack(i, path, total + nums[i])
                path.pop()

        backtrack(0, [], 0)
        return result
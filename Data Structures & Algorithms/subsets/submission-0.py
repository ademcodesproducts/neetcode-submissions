class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(i, path):
            if i == len(nums):
                result.append(path[:])
                return

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            backtrack(i + 1, path)
 
        backtrack(0, [])
        return result
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start_idx, path):
            if start_idx == len(nums):
                result.append(path[:])
                return
                
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(start_idx + 1, path)
                path.pop()
            
        backtrack(0, [])
        return result
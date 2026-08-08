class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start_idx, path, total):
            if total == target:
                result.append(path[:]) #check why
                return
            if total > target:
                return

            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return result
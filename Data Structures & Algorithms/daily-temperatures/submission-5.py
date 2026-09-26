class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, x in enumerate(temperatures):
            while stack and x > stack[-1][1]:
                prev_idx, prev_val = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append((i, x))

        return result
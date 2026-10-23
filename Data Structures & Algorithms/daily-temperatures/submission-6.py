class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, tem in enumerate(temperatures):
            while stack and stack[-1][1] < tem:
                idx, _ = stack.pop()
                result[idx] = i - idx
            stack.append((i, tem))
        return result
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            h1 = heights[i]
            for j in range(i + 1, len(heights)):
                h2 = heights[j]
                h = min(h1, h2)
                w = j - i
                max_area = max(max_area, w * h)
        return max_area
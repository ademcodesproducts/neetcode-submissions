class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(len(heights)):
            h = heights[i]

            right = i + 1
            while right < len(heights) and h <= heights[right]:
                right += 1

            left = i - 1
            while left >= 0 and h <= heights[left]:
                left -= 1

            w = right - left - 1
            max_area = max(max_area, w * h)
            
        return max_area
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        n = len(heights)
        max_area = 0
        stack = []

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area
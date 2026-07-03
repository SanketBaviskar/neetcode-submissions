class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, max_area = [], 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                height = heights[stack.pop()]
                prev_smaller = stack[-1] if stack else -1
                next_smaller = i
                width = next_smaller - prev_smaller - 1
                area = height * width
                max_area = max(max_area, area)
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            prev_smaller = stack[-1] if stack else -1
            next_smaller = len(heights)
            width = next_smaller - prev_smaller - 1
            area = width * height
            max_area = max(max_area, area)
        return max_area
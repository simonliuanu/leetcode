class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        ans = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                top = stack.pop()
                width = (i - 1) - (stack[-1] + 1) + 1
                area = width * heights[top]
                ans = max(ans, area)
            stack.append(i)

        return ans

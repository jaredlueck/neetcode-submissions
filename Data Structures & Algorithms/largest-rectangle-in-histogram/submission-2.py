class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n+1):
            while stack and (i == n or heights[stack[-1]] > heights[i]):
                # if the next bar is lower than the one at the top of the stack,
                # then we have found the right boundary
                h = heights[stack.pop()]
                # left boundary would be the next element of the stack
                # since it is monotonically increasing
                prev = -1 if not stack else stack[-1]
                area = (i - prev - 1) * h
                max_area = max(max_area, area)
            stack.append(i)
        return max_area


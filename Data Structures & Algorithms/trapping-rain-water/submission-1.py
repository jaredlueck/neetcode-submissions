class Solution:
    def trap(self, height: List[int]) -> int:
        heights = height
        max_l = [0] * len(heights)
        max_l[0] = heights[0]
        for i in range(1, len(height)):
            max_l[i] = max(max_l[i-1], heights[i])
        max_r = [0] * len(heights)
        max_r[len(heights)-1] = heights[len(height)-1]
        for i in range(len(heights)-2, -1, -1):
            max_r[i] = max(max_r[i+1], heights[i])
        print(max_l)
        print(max_r)

        total = 0

        for i in range(1, len(heights)-1):
            total += max(min(max_l[i-1], max_r[i+1]) - heights[i], 0)
        return total
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # find i, j to maximize:
        #    min(heights[i], heights[j]) * abs((i - j))
        l, r = 0, len(heights)-1
        res = 0
        while l < r:
            print(l, r)
            height = min(heights[l], heights[r])
            length = r - l
            res = max(res, length * height)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return res
        
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_l = 0
        max_r = 0
        total = 0
        while l <= r:
            # l is limiting
            if max_r >= max_l:
                total += max(max_l - height[l], 0)
                max_l = max(max_l, height[l])
                l += 1
            else:
                total += max(max_r - height[r], 0)
                max_r = max(max_r, height[r])
                r -= 1
        return total
            
            


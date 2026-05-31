class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            print((l, r))
            if nums[l] <= nums[r]:
                return nums[l]
            m = (l + r) // 2
            # array has been rotated so smaller should be to the right
            if nums[m] >= nums[r]:
                l = m + 1
            # array is rotated so smaller a
            else:
                r = m
        return nums[r]
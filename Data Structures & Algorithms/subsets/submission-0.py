class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr, index, nums):
            print(curr)
            nonlocal res
            res.append(curr)
            if index >= len(nums):
                return

            for i in range(index + 1, len(nums)):
                backtrack(curr + [nums[i]], i, nums)
        backtrack([], -1, nums)
        return res
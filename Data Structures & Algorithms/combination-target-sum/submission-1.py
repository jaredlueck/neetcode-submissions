class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(curr_val, curr_sum, index):
            nonlocal res, target
            if curr_sum == target:
                res.append(curr_val.copy())
                return
            elif curr_sum > target:
                return
            else:
                for i in range(index, len(nums)):
                    num = nums[i]
                    curr_val.append(num)
                    backtrack(curr_val + [], curr_sum + num, i)
                    curr_val.pop()
        backtrack([], 0, 0)
        return res
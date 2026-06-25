class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(curr, curr_sum, index):
            if curr_sum == target:
                res.append(curr.copy())
                return
            elif curr_sum > target:
                return
            else:
                for i in range(index, len(candidates)):
                    # prevent duplicates by not adding the same number again
                    # if we already visited it from this index
                    if i > index and candidates[i] == candidates[i-1]:
                        continue
                    curr.append(candidates[i])
                    backtrack(curr, curr_sum + candidates[i], i+1)
                    curr.pop()
        backtrack([], 0, 0)
        return res

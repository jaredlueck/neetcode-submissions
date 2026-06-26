class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, rem):
            if not rem:
                res.append(curr.copy())
                return
            
            for i in range(len(rem)):
                next_val = rem.pop(i)
                curr.append(next_val)
                backtrack(curr, rem)
                curr.pop()
                rem.insert(i, next_val)
        
        backtrack([], nums)
        return res



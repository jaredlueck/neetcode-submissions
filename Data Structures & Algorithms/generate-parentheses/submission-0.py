class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, opened, closed):
            nonlocal res, n
            print((curr, opened, closed, n))
            # no more paranthesis left
            if opened == closed == n:
                res.append(curr)
                return
            else:
                # we can always place another opening paranthesis if we have more left
                if opened < n:
                    backtrack(curr + "(", opened + 1, closed)
                # can only place a closing paranthesis if there is at least one unclosed opening
                # paranthesis
                if opened > closed:
                    backtrack(curr + ")", opened, closed + 1)
        backtrack("", 0, 0)
        return res
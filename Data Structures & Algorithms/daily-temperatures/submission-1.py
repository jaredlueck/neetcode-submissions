class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stackTemp, ind = stack.pop()
                res[ind] = i - ind
            stack.append((temp, i))
        return res
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        i = n - 1
        res = [0] * n
        warmest = float('-inf')
        while i >= 0:
            temp = temperatures[i]
            if warmest <= temp: 
                stack.append((temp, i))
                warmest = temp
                i -= 1
                continue
            while stack and stack[-1][0] <= temp:
                stack.pop()
            res[i] = stack[-1][1] - i
            stack.append((temp, i))
            
            print(stack)
            print(res)
            i -= 1

        return res
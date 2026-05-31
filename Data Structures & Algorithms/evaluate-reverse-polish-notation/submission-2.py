class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i, n in enumerate(tokens):
            if n in "+-/*":
                print(n)
                print(stack)
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                
                if n == "-":
                    res = operand_1 - operand_2
                if n == "+":
                    res = operand_1 + operand_2
                if n == "*":
                    res = operand_1 * operand_2
                if n == "/":
                    res = int(operand_1 / operand_2)
                print(res)
                stack.append(res)
            else:
                stack.append(int(n))
        return stack[0]

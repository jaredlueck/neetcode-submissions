class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = []
        for i, c in enumerate(s):
            if c in ['(', '[', '{']:
                stack.append(c)
                continue

            if len(stack) == 0: return False
            
            prev = stack.pop()

            if c == ")" and prev != "(" or c == "]" and prev != "[" or c == "}" and prev != "{":
                return False
        return len(stack) == 0
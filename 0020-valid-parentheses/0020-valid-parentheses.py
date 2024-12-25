class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = True
        for char in s:
            if char == ')':
                if (not stack):
                    return False
                if (stack.pop() != '('):
                    return False
            elif char == ']':
                if (not stack):
                    return False
                if (stack.pop() != '['):
                    return False
            elif char == '}':
                if (not stack):
                    return False
                if (stack.pop() != '{'):
                    return False
            else:
                stack.append(char)
        return not stack
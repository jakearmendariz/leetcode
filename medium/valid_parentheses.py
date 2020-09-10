class Solution:
    def isValid(self, s: str) -> bool:
        paren = bracket = curly = 0
        open = ['{', '(', '[']
        close = ['}', ')', ']']
        
        stack = []
        for i in list(s):
            if i in open:
                stack.append(i)
            elif i in close:
                if len(stack) == 0:
                    return False
                elif open.index(stack.pop()) is not close.index(i):
                    return False
        return len(stack) == 0
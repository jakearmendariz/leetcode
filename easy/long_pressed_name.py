class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        j = 0
        if len(name) > len(typed):
            return False
        for i, c in enumerate(name):
            if j >= len(typed) or typed[j] is not c:
                return False
            if i < len(name) -1:
                if c == name[i+1]:
                    j+=1
                    continue
            while(j < len(typed) and typed[j] is c):
                j += 1
        print('len check', j)
        if j == len(typed) -1:
            return typed[-1] == name[-1]
        return j >= len(typed) -1
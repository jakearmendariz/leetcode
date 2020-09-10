class Solution(object):
     def isMatch(self, text, pattern):
        memory = {}
        def dp(i,j):
            if(i,j) not in memory:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    current = i < len(text) and pattern[j] in {text[i], '.'}
                    
                    if j + 1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or current and dp(i+1, j)
                    else:
                        ans = current and dp(i+1, j+1)
                memory[i,j] = ans
            return memory[i,j]
        return dp(0,0)
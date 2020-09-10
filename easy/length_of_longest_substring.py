class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        best = 0
        for c in s:
            if c in sub:
                sub = sub[sub.index(c)+1:] 
            sub += c
            best = max(best, len(sub))
        return best
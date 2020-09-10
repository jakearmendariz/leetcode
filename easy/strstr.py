class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        if n == 0:
            return 0
        if needle == haystack:
            return 0
        
        for i in range(0, len(haystack)-n+1):
            if haystack[i:i+n] == needle:
                return i
        return -1
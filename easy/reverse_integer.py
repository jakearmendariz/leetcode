class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while(x > 0):
            rev *= 10
            rev += x%10
            x= int(x/10)
        if rev > 2147483647 or rev < -2147483648:
            return 0
        return rev * sign
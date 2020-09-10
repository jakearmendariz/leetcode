class Solution:  
    def consecutiveNumbersSum(self, N: int) -> int:
        def sum_from(n): 
            return (n*(n+1))/2
        n = 2
        result = 1
        sum = 1
        while(sum < N):
            if (N-sum)%n == 0:
                result += 1
            sum += n
            n+=1
        return result
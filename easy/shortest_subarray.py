class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        history = {}
        max_degree = 0
        min_diff = 500000
        for i,n in enumerate(nums):
            if n not in history:
                history[n] = [i,1]
            else:
                history[n][1] += 1
                if  history[n][1] > max_degree:
                    max_degree = history[n][1]
                    min_diff = i - history[n][0] + 1
                elif history[n][1] == max_degree:
                    min_diff = min(i - history[n][0] + 1, min_diff)
        if min_diff == 500000:
            if len(nums) == 0: return 0
            else: return 1
        return min_diff